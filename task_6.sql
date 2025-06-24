INSERT INTO customer ( 
  customer_id,
  customer_name,
  email,
  address
)
VALUES (
  2, 
  'Blessing Malik',
  'bmalik@sandtech.com',
  '124 Happiness Ave.'
)

VALUES (
  3, 
  'Obed Ehoneah',
  'eobed@sandtech.com',
  '125 Happiness Ave.'
)

VALUES (
  4, 
  'Nehemial Kamolu',
  'nkamolu@sandtech.com',
  '126 Happiness Ave.'
)
WHERE 
  TABLE_NAME = 'Books'
  AND TABLE_SCHEMA = 'alx_book_store';
