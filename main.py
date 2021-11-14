import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from animechan import randomq
from animeAPI import search
import random

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['Animealıntısı'])
    async def quote(self, ctx:Context):
        a = randomq.Quotes()
        b = await a.random_quotes()
        animeName = b["anime"]
        c = search.AnimeSearch(what = "anime")
        d = await c.searchAnime1(anime_name = animeName)
        animeImage = d["image_url"]
        embedVar = discord.Embed(color = discord.Colour.dark_theme())
        embedVar.add_field(name = "Anime" , value = f"{animeName}")
        embedVar.add_field(name = "Karakter" , value = "{0}".format(b["character"]))
        embedVar.add_field(name = "Karakter" , value = "{0}".format(b["quote"]))
        embedVar.set_thumbnail(url = animeImage)
        await ctx.channel.send(embed = embedVar)
        return
    
    @quote.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send(":x: "+str(error))
        return
    
    ##################################################################################


    @commands.command(aliases = ['artofwar',"sun"])
    async def suntzu(self, ctx:Context):
        a = [
'Savaşı kazanan general, savaş yapılmadan önce tapınağında çok hesap yapar. Kaybeden general, önceden çok az hesap yapar.',
41
'Bir lider, zorla değil, örnek olarak liderlik eder.',
42
'Büyük bir gücün denetimi, birkaç kişinin denetimiyle aynı ilkedir: yalnızca sayılarını bölme sorunudur.',
43
'Bir kişinin birliklerini elden çıkarmanın en son noktası, kesin bir şekle sahip olmamaktır. O zaman en nüfuzlu casuslar içeri dalamazlar ve akıllılar da size karşı planlar yapamazlar.',
44
'Emirler açık ve net değilse, emirler tam olarak anlaşılmadıysa, suç generaldir. Ama emirleri açık ise ve askerler buna rağmen itaat etmiyorsa, o zaman subaylarının suçudur.',
45
'Taktiksiz strateji, zafere giden en yavaş yoldur. Stratejisiz taktik, yenilgiden önceki gürültüdür.',
46
'Tüm savaşlar aldatmaca üzerine kuruludur.',
47
'Savaşın zaferle sonuçlanacağı kesinse, o zaman savaşmalısınız.',
48
'Gücü yetersiz olduğunda savunur, bol olduğunda saldırır.',
49
'Kararın kalitesi, bir şahinin kurbanını vurup yok etmesini sağlayan iyi zamanlanmış saldırısı gibidir.',
50
'Düşman rahatken onu yorun; iyi beslendiğinde aç bırakın; hareketsizken onu hareket ettirin. Acele etmesi gereken yerlerde görünün, sizi beklemediği yerde hızla hareket edin.' ,
51
'Düşmanını ve kendini biliyorsan, yüz savaşın sonuçlarından korkmana gerek yok. Kendini biliyorsan ama düşmanı bilmiyorsan, kazandığın her zafer için de bir yenilgiye uğrayacaksın. Ne düşmanı ne de kendini tanıyorsan, kaybedersin. Her savaşta yenik.',
52
'Şöhrete imrenmeden ilerleyen, rezil olmaktan korkmadan geri çekilen, tek düşüncesi ülkesini korumak ve hükümdarına iyi hizmet etmek olan general, krallığın mücevheridir.',
53
'Çünkü yüz muharebede yüz zafer kazanmak hünerin zirvesi değildir. Düşmanı savaşmadan boyun eğdirmek hünerin zirvesidir.',
54
'Eskilerin akıllı dövüşçü dediği şey, sadece kazanmakla kalmayıp, kolaylıkla kazanmayı da başaran kişidir.',
55
'Çevrelenmiş bir düşmana bir kaçış yolu bırakmalısın.',
56
'Düşmanını tanımak için Düşmanın olmalısın.',
57
'Dolayısıyla, savaşta en büyük önem, düşmanın stratejisine saldırmaktır.',
58
'Bir lider, zorla değil, örnek alarak yönetir.',
59
'Çok sık ödüller, generalin kaynaklarının sonuna geldiğini gösterir; çok sık cezalar, şiddetli sıkıntı içinde olduğunu gösterir.',
60
'Aşağılık rolü yapın ve kibirini teşvik edin.',
61
'Bütün insanlar, benim fethettiğim bu taktikleri görebilir, ama kimsenin göremediği şey, zaferin içinden çıktığı stratejidir.',
62
'Savaşmak istemiyorsak, kampımızın hatları sadece yerde görülse bile düşmanın bize saldırmasını engelleyebiliriz. Tek yapmamız gereken, yoluna tuhaf ve anlaşılmaz bir şey atmak.',
63
'Askeri harekat aldatma içerir. Yetkin olsanız bile beceriksiz görünün. Etkili olsanız da etkisiz görünün.',
64
'Muzaffer savaşçılar önce kazanır sonra savaşa girer, mağlup savaşçılar önce savaşa girer sonra kazanmaya çalışır.',
65
'En iyi zafer, gerçek düşmanlıklar olmadan rakibin kendi isteğiyle teslim olduğu zamandır... Savaşmadan kazanmak en iyisidir.',
66
'Fırsatlar ele geçirildikçe çoğalır.',
67
'Savaşın özü hızdır. Düşmanın hazırlıksızlığından yararlanın, beklenmedik yollardan gidin ve önlem almadığı yerden vurun.',
68
'Rakibiniz choleric mizacına sahipse, onu sinirlendirmeye çalışın.',
69
'Birçoğunun yönetimi, azınlığın yönetimiyle aynıdır. Bu bir organizasyon meselesidir.',
70
'Eskinin iyi savaşçıları önce kendilerini yenilgi olasılığının ötesine geçirdiler ve sonra düşmanı yenmek için bir fırsat beklediler.',
71
'Rakibine geri çekilmek için altın bir köprü inşa et.',
72
'Rüzgar kadar hızlı. Orman kadar sessiz. Ateş gibi fethedin. Dağ gibi sabit.',
73
'Size karşı casusluk yapmak ve size hizmet etmeleri için onlara rüşvet vermek için gelen düşman ajanlarını bulmak esastır. Onlara talimat verin ve onlarla ilgilenin. Böylece iki katına çıkmış ajanlar işe alınır ve kullanılır.',
74
'Şimdi, aydın prens ve bilge generalin her hareket ettiklerinde düşmanı yenmesinin ve başarılarının sıradan insanlarınkini aşmasının nedeni önceden bilgidir.',
75
'Ve bu nedenle, savaşta usta olanlar, düşmanı savaş alanına getirir ve oraya onun tarafından getirilmez.',
76
'Uzun süreli savaştan yararlanan bir ulus örneği yoktur.',
77
'Saldırabilecek durumdayken güçsüz görünmeliyiz; güçlerimizi kullanırken hareketsiz görünmeliyiz; yakındayken düşmanı uzakta olduğumuza inandırmalıyız; uzaktayken onu yakın olduğumuza inandırmalıyız. ',
78
'Sağanak su kayaları savurduğunda, bunun nedeni momentumudur. Bir şahinin çarpması avının vücudunu kırdığında, bunun nedeni odur.
]
        embedVar = discord.Embed(title="Savaş Sanatı",color = discord.Colour.dark_theme())
        embedVar.add_field(name = "Alıntı" , value = "{0}".format(random.choice(a)))
        await ctx.channel.send(embed = embedVar)
        return
    
    @suntzu.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send(":x: "+str(error))
        return


def setup(client):
    client.add_cog(Ping(client))
