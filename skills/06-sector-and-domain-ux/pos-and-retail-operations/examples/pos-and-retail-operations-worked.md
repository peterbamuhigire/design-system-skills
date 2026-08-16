# Worked Example: One Tenant, Three POS Surfaces

Tenant: Nile Harvest Foods Ltd. The tenant setting
`pos_default_customer_id` points to the active customer **Walk-in**.

## What the operator sees

- `pos.php` loads Walk-in, shows the current shop and store, and offers mapped
  finished products only.
- `agent-pos.php` loads the same Walk-in customer, then adds the selected
  sales agent and agent-store context. It does not expose packaging or raw
  ingredients.
- `encode-sales.php` loads the same Walk-in customer, then records the manual
  invoice date/reference and sales point. It is not used for quote delivery or
  payment collection.

## What the data model means

“Nile Harvest Cured Vanilla Beans Grade A Prime Gourmet 1 kg” is the product.
Its one mapped finished stock item owns batches, cost, unit, and balance. The
recipe may consume cured vanilla beans, packaging, and labels when the item is
manufactured. A later sale consumes one unit of the finished stock item only.

## What QA proves

1. Changing the tenant default updates all three surfaces on their next load.
2. Deactivating the configured customer produces a configuration error rather
   than choosing another customer.
3. A manufacturing job decreases ingredient balances and increases finished
   stock; a sale decreases finished stock and does not decrease ingredients a
   second time.
4. Repeating a timed-out payment with the same idempotency key returns the
   existing result and does not create a second sale.
