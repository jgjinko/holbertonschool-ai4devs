const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// Mock Database
let inventory = [
  { sku: "WJK01", name: "Winter Jacket", total_stock: 150, channels: [{ platform: "Shopify", stock: 50 }] },
  { sku: "WBT02", name: "Winter Boots", total_stock: 80, channels: [{ platform: "Amazon", stock: 30 }] }
];

// Helper: Basic Error Formatter
const errorRes = (res, status, message) => {
  return res.status(status).json({ status, error: message });
};

// 1. READ (List) - Paginated
app.get('/inventory', (req, res) => {
  const limit = parseInt(req.query.limit) || 20;
  const offset = parseInt(req.query.offset) || 0;
  
  const paginatedItems = inventory.slice(offset, offset + limit);
  
  res.json({
    total: inventory.length,
    limit,
    offset,
    items: paginatedItems
  });
});

// 2. CREATE - New SKU
app.post('/inventory', (req, res) => {
  const { sku, name, total_stock, channels } = req.body;
  if (!sku || !name) return errorRes(res, 400, "Missing required fields (sku/name)");
  
  if (inventory.find(i => i.sku === sku)) return errorRes(res, 400, "SKU already exists");

  const newItem = { sku, name, total_stock: total_stock || 0, channels: channels || [] };
  inventory.push(newItem);
  res.status(201).json(newItem);
});

// 3. READ (Detail) - Specific SKU
app.get('/inventory/:sku', (req, res) => {
  const item = inventory.find(i => i.sku === req.params.sku);
  if (!item) return errorRes(res, 404, "SKU not found");
  res.json(item);
});

// 4. UPDATE - Stock Level
app.patch('/inventory/:sku', (req, res) => {
  const item = inventory.find(i => i.sku === req.params.sku);
  if (!item) return errorRes(res, 404, "SKU not found");

  const { total_stock } = req.body;
  if (typeof total_stock === 'number') {
    item.total_stock = total_stock;
    return res.json({ message: "Stock updated", item });
  }
  errorRes(res, 400, "Invalid stock data");
});

// 5. DELETE - Remove SKU
app.delete('/inventory/:sku', (req, res) => {
  const index = inventory.findIndex(i => i.sku === req.params.sku);
  if (index === -1) return errorRes(res, 404, "SKU not found");

  inventory.splice(index, 1);
  res.status(204).send();
});

app.listen(port, () => {
  console.log(`StockSync API running at http://localhost:${port}`);
});