db = db.getSiblingDB('ecommerce');
db.users.insertMany([
  { id: "1", name: "Alice" },
  { id: "2", name: "Bob" }
]);

db.products.insertMany([
  { id: "1001", name: "Laptop", price: 1200 },
  { id: "1002", name: "Smartphone", price: 800 },
  { id: "1003", name: "Tablet", price: 600 }
]);

db.orders.insertMany([
  { order_id: "101", user_id: "1", product_id: "1001" },
  { order_id: "102", user_id: "1", product_id: "1002" },
  { order_id: "103", user_id: "2", product_id: "1003" }
]);
