# MR Store — Android APK project

مشروع Android مبني باستخدام Capacitor ويحتفظ بملفات المتجر الأصلية داخل `www/`.

## المميزات
- تطبيق Android باسم **MR Store** ومعرّف `com.mrstore.app`.
- الموقع الأصلي `index.html` وصفحة تسجيل الدخول `login.html`.
- شريط تنقل سفلي زجاجي وشفاف على شاشات الموبايل.
- اختيار العربية / English وحفظ الاختيار على الجهاز.
- زر تبديل الوضع الليلي من الإعدادات.
- أيقونة مخصصة للتطبيق.
- GitHub Actions لبناء APK تلقائياً.

## إخراج APK من GitHub
1. أنشئ Repository جديد وارفع كل محتويات هذا المجلد.
2. افتح تبويب **Actions**.
3. اختر **Build MR Store APK** ثم **Run workflow**، أو انتظر البناء بعد Push.
4. بعد نجاح العملية افتح نتيجة التشغيل وانزل إلى **Artifacts**.
5. حمّل `MR-Store-APK` وستجد بداخله `app-debug.apk`.

## تشغيل محلياً
يتطلب Node.js 20 وJava 17 وAndroid SDK:
```bash
npm install
npx capacitor-assets generate --android
npx cap add android
npx cap sync android
cd android
./gradlew assembleDebug
```

## تنبيهات مهمة
- التطبيق يعرض موقع المتجر داخل غلاف Android؛ بيانات المنتجات والحسابات تظل مرتبطة بإعدادات Firebase الموجودة في ملفات الموقع.
- تسجيل Google قد يحتاج إعداد OAuth لإضافة بصمة SHA-1 / SHA-256 الخاصة بتطبيق Android وربطها بمشروع Google/Firebase. لا يمكن ضمان عمل تسجيل Google على Android قبل إكمال ذلك.
- قبل نشر نسخة إنتاجية، راجع قواعد Firebase Security Rules ولا تضع أسرار إدارية أو صلاحيات موثوقة داخل كود الواجهة.
- الـ workflow ينتج APK تجريبياً (debug) مناسباً للتثبيت والاختبار؛ للنشر على Google Play استخدم توقيع release.
