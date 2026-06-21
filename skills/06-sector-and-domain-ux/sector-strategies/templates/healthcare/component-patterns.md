---
title: Healthcare Component Patterns
sector: healthcare
---

# Healthcare: Component Patterns

HTML/Tailwind patterns for healthcare websites.

## Appointment Booking CTA (Hero)
```html
<section class="py-16 bg-blue-50 text-center">
  <h1 class="text-4xl font-bold text-blue-900 mb-4">Book Your Appointment</h1>
  <button class="px-8 py-3 bg-blue-700 text-white font-semibold rounded">
    Schedule Now →
  </button>
</section>
```

## Doctor Profile Card
```html
<div class="bg-white rounded-lg shadow p-6">
  <img src="doctor.jpg" alt="Dr. Smith" class="h-40 w-40 rounded-full mx-auto mb-4 object-cover" />
  <h3 class="font-bold text-lg text-center">Dr. Sarah Smith</h3>
  <p class="text-center text-green-600 font-semibold">Cardiology Specialist</p>
  <p class="text-center text-gray-600 text-sm mt-2">MD Harvard • 12+ years practice</p>
  <div class="mt-4 flex gap-2">⭐⭐⭐⭐⭐ (47 reviews)</div>
  <button class="mt-4 w-full px-4 py-2 bg-blue-700 text-white rounded">Book with Dr. Smith</button>
</div>
```

## Specialty Finder
```html
<div class="grid md:grid-cols-3 gap-4">
  <div class="p-4 border rounded hover:shadow-lg cursor-pointer">
    <div class="text-3xl mb-2">🫀</div>
    <h3 class="font-bold">Cardiology</h3>
    <p class="text-sm text-gray-600">Heart & vascular care</p>
  </div>
</div>
```

---

See **tour-travel/component-patterns.md** for complete code examples with Tailwind class details and responsive design patterns.
