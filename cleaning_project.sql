use world_layoff;
SELECT *
FROM layoffs_staging;

SELECT *
FROM layoffs;

DROP TABLE students;

DROP TABLE studentsss;

DROP TABLE layoffs_staging2;

DROP TABLE layoffs_staging;

CREATE TABLE layoffs_staging 
like layoffs;

INSERT layoffs_staging
SELECT *
FROM layoffs;

SELECT *
FROM layoffs_staging;

SELECT*,
ROW_NUMBER() OVER( PARTITION BY company,location, industry, total_laid_off,percentage_laid_off, `date`,stage,country,funds_raised_millions) AS row_num
FROM layoffs_staging;

WITH duplicate_removal AS(
SELECT*,
ROW_NUMBER() OVER( PARTITION BY company,location, industry, total_laid_off,percentage_laid_off, `date`,stage,country,funds_raised_millions) AS row_num
FROM layoffs_staging)
SELECT*
FROM duplicate_removal WHERE row_num > 1;

SELECT *
FROM layoffs_staging WHERE company = 'Casper';

CREATE TABLE layoffs_staging2
LIKE layoffs_staging;

SELECT *
FROM layoffs_staging2;

DROP TABLE layoffs_staging2;

CREATE TABLE layoffs_staging2(
company text,
location text, 
industry text,
total_laid_off int, 
percentage_laid_off text, 
`date` text ,
stage text ,
country text, 
funds_raised_millions int,
row_num int);

INSERT  layoffs_staging2
SELECT*,
ROW_NUMBER() OVER( PARTITION BY company,location, industry, total_laid_off,percentage_laid_off, `date`,stage,country,funds_raised_millions) AS row_num
FROM layoffs_staging;

SET SQL_SAFE_UPDATES = 0;

DELETE
FROM layoffs_staging2 WHERE row_num > 1;

SELECT *
FROM layoffs_staging2 WHERE row_num > 1;

ALTER TABLE layoffs_staging2
DROP COLUMN row_num;

SELECT *
FROM layoffs_staging2;

SELECT DISTINCT industry
FROM layoffs_staging2;

-- After those processes we have gotten rid of any duplicate values in our dataset

SELECT TRIM(company)
FROM layoffs_staging2;

UPDATE layoffs_staging2
SET company = TRIM(company);

SELECT DISTINCT location
FROM layoffs_staging2;

SELECT DISTINCT industry
FROM layoffs_staging2 order by 1;
-- The industry column has; crypto, cryptocurrency and crypto currency as different industries which will bring problems to us when visualising data.

UPDATE layoffs_staging2
SET industry = 'Crypto'
WHERE industry LIKE 'Crypto%';

SELECT  industry
FROM layoffs_staging2 WHERE industry like 'crypto%';

SELECT date , str_to_date(date, '%m/%d/%Y') as DT
FROM layoffs_staging2;

-- changing the data type of my date from text to date
UPDATE layoffs_staging2
SET `date` = str_to_date(`date`, '%m/%d/%Y');

SELECT `date`
FROM layoffs_staging2;

ALTER TABLE layoffs_staging2
MODIFY COLUMN `date` date;

SELECT DISTINCT COUNTRY
FROM layoffs_staging2 order by 1;
-- United States seems to have two values which may also bring problems when visualising the data

UPDATE layoffs_staging2
SET country = 'United States'
WHERE country LIKE 'United States%';

SELECT t1.industry,t2.industry
FROM layoffs_staging2 t1
JOIN  layoffs_staging2 t2
	ON t1.company = t2.company
    WHERE t1.industry IS NULL 
    AND t2.industry IS NOT NULL;

UPDATE layoffs_staging2
SET industry = null
WHERE industry = '';

UPDATE layoffs_staging2 as t1
JOIN layoffs_staging2 as t2
	ON t1.company = t2.company
    SET t1.industry = t2.industry
    WHERE t1.industry IS NULL 
    AND t2.industry IS NOT NULL;
    
SELECT company 
FROM layoffs_staging2
WHERE industry  IS null;

SELECT *
FROM layoffs_staging2;

SELECT *
FROM layoffs_staging2
WHERE total_laid_off is null
and percentage_laid_off is null and funds_raised_millions is null;

DELETE
FROM layoffs_staging2
WHERE total_laid_off is null
and percentage_laid_off is null and funds_raised_millions is null;




