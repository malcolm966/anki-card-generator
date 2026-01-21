from db_util import insert_grammar

title = '～によって／によっては／により／による'
usage = '名詞＋によって／によっては／により／による'
level = 'N3'

meaning = '【根拠】の用法（根据…／依据…／通过…）'
explanation = '「～をもとにして」「～に基づいて」などに言い換えることができます。'
sentences = '''
（１）　その日の気分によって着ていく服を選ぶ。　▶
　　　　　根据当天的心情选择穿什么衣服。
　　　　　Based on the mood of the day, choose what clothes to wear.
（２）　声は体調の良し悪しによっても左右されます。　▶
　　　　　声音会受到身体状况的影响。
　　　　　The voice can be affected by the physical condition.
（３）　旅行のスケジュールは天候によって変更されることがあります。　▶
　　　　　旅行的日程可能会受天气变化而调整。
　　　　　The travel schedule may be adjusted based on weather changes.
'''
insert_grammar(title=title, usage= usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)
meaning = '【手段】の用法（通过…／凭借…／靠…）'
explanation = '''
手段を表す格助詞「で」に置き換えることができます。ただし、日常生活で使うようなものに対しては「～よって」を使うことはできません。そのような場合は「で」を使います。
（例）◯電車で会社に行く。
　　　　✕電車によって会社に行く。
'''
sentences = '''
（13）　インターネットによって世界中のニュースを知ることができるようになった。　▶
　　　　　互联网使我们能够获取世界各地的新闻。
　　　　　The Internet enables us to access news from around the world.
（14）　職場環境を改善することによって従業員の満足度を高める。　▶
　　　　　改善工作环境可以提高员工的满意度。
　　　　　Improving the work environment can increase employee satisfaction.
（15）　研究によって新しい治療法が開発されました。　▶
　　　　　研究开发出了新的治疗方法。
　　　　　Research has developed new treatment methods.
'''
insert_grammar(title=title, usage= usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '【原因】の用法（因为…而…／由于…原因）'
explanation = '''
　前件で客観的な原因を述べ、後件ではその原因によって発生した何らかの出来事を述べます。書き言葉的です。
　「～が原因で」に置き換えられます。
'''
sentences = '''
（23）　強風によって窓が割れた。　▶
　　　　　窗户被强风打破了。
　　　　　The window was broken by strong winds.
（24）　新商品の評判は顧客の口コミによって広がりました。　▶
　　　　　新产品的声誉因客户口碑而传播开来。
　　　　　The reputation of the new product spread through word of mouth from customers.
'''
insert_grammar(title=title, usage= usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '【受身文に対応する能動文の動作主】の用法（被…／由…）'
explanation = '''
　受身文に対応する能動文の動作主を表します。歴史上の事実や規定事実を客観的に伝えるときによく用います。
　構文としては「Ａが Ｂによって ～られる」です。これは「Ｂが Ａを ～する」に言い換えられます。
'''
sentences = '''
（34）　金閣寺は足利義満によって建てられた。　▶
　　　　　金阁寺是由足利义满建造的。
　　　　　The Golden Pavilion was built by Ashikaga Yoshimitsu.
（35）　壁が何者かによって壊された。　▶
　　　　　墙壁被某人破坏了。
　　　　　The wall was damaged by someone.
'''
insert_grammar(title=title, usage= usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '異なる状況で異なる結果】の用法（因…／根据…（而不同））'
explanation = '''
　状況が異なると結果も異なることを表します。多くの場合、後件には「違う」「異なる」などが呼応します。「～によっては」は基本、この用法の時にだけ使います。
'''
sentences = '''
（44）　人によって考え方は違う。　▶
　　　　　每个人的思考方式因人而异。
　　　　　People have different ways of thinking.
（45）　人によって態度を変えるのは良くない。　▶
　　　　　因人而异地改变态度并不好。
　　　　　It is not good to change one’s attitude depending on the person.
'''
insert_grammar(title=title, usage= usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)
meaning = '【動作の主体】の用法'

explanation = '''
　「名詞Ａ＋による＋動作性名詞Ｂ」などの形をとり、動作性名詞Ｂの動作を行う主体が名詞Ａであることを表します。
'''
sentences = '''
（54）　校長先生による特別講義が行われた。　▶
　　　　　校长进行了特别讲座。
　　　　　A special lecture was conducted by the principal.
（55）　Ａ国は空軍によるＢ国へのミサイル攻撃を否定している。　▶
　　　　　A国否认对B国进行空军导弹攻击。
　　　　　Country A denies a missile attack on Country B by its air force.
（56）　私は今、上司によるパワハラに苦しんでいる。　▶
　　　　　我目前正在遭受上司的权力骚扰。
　　　　　I am currently suffering from harassment by my boss.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

title = '～てくる'
usage = '動て形＋くる'
level = 'N4'

meaning = '移動時の状態（…着来）'
explanation = '''
移動に関する動詞に接続して、どのような動作で、どのような手段で移動が行われたかを表します。
'''
sentences = '''
（１）　家まで走ってくる。　▶
　　　　　跑到家里来。
　　　　　I’ll run home.
（２）　天気が悪いからタクシーに乗ってきた。　▶
　　　　　因为天气不好，所以坐了出租车回来。
　　　　　Since the weather is bad, I came by taxi.
（３）　タイヤがパンクしたので、自転車を引っ張ってきた。　▶
　　　　　因为轮胎爆胎了，所以把自行车拉过来了。
　　　　　The tire was flat, so I pulled the bicycle.
（４）　階段でゆっくり下りてきた。　▶
　　　　　我慢慢地从楼梯上下来了。
　　　　　I came down the stairs slowly.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '順次的動作（…来）'
explanation = '''
　順次的動作の用法の時、「～てくる」は文字通り「～てから来る」という意味です。
（５）ではまず予約をしに行って、そして戻る（来る）という物事の順序を表します。
　必ず意志動詞に接続して、その動作が完全に終わった後に「来る」が行われます。
'''
sentences = '''
（５）　予約をしてきますので、ここで待っていてください。　▶
　　　　　我去预约一下，请在这里等着。
　　　　　I’ll make a reservation, so please wait here.
（６）　友達に家に遊びにいってきます。　▶
　　　　　我去朋友家玩。
　　　　　I’m going to a friend’s house to play.
（７）　途中偶然友人に会って話してきたから遅くなった。　▶
　　　　　路上偶然遇见朋友聊天，所以迟到了。
　　　　　I met a friend by chance on the way and talked, so I became late.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)


meaning = '動作の継続（過去から現在まで）（一直…下来）'
explanation = '''
　意志動詞に接続して、その動作が過去のある時点から現在まで持続していることを表します。
必ず過去形「～てきた」の形をとります。
'''
sentences = '''
（８）　ずっと努力してきたのに、なかなか結果が出ない。　▶
　　　　　我一直努力着，却怎么也没有结果。
　　　　　I’ve been working hard for a long time, but the results haven’t come easily.
（９）　何百年も前から続いてきたこの伝統を、これからも守っていく。　▶
　　　　　从几百年前延续下来的这个传统，今后也将传承下去。
　　　　　I will continue to uphold this tradition that has been going on for hundreds of years.
（10）　大学を卒業して以来、ずっとここで仕事をしてきました。　▶
　　　　　我从大学毕业以来一直在这里工作。
　　　　　Since graduating from university, I have been working here all along.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '少しずつ近づく（…来）'
explanation = '''
　対象が話し手へと徐々に近づくことを表します。
（11）は物理的な距離のみならず、精神的な距離としても解釈できます。
'''
sentences = '''
（11）　二人の距離は近づいてきた。　▶
　　　　　两人的距离越来越近了。
　　　　　The distance between the two has become closer.
（12）　ご主人様が戻ってこられました。　▶
　　　　　主人回来了。
　　　　　The master has returned.
（13）　うちの子はお腹がすくとすぐ帰ってくる。　▶
　　　　　我家孩子一饿就会回来。
　　　　　My child comes back home quickly when hungry.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '状態変化の開始（…起来／…了）'
explanation = '''
　無意志動詞に接続して、変化が開始したことを表します。
　どんどん、だんだんなどの副詞と呼応して用いられることが多いです。
'''
sentences = '''
（14）　高齢者人口はどんどん増えてきている。　▶
　　　　　老年人口不断增加。
　　　　　The elderly population has been steadily increasing.
（15）　ここ数日の大雪で雪が積もってきた。　▶
　　　　　这几天由于下了大雪，积了一层雪。
　　　　　The recent heavy snowfall has caused the snow to accumulate.
（16）　最近暑くなってきた。　▶
　　　　　最近热起来了。
　　　　　It has become hotter recently.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)


meaning = '出現（…出来）'
explanation = '''
　無意志動詞に接続して、元々存在していなかった、あるいは話し手が見えていなかったものが見えるようになることを表します。
　どんどん、だんだんなどの副詞と呼応して用いられることが多いです。
'''
sentences = '''
（17）　太陽が地平線から昇ってきた。　▶
　　　　　太阳从地平线上升来了。
　　　　　The sun has risen from the horizon.
（18）　歯が生えてきた。　▶
　　　　　长牙了。
　　　　　Teeth have started to come in.
（19）　新年度になり新しい学生がやってきた。　▶
　　　　　到了新年度，来了新学生。
　　　　　A new academic year has started, and new students have arrived.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = 'こちらへの一方的な動作（…来／…过来）'
explanation = '''
話し手、あるいは話し手が見ている人に対して一方的な動作が行われることを表します。
'''
sentences = '''
（20）　知らない人が話しかけてきた。　▶
　　　　　一个陌生人向我搭话。
　　　　　Someone I don’t know started talking to me.
（21）　猫が噛み付いてきた。　▶
　　　　　猫咬了我。
　　　　　The cat bit me.
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)


title = '～ていく'
usage = '動て形＋いく'
level = 'N4'


meaning = '移動時の状態（…着去／…去）'
sentences = '''
（１）　教室まで歩いていく。　▶
　　　　　走到教室去。
　　　　　I’ll walk to the classroom.
（２）　天気が悪いからバスに乗っていきましょう。　▶
　　　　　天气不好，坐公共汽车去吧。
　　　　　Since the weather is bad, let’s take the bus.
（３）　タイヤがパンクしたので、自転車を引っ張っていった。　▶
　　　　　因为轮胎爆胎了，所以我拉着自行车走。
　　　　　The tire was flat, so I pulled the bicycle.
（４）　川をカヌーでゆっくり下っていく。　▶
　　　　　乘独木舟在河上慢慢地往下走。
　　　　　Slowly go down the river in a canoe.
'''
explanation = '''
　移動に関する動詞に接続して、どのような動作で、どのような手段で移動が行われたかを表します
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)


meaning = '順次的動作（…了再去）'
sentences = '''
（５）　先にこの仕事をすませていきます。　▶
　　　　　我先把这项工作做完。
　　　　　I’ll finish this work first.
（６）　遠慮せずに泊まっていってください。　▶
　　　　　请不要客气，住在这里吧。
　　　　　Please feel free to stay overnight.
（７）　とりあえずここで休憩していこう。　▶
　　　　　总之先在这里休息吧。
　　　　　Let’s take a break here for now.
'''
explanation = '''
　順次的動作の用法の時、「～ていく」は文字通り「～てから行く」という意味です。
（26）ではまず仕事を終わらせて、そして行くという物事の順序を表します。
　必ず意志動詞に接続して、その動作が完全に終わった後に「行く」が行われます。
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '動作の継続（未来へ）（…下去）'
sentences = '''
（８）　以後も変わらず努力していく。　▶
　　　　　以后也要一如既往地努力下去。
　　　　　I will continue to make efforts unchanged.
（９）　就職しても趣味のマラソンは続けていくつもりだ。　▶
　　　　　即使工作了，作为兴趣爱好的马拉松也打算继续下去。
　　　　　Even after getting a job, I plan to continue my hobby of marathon running.
（10）　これからもここで生きていく。　▶
　　　　　今后也要在这里生活。
　　　　　I will continue to live here from now on.
'''
explanation = '''
意志動詞に接続して、その動作がその後も将来にかけて継続することを表します。
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '少しずつ遠ざかる（逐渐远去）'
sentences ='''
（11）　心はどんどん離れていった。　▶
　　　　　心渐渐离开了。
　　　　　My heart gradually drifted away.
（12）　アリは自らの巣に戻っていきました。　▶
　　　　　蚂蚁回到了自己的窝里。
　　　　　The ants returned to their nest.
（13）　授業が終わると学生はすぐに帰っていきました。　▶
　　　　　下课后学生马上回去了。
　　　　　When the class ended, the students immediately went home.
'''
explanation = '''
　対象が話し手から徐々に離れることを表します。
　物理的な距離のみならず、（32）のように精神的な距離でも使うことができます。
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)


meaning = '状態変化の進展（…下去）'
sentences = '''
（14）　高齢者人口は今後もどんどん増えていく。　▶
　　　　　高龄人口今后也会不断增加。
　　　　　The elderly population will continue to increase.
（15）　雪が積もっていく。　▶
　　　　　雪渐渐积起来。
　　　　　The snow is piling up.
（16）　これからますます寒くなっていくだろう。　▶
　　　　　今后会越来越冷吧。
　　　　　It will get colder and colder from now on.
'''
explanation = '''
　無意志動詞に接続して、変化が進行していることを表します。
　どんどん、だんだんなどの副詞と呼応して用いられることが多いです。
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)

meaning = '消失（消失不见）'
sentences = '''
（17）　太陽が地平線に沈んでいった。　▶
　　　　　太阳落在地平线上。
　　　　　The sun sank below the horizon.
（18）　覚えたそばから忘れていく。　▶
　　　　　刚记住就忘了。
　　　　　Forget as soon as you learn.
（19）　学生が卒業していくのは寂しくてたまらない。　▶
　　　　　学生毕业后寂寞得不得了。
　　　　　It’s lonely and unbearable when students graduate.
'''
explanation = '''
　無意志動詞に接続して、元々存在していた物事が話し手の視界から消えることを表します。
　最後は完全に消えて見えなくなります。
　どんどん、だんだんなどの副詞と呼応して用いられることが多いです。
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)


meaning = 'こちらからの一方的な動作（…去／…过去）'
sentences = '''
（20）　道行く人に次から次へと声をかけていく。　▶
　　　　　一个接一个地向路人打招呼。
　　　　　I’ll talk to passing people one after another.
（21）　手当たり次第に聞いていこう。　▶
　　　　　随便问问吧。
　　　　　Let’s ask around haphazardly.
'''
explanation = '''
話し手から、あるいは話し手が見ている人から他の対象に対して一方的な動作が行われることを表します。
'''
insert_grammar(title=title, usage = usage, meaning=meaning, explanation=explanation, sentences= sentences, level= level)