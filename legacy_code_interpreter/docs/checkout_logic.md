# Module: Checkout Logic (`checkout_process.php`)

## Overview
A monolithic procedural script that handles the finalization of an order. It processes payment, updates inventory, and sends confirmation emails.

## Logic Flow
1. Load order details from the session.
2. Initialize selected payment module.
3. Validate stock levels for all items in the cart.
4. Insert record into `orders` and `orders_products` tables.
5. Clear the shopping cart session.