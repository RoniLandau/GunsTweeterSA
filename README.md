קישור לאתר הפרוייקט -
https://litalfeldman19.wixsite.com/my-site-1

 # מטרת הפרויקט

המטרה היא לבדוק האם בעת מקרי ירי או אסונות בארה"ב הסנטימנט כלפי אחזקת נשק חם משתנה. כמו כן, האם מדינות בתוך ארה"ב שמזוהות עם דעה ברורה בנושא אחזקת הנשק החם, משנות את עמדתן בהינתן אירועים כאלו.


# רקע - השאלה או המאבק החברתי

כ-30% מכלל הבוגרים בארצות הברית מחזיקים נשק כמו אקדחים, רובים ותתי מקלע. כמעט שני שליש מהתושבים בארצות הברית חיו בשלב כלשהו של חייהם בבית שהיה בו נשק חם. לדבר זה השפעה חמורה על שיעור הרציחות, התאונות וההתאבדויות מנשק חם. מעל 33 אלף מתושבי ארה"ב מתים בכל שנה עקב ירי בנשק קל. שיעור הרצח בארצות הברית שמעורב בו נשק חם גבוה פי 19 לעומת מדינות מערביות אחרות, מקרי ההתאבדויות והתאונות מנשק חם גבוהים במאות אחוזים. 

נושא נשיאת הנשק בקרב תושבי ארה"ב שנוי במחלוקת ובשונה מהנתונים לעיל, יש הטוענים שנשיאת נשק אישי להגנה עצמית נחשבת בין היתר לחירות בסיסית. 

# הקשר למדעי הרוח הדיגיטליים

בפרוייקט שלנו ניקח טקסט לא מעובד – תוכן של ציוצי טוויטר ונעבד אותו באמצעות אלגוריתם לשיוך סנטימנט. לאחר עיבודו, ננתח את התוצאות. כלומר נשתמש בכלי דיגיטלי על מנת לחקור טקסטים מסויימים מתחום מדעי הרוח.

# תכנית עבודה - כלים

-	שימוש בapi של טוויטר לטובת שליפת תוכן הציוצים – נבצע שאילתא תחומה גאוגרפית בארה"ב הכוללת מילים מסויימות שקשורות לנושא הנשק החם.
-	שימוש באלגוריתם Vader על מנת לתייג את הציוצים - אלגוריתם Vader  הוא אלגוריתם לזיהוי סנטימנט חיובי או שלילי ועוצמתו. אלגוריתם זה מומלץ לניתוח סנטימנט שמבוטא ברשתות חברתיות, בינהן טוויטר. 
-	בתקופות בהן יש תוצאות חריגות (ריבוי סנטימנט חיובי או שלילי), נבצע חיפוש ממוקד על מנת להבין האם התרחש אירוע חריג – נבצע "קריאה צמודה".
-	ננתח את המטה-דאטה שהגיעה מהשאילתא כדי לנסות להבין האם במדינות מסויימות בארה"ב יש שוני בסנטימנט.
-	נשתמש בPlotly על מנת לבצע ויזואליזציה גרפית באמצעות הצגת התוצאות על גבי ציר זמן ועל גבי מפה.
-	נציג את הפרויקט שלנו באמצעות אתר Wix. 


# סוג הפרויקט  

הפרויקט הוא פרויקט של קריאה משולבת – מצד אחד, אנו מבצעים קריאה רחוקה כאשר אנו שולפים מסה של נתונים בקריאת API ומפעילים עליה אלגוריתם לניתוח סנטימנט. מצד שני, אנו מבצעים קריאה צמודה כך שעבור תוצאות חריגות, אנו בוחנים לעומק תקופות ובודקים האם התרחשו אירועים שעשויים לשקף את תוצאות האלו.

# היעד 
לחקור את השיח העוסק בשימוש בנשק בארה"ב, כפי שמשתקף בציוצים ברשת החברתית טוויטר.
כמו כן, הצגת התוצאות על גבי ציר זמן, עם התייחסות לנקודות חריגות בגרף כרפרנסים לאירועים שהיו באותן תקופות.

# הערכות 

להערכתינו, לאחר אירועי ירי המוניים בבתי ספר או לאחר אסונות שקשורים לנשק חם, הסנטימנט השלילי לגבי החזקת כלי נשק ע"י אזרחים פרטיים כפי שמשתקף בציוצים בטוויטר יעלה. זאת לאור הטראומה הקולקטיבית והעלייה בתיעוד האירוע ותיאוריהם של עדי ראייה.
כמו כן, אנו צופים שיח שלילי יותר רווח במדינות שמחמירות בהחזקת נשק חם (לדוגמא בוסטון) לעומת שיח חיובי במדינות שמתירות נשק חם ומעודדות שימוש בו להגנה עצמית (לדוגמא אלבאמה).

# סיכום ומסקנות

מניתוח של כ-8000 ציוצים ששלפנו, בין התאריכים 16-22.7.2022, ניתן לראות כי 4000 ציוצים הם בעלי סנטימנט שלילי, 2000 בעלי סנטימנט חיובי ו2000 בעלי סנטימנט נייטרלי.  מניתוח הסנטימנט של המדינות עלה כי יותר מ90% מהמדינות מזוהות עם סנטימנט שלילי לכן לא ניתן להצביע על קורלציה חד משמעית בין המפלגה הדומיננטית במדינה לבין הסנטימנט. כמו כן, נוכחנו לגלות כי ב18.07.22 היה מספר ציוצים גבוה יחסית לשאר הימים ולאחר ביצוע קריאה צמודה, גילינו שאכן היה אירוע ירי בתאריך זה, שהתרחש באינדיאנה.
ניכר כי רב השיח על נשקים ברשת החברתית טוויטר, בימים בהם חקרנו אותו, הוא שיח שלילי. ייתכן והדבר מצביע על כך שמרבית משתמשי טוויטר מתנגדים לאחזקת נשק.
# ביבליוגרפיה

Twitter API - https://developer.twitter.com/en/docs/twitter-api

VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text by C.J. Hutto and Eric Gilbert

VADER Sentiment Analysis repo -
https://github.com/cjhutto/vaderSentiment

Guns in the US background - https://ecowiki.org.il/wiki/%D7%A0%D7%A9%D7%A7_%D7%91%D7%90%D7%A8%D7%A6%D7%95%D7%AA_%D7%94%D7%91%D7%A8%D7%99%D7%AA

Like It or Not: A Survey of Twitter Sentiment Analysis Methods by ANASTASIA GIACHANOU and FABIO CRESTANI, Universita della Svizzera Italiana  -
http://old-eclass.uop.gr/modules/document/file.php/DIT104/%CE%92%CE%B9%CE%B2%CE%BB%CE%B9%CE%BF%CE%B3%CF%81%CE%B1%CF%86%CE%AF%CE%B1%202017-2018/Like%20It%20or%20Not%20A%20Survey%20of%20Twitter%20Sentiment%20Analysis%20Methods.pdf
