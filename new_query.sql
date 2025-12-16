
SELECT * FROM Animal;
SELECT * FROM Shelter;
SELECT * FROM Adopter;
SELECT * FROM animal_remark;

動物完整資料卡片查詢：
SELECT
  a.id, a.sub_id, a.kind, a.variety, a.sex, a.age, a.status,
  s.name AS shelter_name, s.address, s.phone AS shelter_phone,
  ad.name AS adopter_name, ad.phone AS adopter_phone,
  a.opendate, a.adoption_date
FROM Animal a
LEFT JOIN Shelter s ON a.shelter_pkid = s.id
LEFT JOIN Adopter ad ON a.adopter_id = ad.id
ORDER BY a.update_at DESC
LIMIT 30;

目前可認養清單（未被領養）：
SELECT a.id, a.kind, a.variety, a.sex, a.age, a.opendate, s.name AS shelter
FROM Animal a
JOIN Shelter s ON a.shelter_pkid = s.id
WHERE a.adopter_id IS NULL
ORDER BY date(a.opendate) DESC, a.id DESC;

各收容所目前「待領養數量」排行榜：
SELECT s.name, COUNT(*) AS waiting_cnt
FROM Animal a
JOIN Shelter s ON a.shelter_pkid = s.id
WHERE a.adopter_id IS NULL
GROUP BY s.id
ORDER BY waiting_cnt DESC, s.name;

各收容所「總收容」與「已領養」比例排行榜：
SELECT
  s.name,
  COUNT(*) AS total_animals,
  SUM(CASE WHEN a.adopter_id IS NOT NULL THEN 1 ELSE 0 END) AS adopted,
  ROUND(
    100.0 * SUM(CASE WHEN a.adopter_id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*),
    1
  ) AS adopted_rate_pct
FROM Animal a
JOIN Shelter s ON a.shelter_pkid = s.id
GROUP BY s.id
ORDER BY adopted_rate_pct DESC, total_animals DESC;

領養效率：從開放日到領養日平均花幾天？
SELECT
  s.name,
  ROUND(AVG(julianday(date(a.adoption_date)) - julianday(date(a.opendate))), 1) AS avg_days_to_adopt,
  COUNT(*) AS adopted_cnt
FROM Animal a
JOIN Shelter s ON a.shelter_pkid = s.id
WHERE a.adopter_id IS NOT NULL
  AND a.adoption_date IS NOT NULL
  AND a.opendate IS NOT NULL
GROUP BY s.id
HAVING adopted_cnt >= 5
ORDER BY avg_days_to_adopt ASC;

動物種類分布（kind）+ 性別（sex）交叉表
SELECT
  kind,
  SUM(CASE WHEN sex='M' THEN 1 ELSE 0 END) AS male_cnt,
  SUM(CASE WHEN sex='F' THEN 1 ELSE 0 END) AS female_cnt,
  SUM(CASE WHEN sex IS NULL OR sex='' THEN 1 ELSE 0 END) AS unknown_cnt,
  COUNT(*) AS total
FROM Animal
GROUP BY kind
ORDER BY total DESC;

加分小招：做一個 View，demo 更像「系統」
CREATE VIEW v_animal_full AS
SELECT
  a.*,
  s.name AS shelter_name, s.address AS shelter_address, s.phone AS shelter_phone,
  ad.name AS adopter_name, ad.phone AS adopter_phone, ad.email AS adopter_email
FROM Animal a
LEFT JOIN Shelter s ON a.shelter_pkid = s.id
LEFT JOIN Adopter ad ON a.adopter_id = ad.id;
然後 demo 就用：
SELECT id, kind, variety, shelter_name, adopter_name
FROM v_animal_full
ORDER BY datetime(update_at) DESC
LIMIT 20;