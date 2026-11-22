# شاشة البداية والأيقونة واسم الـ APK

## اللي اتغيّر
- **شاشة البداية (Splash):** خلفية كحلي غامق `#0A1230` مع لوجو MR Store وهالة دهبية خفيفة حواليه، بدل الخلفية البنية/السودا القديمة.
- **أيقونة التطبيق:** اتعملت من اللوجو بعد إزالة الزوايا السودا، وبأحجام صح لكل الشاشات (Adaptive + Legacy + Round).
- **اسم التطبيق على الموبايل:** `MR Store` (من `capacitor.config.json`).
- **اسم ملف الـ APK:** `MR-Store.apk` بدل `app-debug.apk`، ومعاه Release ثابت على GitHub.

## تحميل التطبيق من GitHub
بعد ما الـ workflow **Build MR Store APK** يخلص:
1. **Releases** ← أحدث إصدار `MR Store` ← حمّل `MR-Store.apk`، أو
2. **Actions** ← آخر تشغيل ← **Artifacts** ← `MR-Store`.

رابط التحميل المباشر الثابت:
`https://github.com/<اسم-المستخدم>/<اسم-المستودع>/releases/latest/download/MR-Store.apk`

## الملفات
- `design/mr-store-logo-original.png` — اللوجو الأصلي (للاحتفاظ بيه فقط).
- `assets/` — صور الأيقونة والسبلاتش اللي بتتولد منها الموارد.
- `android-overrides/res/` — الأيقونات النهائية وصورة لوجو السبلاتش ولون الخلفية.
- `.github/scripts/apply_android_overrides.py` — بيطبّق التعديلات دي على مشروع الأندرويد وقت البناء.
- لتغيير لون الخلفية: عدّل `android-overrides/res/values/mr_store_colors.xml`.
