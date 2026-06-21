---
title: Education Component Patterns
sector: education
---

# Education: Component Patterns

HTML/Tailwind patterns optimized for education websites.

## Key Components for Education Sites

### Enrollment CTA Hero
```html
<section class="relative py-20 bg-gradient-to-r from-blue-700 to-green-600 text-white text-center">
  <h1 class="text-5xl font-bold mb-4">Enroll Now</h1>
  <p class="text-xl mb-8">Secure your spot in our next cohort</p>
  <button class="px-8 py-3 bg-white text-blue-700 font-semibold rounded hover:shadow-lg">
    Start Application →
  </button>
</section>
```

### Program/Course Card
```html
<div class="bg-white rounded-lg shadow p-6 hover:shadow-lg transition">
  <div class="h-40 bg-blue-100 rounded mb-4"></div>
  <h3 class="font-bold text-lg mb-2">Program Name</h3>
  <p class="text-gray-600 text-sm mb-4">Brief description of program outcomes.</p>
  <div class="flex justify-between items-center">
    <span class="text-sm font-semibold text-gold">12 months</span>
    <button class="px-4 py-2 bg-blue-700 text-white rounded text-sm">Learn More</button>
  </div>
</div>
```

### Faculty Profile
```html
<div class="text-center">
  <img src="faculty.jpg" alt="Dr. Jane Smith" class="h-32 w-32 rounded-full mx-auto mb-4 object-cover" />
  <h3 class="font-bold text-lg">Dr. Jane Smith</h3>
  <p class="text-green-600 text-sm font-semibold mb-2">Head of Computer Science</p>
  <p class="text-gray-600 text-sm">PhD Stanford, 15+ years in industry</p>
</div>
```

### Event Calendar List
```html
<div class="space-y-3">
  <div class="flex gap-4 border-b pb-4">
    <div class="text-blue-700 font-bold text-lg w-12">25</div>
    <div class="flex-1">
      <h4 class="font-bold">Open House</h4>
      <p class="text-gray-600 text-sm">March 2024 • 2:00 PM</p>
      <button class="mt-2 text-sm text-blue-700 font-semibold">Register →</button>
    </div>
  </div>
</div>
```

---

See **tour-travel/component-patterns.md** for complete pattern examples with detailed code and styling guidance. Apply the same structure here with education-specific components (course cards, enrollment flows, faculty directories, event calendars).
