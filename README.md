# netverk5

hérna er server og client sem við náðum í frá http://net-informations.com/python/net/thread.htm 

Aðal munurinn á milli venjulegan socket server og multithread server er að socket serverinn getur bara tekið við einum client í einu þar sem hann í rauninni hefur bara einn thread, en thread er hægt að lýsa sem cursor forritsins það er þar sem forritið er að keyra kóða svo ef þú hefur bara einn thread þá þarftu að klára að keyra/lesa allan kóðan áður en þú getur byrjað aftur en með multithread geturðu keyrt sama kóðan á mörgum stöðum í einu og þannig tekið við mun fleiri fyrirspurnum um upplýsingar ef þú ert server þar sem þú getur gefið hverri tengingu við serverinn með sínum eigin thread svo að engin er fyrir hvor öðrum.

Auðvitað er nú samt ekki til neinn server með endalausa threads svo það er enn þá hægt að nota DDoS árásir eins lengi og nógu mikið af bots eru að gera áras og taka burtu thread frá alvöru kúnna en það má taka fram að það lýtur út fyrir að þannig árásir séu að deyja út bráðum ef miða á við að github nýlega lifði af stærstu DDoS áras sem hefur nokkrun tíma verið framinn og enginn server hjá þeim dó en árásinn á sínum hæsta punkti var að senda 1.35 terabits á sekúndu á github en sú áras notaði ekki bots heldur lítill óvarinn tæki sem finnast allstaðar eins og úr, ískápar og fleiri nýjunga húsgögn sem þurfa víst öll að hafa net samband af einhverri ástæðu en það er mjög létt að finna þau tæki og skipa þeim um að senda beiðnir hingað og þangað og þegar þeim beiðnum er svarað að þá senda sömu gögn til baka á server en bara eftir að hafa margfaldað gögnin til að taka upp eins mikinn tíma og mögulegt er.
