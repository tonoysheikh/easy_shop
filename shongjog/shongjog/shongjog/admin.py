from django.contrib import admin

from .models import Infomation_Home
from .models import Registration
from .models import Top_product
from .models import For_home
from .models import Recently_view
from .models import Trending
from .models import Review
from .models import Contact
from .models import Recommended
from .models import order

admin.site.register(Infomation_Home)
admin.site.register(Registration)
admin.site.register(Top_product)
admin.site.register(For_home)
admin.site.register(Recently_view)
admin.site.register(Trending)
admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(Recommended)
admin.site.register(order)
