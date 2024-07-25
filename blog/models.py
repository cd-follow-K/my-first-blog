# Create your models here.
from django.conf import settings  # settingsモジュールから設定をインポート
from django.db import models      # modelsモジュールからモデルをインポート
from django.utils import timezone # timezoneモジュールからタイムゾーンをインポート

# Postモデルを定義するクラス
class Post(models.Model):  # Postモデルの定義開始。Postはモデルの名前で、models.Modelを継承することでDjangoのモデルであることを示す。
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    # authorフィールドを定義。これはForeignKeyとしてユーザーモデルに関連付けられ、関連ユーザーが削除されるとPostも削除される。

    title = models.CharField(max_length=200)  
    # titleフィールドを定義。これはCharFieldで、最大200文字のテキストフィールド。

    text = models.TextField()  
    # textフィールドを定義。これはTextFieldで、大量のテキストデータを保存するためのフィールド。

    created_date = models.DateTimeField(default=timezone.now)  
    # created_dateフィールドを定義。これはDateTimeFieldで、デフォルト値として現在の日時を使用。

    published_date = models.DateTimeField(blank=True, null=True)  
    # published_dateフィールドを定義。これはDateTimeFieldで、空白とnullを許可するオプションフィールド。

    def publish(self):  # ブログ投稿を公開するためのメソッドを定義。
        self.published_date = timezone.now()  # 現在の日時をpublished_dateフィールドに設定。
        self.save()  # オブジェクトの現在の状態をデータベースに保存。

    def __str__(self):  # オブジェクトを文字列として表現する方法を定義。
        return self.title   # 投稿のタイトルを返す。

# このモデルは、データベースに保存する必要があることをDjangoに知らせる役割を持つ。


