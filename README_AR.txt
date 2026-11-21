تحديث التصميم الزجاجي

هذا الإصدار يتضمن إعادة تصميم واجهة MR Store بالكامل بطابع Glassmorphism، مع الحفاظ على تسجيل الدخول وقسم الأدمن. عند تحديث مستودع GitHub، ارفع المشروع كاملاً أو استبدل الملفات الموجودة في الأرشيف، خصوصاً www/index.html وwww/login.html وwww/glass-redesign.css وcapacitor.config.json. خطوات البناء موجودة في [DESIGN_UPDATE_AR.md](DESIGN_UPDATE_AR.md).

---

إصلاح تسجيل الدخول بجوجل - MR Store

استبدل الملفين في مستودع GitHub بنفس المسارات:

1. native-google-auth.js (في جذر المستودع)
2. capacitor.config.json (في جذر المستودع)

ثم اعمل Commit Changes وشغّل GitHub Actions لبناء APK جديد.

#تحديث مهم في Google Cloud قبل تجربة APK الجديد

آخر عملية بناء ناجحة كانت Workflow Run رقم 44941545115، وبصمة شهادة APK المرفوع منها هي:

- SHA-1: B0:71:7D:02:12:A0:87:E0:16:79:B2:8C:D9:F6:DE:35:74:46:12:6B
- Package name: com.mrstore.app

افتح Android OAuth Client في مشروع mr-gaming-24803، واجعل SHA-1 هي القيمة أعلاه. لا تضع SHA-1 القديمة E0:50:... لهذه النسخة الحالية.

اترك Web Client ID كما هو في native-google-auth.js وserverClientId:
443646227114-vbstcio2leo5l5ene86mtmd9cv6djdln.apps.googleusercontent.com

اترك Android Client ID مسجلاً في Google Cloud مع Package name وSHA-1؛ لا تستخدمه كـ Web Client ID.

#بعد البناء

نزّل APK من نفس عملية البناء الجديدة وثبّته. إذا استمر الخطأ، أرسل نص رسالة الخطأ التفصيلية أو رقم الخطأ الذي يظهر، ولا ترسل أي كلمات مرور أو مفاتيح سرية.

إصلاح بناء APK: تمت إضافة معالجة تلقائية لاعتمادية Kotlin التي تظهر مع Google Services. التفاصيل في FIX_ANDROID_BUILD_AR.md.
