UPDATE
  awscost
/* Set to the new status */
SET end_date = '2020-04-23'
WHERE
  /* Include the old status in the WHERE clause */
  end_date = '0000-00-00'
