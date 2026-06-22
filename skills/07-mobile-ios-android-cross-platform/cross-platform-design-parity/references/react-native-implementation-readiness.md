# React Native Implementation Readiness

Use this after the parity decision has been made. It does not replace platform-native iOS/Android
design review; it checks whether a React Native or Expo team can actually build the specified
parity without flattening it into generic UI.

Source basis: project patterns from the local React Native cross-platform application-development
book were used as historical implementation-pattern input only. Current architecture, performance,
build, and update expectations must be checked against the official React Native and Expo docs.

---

## Current platform baseline

- React Native 0.76+ enables the New Architecture by default. Treat JSI/native interop,
  synchronous layout/effects, and concurrent rendering as the current baseline, not as an exotic
  future mode.
- Performance review must happen in release builds, not debug builds.
- Keep the 60 FPS target visible: a frame has about 16.67 ms of budget. Separate JS-thread
  jank from UI-thread jank when diagnosing interactions.
- For Expo projects, identify whether EAS Build and EAS Update are in scope before promising
  native dependencies, permissions, over-the-air updates, or release channels.

## Readiness checklist

| Area | Required design/handoff decision |
|---|---|
| Navigation shell | Same IA and destinations; native-feeling shell per platform. State whether React Navigation native-stack, Expo Router, tabs, drawers, or nested stacks are expected. |
| Screen architecture | Identify screens, reusable components, state owners, service/API modules, native modules, and asset folders. |
| Platform branches | Mark every required `Platform.OS`, `Platform.select`, `.ios/.android` file, or runtime branch. Do not leave divergence as a verbal note. |
| State model | Specify loading, error, empty, offline, syncing, stale-data, optimistic, permission-denied, and retry states. |
| Native APIs | For camera, maps, geolocation, notifications, media, biometrics, sharing, files, or contacts, define permission, unavailable-device, denied, limited, and recovery states. |
| Lists and feeds | Require virtualized rendering (`FlatList`, `SectionList`, FlashList, or equivalent) and define row height, separators, swipe affordances, placeholders, and pagination/loading behavior. |
| Forms and keyboard | Define keyboard type, submit behavior, validation timing, safe-area/keyboard avoidance, focus order, and error copy. |
| Responsive layout | Define compact/large phone, tablet/foldable, orientation, safe-area, notch, status/nav bar, pointer/keyboard, and text-scaling behavior. |
| Motion and gestures | Prefer native-stack transitions and platform-native gestures. Mark JS-driven animation as intentional and testable, not default. |
| Assets and media | Specify image density, placeholders, upload/progress/failure states, cache behavior, and whether generated imagery is allowed. |
| Accessibility | Check labels, roles, focus order, reduce-motion, dynamic text scaling, touch targets, and screen-reader announcements on both platforms. |
| Build/release | Record Expo vs bare RN, required config plugins/native dependencies, EAS/build channels, app identifiers, permissions manifests, signing, and store-review risks. |

## Output addendum

Add a short "RN implementation readiness" block to the parity spec:

- `RN target:` Expo managed, Expo prebuild, or bare RN; minimum RN/Expo version if known.
- `Native dependencies:` list modules and permission surfaces.
- `Platform branches:` list branch points and owners.
- `Performance risks:` list screens likely to stress JS/UI thread, lists, media, maps, or animation.
- `Release gates:` release-build performance check, device smoke test, EAS/build-channel plan,
  accessibility pass, and store-review permission wording.

## Failure modes

- Treating React Native as "one design, one implementation" after the parity table already proved
  platform divergence is required.
- Designing a camera/map/chat/feed screen with no permission, offline, upload, or failure states.
- Approving custom JS transitions that were never tested against release-build frame budgets.
- Promising Expo updates or native modules without naming EAS/build-channel implications.
- Using the book-era library pattern as current authority instead of checking current RN/Expo docs.
