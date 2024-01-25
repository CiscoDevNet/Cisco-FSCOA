UPDATE
  awscost
/* Set to the new status */
SET start_date = '2020-04-01'
WHERE
  /* Include the old status in the WHERE clause */
  start_date = '0000-00-00'
