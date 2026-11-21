# إصلاح بناء APK في MR Store

تمت إضافة ملف Gradle init script لمعالجة الخطأ:

`Could not find org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.9.0`

الطلب يأتي بشكل غير مباشر من `com.google.android.gms:strict-version-matcher-plugin:1.2.4` الذي يستخدمه Google Services Gradle plugin. يوجّه ملف `.github/gradle/kotlin-stdlib-compat.init.gradle` طلبي `kotlin-stdlib-jdk8` و`kotlin-stdlib-jdk7` إلى `kotlin-stdlib` بالإصدار نفسه، لأن Kotlin دمج محتويات هذين المكوّنين في `kotlin-stdlib` منذ إصدار 1.8.0.

يتم تمرير ملف الإصلاح تلقائياً إلى Gradle في خطوة `Build debug APK` داخل `.github/workflows/android-apk.yml`. لا يتطلب ذلك تعديل ملفات تسجيل الدخول أو إعدادات Google Auth أو كود التطبيق.

## طريقة الاستخدام

ارفع المشروع كاملاً إلى GitHub، ثم شغّل Workflow باسم **Build MR Store APK**. إذا ظهر خطأ جديد بعد تجاوز رسالة Kotlin، فسيكون خطأً لاحقاً مستقلاً ويحتاج سجل البناء الجديد لتشخيصه.
