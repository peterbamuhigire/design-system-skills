---
title: E-commerce Component Patterns
sector: ecommerce
---

# E-commerce: Component Patterns

HTML/Tailwind patterns for e-commerce websites.

## Product Card (Grid)
```html
<div class="bg-white rounded-lg shadow hover:shadow-lg transition">
  <img src="product.jpg" alt="Product" class="w-full h-48 object-cover rounded-t" />
  <div class="p-4">
    <h3 class="font-bold text-lg">Product Name</h3>
    <div class="flex items-center gap-2 my-2">
      ⭐⭐⭐⭐⭐ (124 reviews)
    </div>
    <p class="text-gray-600 text-sm mb-3">Brief product description</p>
    <div class="flex justify-between items-center">
      <span class="text-2xl font-bold text-accent">$49.99</span>
      <button class="px-4 py-2 bg-accent text-white rounded font-semibold">
        Add to Cart
      </button>
    </div>
    <p class="text-green-600 text-sm mt-2">✓ In stock</p>
  </div>
</div>
```

## Product Review
```html
<div class="border-b pb-4 mb-4">
  <div class="flex gap-2 mb-2">⭐⭐⭐⭐⭐</div>
  <h4 class="font-bold">"Excellent quality!"</h4>
  <p class="text-gray-600 text-sm mb-2">Perfect fit and arrived quickly.</p>
  <p class="text-gray-500 text-xs">Sarah M. • Verified Purchase</p>
</div>
```

## Checkout CTA Section
```html
<section class="bg-gray-50 py-12 text-center">
  <h2 class="text-3xl font-bold mb-4">Ready to Order?</h2>
  <button class="px-8 py-4 bg-accent text-white font-bold text-lg rounded hover:shadow-lg">
    Proceed to Checkout
  </button>
  <div class="mt-6 flex justify-center gap-4 text-gray-600 text-sm">
    <span>🔒 Secure Payment</span>
    <span>✓ 30-Day Returns</span>
    <span>📦 Free Shipping</span>
  </div>
</section>
```

---

See **tour-travel/component-patterns.md** for complete detailed examples with full Tailwind classes and responsive design.
