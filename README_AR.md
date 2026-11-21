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


## إعداد تسجيل الدخول بجوجل على Android (مهم)

تم تجهيز التطبيق لاستخدام نافذة Google الأصلية على Android بدلاً من نافذة تسجيل الدخول داخل WebView؛ وهذا يعالج سبب رفض Google لتسجيل الدخول داخل المتصفح المضمّن. لكن يلزم ضبط OAuth مرة واحدة في Google Cloud/Firebase قبل أن يعمل على جهازك:

1. افتح Google Cloud Console ثم APIs & Services → Credentials.
2. احتفظ بعميل OAuth من نوع **Web application** الحالي؛ الـ Client ID الموجود في الكود يستخدم كـ `serverClientId`.
3. أنشئ عميل OAuth جديداً من نوع **Android** بالحزمة `com.mrstore.app` وبصمة SHA-1 الخاصة بتوقيع التطبيق. استخدم عميل Web الموجود كـ `serverClientId` ولا تضع Android Client ID مكانه.
4. لاستخراج بصمة Debug بعد إنشاء مجلد Android شغّل من المشروع: `cd android && ./gradlew signingReport`، وانسخ SHA-1 من variant `debug`. أضف أيضاً بصمة SHA-256 إلى إعدادات تطبيق Android في Firebase إذا طلبتها لوحة Firebase.
5. تأكد أن Google provider مفعّل في Firebase Authentication، وأن إعدادات OAuth تخص نفس مشروع Firebase المستخدم في الموقع.
6. بعد إضافة البصمة، أعد بناء APK من GitHub Actions وثبّت النسخة الجديدة. عند استخدام توقيع Release لاحقاً، أضف بصمة شهادة Release أيضاً.

**ملاحظة:** لا يمكن إصلاح رفض OAuth من تصميم الزر وحده؛ Google يحتاج مطابقة package name وبصمة شهادة Android مع عميل OAuth. تسجيل الدخول من متصفح الموقع يظل يستخدم Google Identity Services المعتاد.
