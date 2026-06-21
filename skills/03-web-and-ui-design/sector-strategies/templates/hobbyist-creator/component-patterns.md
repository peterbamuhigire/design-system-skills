---
title: Hobbyist/Creator Component Patterns
sector: hobbyist-creator
---

# Hobbyist/Creator: Component Patterns

HTML/Tailwind patterns for creator and hobbyist websites.

## Portfolio Grid (Hero Showcase)
```html
<div class="grid grid-cols-2 md:grid-cols-3 gap-4">
  <div class="group relative overflow-hidden rounded cursor-pointer">
    <img src="work-1.jpg" alt="Work title" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
    <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-all duration-300 flex items-center justify-center">
      <span class="text-white font-bold opacity-0 group-hover:opacity-100">View Project</span>
    </div>
  </div>
</div>
```

## Behind-the-Scenes Section
```html
<section class="py-12 bg-cream">
  <h2 class="text-3xl font-bold mb-8">How I Create</h2>
  <div class="grid md:grid-cols-2 gap-8">
    <img src="studio.jpg" alt="My studio" class="rounded-lg" />
    <div>
      <h3 class="text-xl font-bold mb-4">My Process</h3>
      <p class="text-gray-600 mb-4">Personal story about your creative process...</p>
      <ul class="space-y-2 text-gray-600">
        <li>✨ Step one of your process</li>
        <li>✨ Step two of your process</li>
        <li>✨ Step three of your process</li>
      </ul>
    </div>
  </div>
</section>
```

## Subscribe/Follow CTA
```html
<div class="bg-accent text-white rounded-lg p-8 text-center">
  <h3 class="text-2xl font-bold mb-2">Join 5K+ Followers</h3>
  <p class="mb-4">Get behind-the-scenes content and updates</p>
  <button class="px-6 py-3 bg-white text-accent font-bold rounded hover:shadow-lg">
    Subscribe to Newsletter
  </button>
  <div class="mt-4 flex justify-center gap-4">
    <a href="#" class="hover:opacity-80">Instagram</a>
    <a href="#" class="hover:opacity-80">Twitter</a>
    <a href="#" class="hover:opacity-80">YouTube</a>
  </div>
</div>
```

## About Section
```html
<section class="py-12 max-w-2xl">
  <div class="flex gap-8 items-start">
    <img src="creator.jpg" alt="Creator photo" class="h-48 w-48 rounded-full object-cover flex-shrink-0" />
    <div>
      <h2 class="text-3xl font-bold mb-4">About Me</h2>
      <p class="text-gray-600 leading-relaxed mb-4">
        Personal bio and why you create what you create...
      </p>
      <p class="text-gray-600 leading-relaxed">
        Your unique perspective and what makes your work valuable to your audience.
      </p>
    </div>
  </div>
</section>
```

---

See **tour-travel/component-patterns.md** for complete examples with full Tailwind classes and responsive design patterns.
