# React Native & Flutter — mapping a parity design to the framework

A cross-platform framework does **not** make a design native automatically. The parity decisions in
`ios-vs-android-idioms.md` still hold — the framework only changes *how* you implement each
Unify/Diverge call. For every element you have three strategies:

- **Shared** — one component, identical both sides (use for the Unify layer: brand, content, layout).
- **Adaptive** — one component that renders the platform-native form (RN `Platform.select` /
  Flutter `*.adaptive` constructors or `Theme.of(context).platform`).
- **Branched** — two distinct implementations selected at runtime (for deep Diverge cases:
  navigation containers, FAB-vs-bar primary action, motion systems).

Pick the lightest strategy that preserves nativeness. Defaulting everything to "Shared" is the
lowest-common-denominator anti-pattern; branching everything throws away the framework's value.

---

## React Native

| Parity element | Strategy | React Native resolution |
|---|---|---|
| Brand colour / type tokens | Shared | One token source (e.g. Restyle / Tamagui theme); same values both platforms |
| Navigation container | Branched | React Navigation: `BottomTabNavigator` styled per platform — native tab look on iOS, drive Material bottom-nav look on Android (or `expo-router` with platform layouts) |
| Back / header | Adaptive | `@react-navigation/native-stack` uses native headers (iOS large title, Android app bar) automatically; keep the system back gesture on both |
| Switch / toggle | Adaptive | RN `Switch` renders iOS pill vs Android M3 switch natively |
| Date/time picker | Branched | `@react-native-community/datetimepicker` shows the native wheel (iOS) vs calendar/clock dialog (Android) |
| Primary action | Branched | iOS: prominent button in content/bar. Android: a FAB component shown only on Android (`Platform.OS === 'android'`) |
| Action sheet / dialog | Adaptive | `ActionSheetIOS` on iOS; a Material dialog/bottom-sheet on Android — wrap behind one call site |
| Motion / transitions | Branched | Use native-stack default transitions (native per platform); avoid one custom JS animation forced on both |
| Lists | Shared+Adaptive | `FlashList`/`FlatList` shared; row chrome (swipe actions, chevrons) adaptive |
| Haptics | Adaptive | `expo-haptics` maps to each platform's generator |
| Reduce Motion | Shared | `AccessibilityInfo.isReduceMotionEnabled()` — honour on both |

**RN rule of thumb:** prefer **native-stack** and platform-native primitives over JS reimplementations;
use `Platform.select`/`Platform.OS` for the genuine Diverge rows; keep tokens and layout shared.

---

## Flutter

Flutter ships **two design languages in the box**: `MaterialApp`/Material widgets and
`CupertinoApp`/Cupertino widgets. Parity is a deliberate choice between them, not a default.

| Parity element | Strategy | Flutter resolution |
|---|---|---|
| Brand colour / type tokens | Shared | One `ThemeData` + custom `TextTheme` using the embedded brand face; reused across both target themes |
| App scaffold / navigation | Branched | `Scaffold` + `NavigationBar` (Material) vs `CupertinoTabScaffold`/`CupertinoTabBar`; switch on `Theme.of(context).platform` (or `defaultTargetPlatform`) |
| Back / header | Branched | `AppBar` (Material) vs `CupertinoNavigationBar`; both wired to system back |
| Switch / toggle | Adaptive | `Switch.adaptive(...)` renders Cupertino on iOS, Material on Android |
| Slider | Adaptive | `Slider.adaptive(...)` |
| Date/time picker | Branched | `showDatePicker`/`showTimePicker` (Material) vs `CupertinoDatePicker` in a modal |
| Dialog / action sheet | Adaptive/Branched | `showAdaptiveDialog` / `AlertDialog.adaptive`; for sheets, `CupertinoActionSheet` vs `showModalBottomSheet` |
| Primary action | Branched | Material `FloatingActionButton` (Android only) vs a Cupertino prominent button in the bar/content |
| Motion / transitions | Branched | `MaterialPageRoute` (Material transitions, M3 Expressive springs) vs `CupertinoPageRoute` (iOS slide + edge-swipe-back) |
| Icons | Branched | `Icons.*` (Material) vs `CupertinoIcons.*` — match the platform set |
| Lists | Shared+Adaptive | `ListView` shared; row affordances per platform (`Dismissible`, chevrons) |
| Reduce Motion | Shared | `MediaQuery.of(context).disableAnimations` — honour on both |

**Flutter rule of thumb:** use `.adaptive` constructors and `showAdaptive*` for the common
controls; switch on `defaultTargetPlatform` for the navigation scaffold and page transitions;
keep one `ThemeData`-driven brand layer. Do **not** ship Material on iOS just because it is the
Flutter default — that is the cloning anti-pattern in `ios-vs-android-idioms.md`.

---

## Decision shortcut

1. Is it brand/content/layout? → **Shared**.
2. Is it a standard control with an `.adaptive`/native variant? → **Adaptive**.
3. Is it navigation, primary-action placement, or motion? → **Branched** to the native form.
4. Re-run the result through `ios-ui-ux-design` and `android-ui-ux-design` — each side must pass
   its own gate independently, or the framework has flattened the design.
