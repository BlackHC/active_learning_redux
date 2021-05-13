store = {}
store['timestamp']=1620257755
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=2']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=40
store['config']={'seed': 2, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.334061861038208})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.2475953102111816})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.512305498123169})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.901860475540161})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.6361658573150635})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.701, 'crossentropy': 2.23410625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 54725], ['id', 5910], ['id', 10831], ['id', 34535], ['id', 51137], ['id', 10227], ['id', 37175], ['id', 10419], ['id', 52092], ['id', 57040], ['id', 34455], ['id', 28247], ['id', 47562], ['id', 55099], ['id', 56286], ['id', 28919], ['id', 32777], ['id', 59423], ['id', 44690], ['id', 6562]], 'labels': [8, 6, 5, 6, 5, 5, 6, 6, 7, 3, 8, 8, 6, 5, 8, 4, 9, 8, 6, 6], 'scores': [1.0185446739196777, 0.9475427269935608, 1.0134586691856384, 0.891099750995636, 1.1573405861854553, 1.1316472887992859, 0.8009214997291565, 1.0064986944198608, 0.9580684304237366, 0.8170873522758484, 0.9756913185119629, 0.9027166962623596, 0.9339810609817505, 1.056686520576477, 0.8826239705085754, 0.8318593502044678, 1.1162676811218262, 0.9899593591690063, 0.8962703347206116, 0.8817187547683716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7490237951278687})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9886653423309326})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.0447824001312256})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.1595442295074463})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7599, 'crossentropy': 1.4332369140625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 59333], ['id', 28720], ['id', 47947], ['ood', 25632], ['id', 8877], ['id', 8749], ['id', 39938], ['id', 35236], ['id', 45887], ['id', 3762], ['id', 29453], ['id', 19816], ['id', 55941], ['id', 48292], ['id', 31924], ['id', 36427], ['id', 54471], ['id', 7400], ['id', 26574], ['ood', 58131]], 'labels': [2, 5, 1, 7, 0, 2, 8, 1, 6, 8, 2, 1, 3, 2, 6, 3, 8, 8, 5, 7], 'scores': [0.8937410712242126, 0.775850236415863, 0.6868306398391724, 0.4306620955467224, 0.9353979825973511, 0.9974714517593384, 0.7040597200393677, 0.8719136714935303, 0.9641543030738831, 0.877662718296051, 1.0362945199012756, 0.7399702072143555, 0.8148736953735352, 0.9789182543754578, 0.9815064668655396, 0.8708519339561462, 0.6148338317871094, 0.6011676788330078, 0.7115587592124939, 0.41908085346221924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0244548320770264})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0645431280136108})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1454224586486816})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3031859397888184})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.8205, 'crossentropy': 0.974895703125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 26038], ['id', 33674], ['id', 59433], ['id', 57843], ['id', 6884], ['id', 48598], ['id', 49650], ['id', 53139], ['id', 54118], ['id', 29418], ['id', 216], ['id', 22219], ['id', 19590], ['id', 11536], ['id', 15359], ['id', 12707], ['id', 21009], ['id', 37484], ['id', 40646], ['id', 627]], 'labels': [0, 5, 0, 0, 5, 2, 3, 2, 7, 4, 0, 3, 5, 9, 4, 2, 2, 2, 8, 8], 'scores': [0.6700744032859802, 0.7053918838500977, 0.7818589210510254, 0.7083374261856079, 0.566091775894165, 0.7360433340072632, 0.8337997794151306, 0.6776230335235596, 0.48337674140930176, 0.5231949090957642, 0.5868778228759766, 0.7004536390304565, 0.6321907043457031, 0.5123816132545471, 0.377399206161499, 0.6755839586257935, 0.8474410772323608, 0.7661921977996826, 0.592828631401062, 0.5136703252792358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0894593000411987})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9599710702896118})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1083201169967651})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1457479000091553})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2610232830047607})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8277, 'crossentropy': 0.8878220703125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 42086], ['id', 27131], ['id', 22280], ['id', 27834], ['id', 14888], ['id', 49160], ['id', 36515], ['id', 5106], ['id', 46546], ['id', 13155], ['id', 35449], ['id', 46364], ['id', 2034], ['id', 27171], ['id', 43964], ['id', 51241], ['id', 57003], ['id', 9279], ['id', 35395], ['id', 31146]], 'labels': [9, 2, 2, 2, 9, 2, 3, 9, 2, 0, 0, 2, 4, 2, 2, 2, 0, 3, 1, 2], 'scores': [0.6089140176773071, 0.6542467474937439, 0.6694550514221191, 0.7773259282112122, 0.5280618667602539, 0.8554037809371948, 0.5056920945644379, 0.6490912437438965, 0.6192523241043091, 0.5411397218704224, 0.5868351757526398, 0.5682239532470703, 0.7937088012695312, 0.7110460996627808, 0.6762003302574158, 0.5122767090797424, 0.8246705830097198, 0.4345250129699707, 0.28766965866088867, 0.7823858857154846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0280518531799316})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.890477180480957})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7967555522918701})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9085463285446167})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0113147497177124})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.096811294555664})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.669194091796875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 19942], ['id', 14506], ['id', 1374], ['id', 36067], ['id', 32301], ['id', 4955], ['ood', 29661], ['id', 41239], ['id', 53116], ['id', 1514], ['id', 45069], ['id', 22964], ['id', 2000], ['id', 20335], ['id', 28802], ['id', 22139], ['id', 34925], ['id', 41721], ['id', 48271], ['id', 685]], 'labels': [5, 7, 2, 6, 4, 2, 3, 9, 0, 5, 4, 3, 5, 7, 8, 2, 7, 2, 7, 8], 'scores': [0.9386870265007019, 0.5437368750572205, 0.6316858530044556, 0.7732805013656616, 0.8292043805122375, 0.8559761047363281, 0.5236529111862183, 0.8809572458267212, 0.7658592462539673, 0.5407398045063019, 0.7070775032043457, 0.8362573981285095, 0.9646430015563965, 0.8076622486114502, 0.725670576095581, 1.007355511188507, 0.8043673038482666, 0.5667339563369751, 0.7527897953987122, 0.7394466400146484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8424558043479919})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6092383861541748})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7130844593048096})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.703751802444458})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7196425199508667})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.555526953125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 42437], ['id', 10932], ['id', 54880], ['id', 20820], ['id', 53956], ['id', 50082], ['id', 31593], ['id', 26405], ['id', 3304], ['id', 57642], ['id', 49213], ['id', 53083], ['id', 56372], ['id', 42454], ['id', 48900], ['id', 4767], ['id', 37214], ['id', 9308], ['id', 21728], ['id', 37257]], 'labels': [9, 7, 5, 9, 7, 6, 9, 9, 2, 0, 9, 3, 2, 2, 1, 8, 2, 9, 6, 4], 'scores': [0.6411548852920532, 0.5647545456886292, 0.8264697194099426, 0.7812331914901733, 0.39838194847106934, 0.8174833059310913, 0.7224263548851013, 0.7892557382583618, 0.572327733039856, 0.8197352886199951, 0.564038097858429, 0.48002946376800537, 0.6413929462432861, 0.44649219512939453, 0.6429821252822876, 0.7915093898773193, 0.8100603818893433, 0.4315258264541626, 0.7421343326568604, 0.5327827334403992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9647899866104126})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6601029634475708})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7542774677276611})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7378630638122559})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.881241500377655})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8968, 'crossentropy': 0.590411572265625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 40046], ['id', 46368], ['id', 4679], ['id', 27264], ['id', 32490], ['id', 50976], ['id', 37013], ['id', 33200], ['id', 17333], ['id', 44544], ['id', 31148], ['id', 12190], ['id', 59657], ['id', 19855], ['id', 46853], ['id', 37256], ['id', 21395], ['id', 46603], ['id', 1539], ['id', 22673]], 'labels': [7, 8, 2, 2, 3, 3, 3, 5, 3, 4, 2, 8, 4, 3, 3, 6, 8, 0, 2, 2], 'scores': [0.6566472053527832, 0.6661657094955444, 0.4274422526359558, 0.5763006806373596, 0.8361663222312927, 0.5195813179016113, 0.7311158776283264, 0.5316908955574036, 0.37438422441482544, 0.5300968289375305, 0.6859201192855835, 0.5299533605575562, 0.6707199811935425, 0.7812615931034088, 0.6292608380317688, 0.8936997056007385, 0.837429404258728, 0.48004746437072754, 0.6933782696723938, 0.7054152488708496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7585281133651733})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6103478670120239})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5118793845176697})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4929322600364685})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5370133519172668})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5393297076225281})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5410970449447632})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.449151611328125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 26389], ['id', 52332], ['id', 47060], ['id', 49290], ['id', 5170], ['id', 13878], ['id', 21112], ['id', 6170], ['id', 29662], ['id', 56412], ['id', 32835], ['id', 30702], ['id', 11711], ['id', 43818], ['id', 886], ['id', 42415], ['id', 2272], ['id', 32445], ['id', 1964], ['id', 53165]], 'labels': [0, 5, 5, 8, 8, 4, 3, 3, 2, 8, 7, 4, 2, 2, 5, 7, 5, 5, 8, 3], 'scores': [0.6448777914047241, 0.8660839200019836, 0.7795587778091431, 0.57716965675354, 0.8093968629837036, 0.7987402081489563, 0.48581933975219727, 0.9022231698036194, 0.6797775328159332, 0.6253153085708618, 0.6963026523590088, 0.31887853145599365, 0.6828957796096802, 0.7532670199871063, 0.9385992884635925, 0.7938677668571472, 0.7200958728790283, 0.9028269648551941, 0.566977858543396, 0.6298526525497437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.82651686668396})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5864274501800537})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.47696030139923096})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47698765993118286})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45832622051239014})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5015943646430969})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4376334547996521})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5158947706222534})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4492518901824951})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45252588391304016})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.427888623046875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 12898], ['id', 46300], ['id', 41371], ['id', 57154], ['id', 22565], ['id', 50091], ['id', 46941], ['id', 24261], ['id', 51158], ['id', 52708], ['id', 58748], ['id', 40208], ['ood', 40945], ['ood', 15237], ['id', 9158], ['id', 45024], ['id', 8773], ['id', 49493], ['id', 15662], ['id', 28389]], 'labels': [5, 5, 0, 0, 5, 5, 5, 8, 8, 4, 8, 0, 8, 2, 0, 5, 3, 8, 0, 2], 'scores': [0.7746413052082062, 1.0772620141506195, 0.7829649448394775, 0.7575657963752747, 0.9085206389427185, 0.7180587649345398, 0.6642402410507202, 0.6984034180641174, 0.8532027304172516, 0.9406717419624329, 0.7101176977157593, 0.7970708310604095, 0.5195657014846802, 0.480160117149353, 0.7036828994750977, 0.8603673279285431, 0.8434709310531616, 0.8304657340049744, 0.5246720910072327, 0.7601669430732727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9959170818328857})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5272647142410278})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4738836884498596})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4330234229564667})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4927295446395874})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47225865721702576})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45823580026626587})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.429514892578125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 17603], ['ood', 37470], ['id', 48492], ['id', 14765], ['id', 17896], ['id', 14667], ['id', 43417], ['id', 17542], ['id', 30080], ['id', 15190], ['id', 40952], ['ood', 43806], ['id', 31094], ['id', 8464], ['id', 47642], ['id', 27514], ['id', 20169], ['id', 25386], ['id', 4124], ['id', 42828]], 'labels': [0, 3, 6, 3, 4, 9, 3, 6, 0, 6, 6, 7, 9, 1, 1, 4, 4, 0, 9, 7], 'scores': [0.9225966930389404, 0.48894989490509033, 0.6889969110488892, 0.7311833500862122, 0.638287365436554, 0.7704886794090271, 0.7529295682907104, 0.7894015908241272, 0.7917240262031555, 0.7461259961128235, 0.602125883102417, 0.5712674856185913, 0.619243323802948, 0.7910246253013611, 0.7058555781841278, 0.7415039539337158, 0.8440159559249878, 0.9038739800453186, 0.6952416300773621, 0.8330458998680115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9777140617370605})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4904107451438904})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4292086362838745})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40367579460144043})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.44246816635131836})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37874549627304077})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4116429090499878})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43191540241241455})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4012283682823181})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.3408045166015625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 51094], ['id', 50258], ['id', 45615], ['ood', 55043], ['id', 58138], ['id', 23350], ['id', 26613], ['id', 7832], ['id', 32499], ['ood', 35984], ['id', 14070], ['id', 18398], ['id', 52928], ['id', 10446], ['id', 49499], ['id', 25946], ['id', 31650], ['id', 50224], ['id', 6197], ['ood', 26104]], 'labels': [8, 8, 7, 5, 8, 8, 2, 3, 4, 5, 1, 4, 0, 8, 1, 9, 5, 7, 1, 5], 'scores': [0.7057210803031921, 0.478921115398407, 0.6359787285327911, 0.5814259052276611, 0.7244828343391418, 0.8830594420433044, 0.9188929796218872, 0.5534311532974243, 0.7202355861663818, 0.6067034006118774, 0.7844592332839966, 0.7708569169044495, 0.6632832288742065, 0.8137685656547546, 0.6990942358970642, 0.8428822755813599, 0.931576132774353, 0.6175596714019775, 0.4100067615509033, 0.4550483226776123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9588998556137085})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5326966047286987})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4159066677093506})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3907933235168457})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4039812684059143})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3810669183731079})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42704248428344727})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4445330500602722})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.426555335521698})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9551, 'crossentropy': 0.3305177978515625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 8771], ['id', 19886], ['id', 8717], ['id', 14635], ['id', 33222], ['id', 10756], ['id', 28374], ['id', 59574], ['id', 20756], ['id', 29153], ['id', 32747], ['id', 24512], ['id', 16250], ['id', 23575], ['id', 17540], ['id', 529], ['id', 32573], ['id', 20170], ['id', 26516], ['id', 57882]], 'labels': [3, 2, 7, 3, 5, 3, 3, 5, 3, 3, 8, 3, 9, 9, 1, 9, 8, 9, 6, 0], 'scores': [0.8308883309364319, 0.631304919719696, 0.4623667299747467, 0.9125918745994568, 0.6672996282577515, 0.7395650744438171, 0.6150076985359192, 0.7852127552032471, 0.7775692939758301, 0.8930642604827881, 0.9298175573348999, 0.577000617980957, 0.49061471223831177, 0.4642544686794281, 0.7858823537826538, 0.5412470698356628, 0.656664252281189, 0.6629100441932678, 0.6747047305107117, 0.9196332693099976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0138417482376099})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5727413892745972})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4815007150173187})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43410295248031616})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.410519003868103})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37352699041366577})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40044867992401123})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40492963790893555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3662233352661133})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3974543809890747})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39004960656166077})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3814316987991333})
store['active_learning_steps'][12]['training']['best_epoch']=9
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9553, 'crossentropy': 0.363434130859375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 27176], ['id', 7784], ['id', 42715], ['id', 13655], ['id', 34908], ['id', 14580], ['id', 16196], ['id', 1598], ['id', 42181], ['id', 52892], ['id', 23406], ['id', 30720], ['id', 28182], ['id', 38698], ['id', 41538], ['id', 42199], ['id', 34930], ['id', 11767], ['id', 39031], ['id', 25803]], 'labels': [5, 3, 9, 8, 5, 9, 2, 8, 4, 8, 4, 3, 8, 5, 6, 3, 9, 4, 2, 0], 'scores': [0.6077542304992676, 0.8979684114456177, 0.8222559690475464, 0.6423451900482178, 0.6935595870018005, 0.6423588991165161, 0.5747230648994446, 0.7480579018592834, 0.48075416684150696, 0.8189539015293121, 0.8123291730880737, 0.8542613983154297, 0.8943710327148438, 1.0147139430046082, 0.6817483007907867, 0.9359095096588135, 0.8720824718475342, 0.7643216252326965, 0.9920886158943176, 0.7565885782241821]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1158759593963623})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5300540924072266})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4481412172317505})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38377776741981506})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37468987703323364})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3781907558441162})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3828662633895874})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39356231689453125})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9565, 'crossentropy': 0.347992529296875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 26918], ['id', 34845], ['id', 55743], ['id', 28368], ['id', 31883], ['id', 51294], ['id', 14689], ['id', 23100], ['id', 30177], ['id', 30085], ['id', 19868], ['id', 53852], ['id', 8847], ['id', 32738], ['id', 13376], ['id', 47962], ['id', 57195], ['id', 30107], ['id', 6418], ['id', 17739]], 'labels': [5, 3, 3, 9, 4, 7, 5, 9, 7, 9, 5, 7, 9, 7, 3, 6, 3, 2, 5, 5], 'scores': [0.7382714748382568, 0.60405033826828, 0.6434768438339233, 0.8049463033676147, 0.8953297734260559, 0.6677105724811554, 0.8140742778778076, 0.7641568183898926, 0.7785218358039856, 0.6191220283508301, 0.8706485033035278, 0.6054703593254089, 0.8265426158905029, 0.8409950733184814, 0.7698186635971069, 0.6099832057952881, 0.41001707315444946, 0.648987889289856, 0.8484252691268921, 0.7187530398368835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0467147827148438})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5493316650390625})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4384930729866028})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3692842423915863})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38519302010536194})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4320914149284363})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3801710307598114})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9468, 'crossentropy': 0.3713091796875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 50730], ['id', 32002], ['id', 27729], ['id', 54316], ['id', 28587], ['id', 24630], ['id', 27780], ['id', 40034], ['id', 41426], ['id', 854], ['id', 47560], ['id', 5842], ['id', 15935], ['id', 54954], ['id', 14896], ['id', 29759], ['id', 1674], ['id', 38526], ['id', 31339], ['id', 34552]], 'labels': [7, 6, 8, 6, 8, 5, 9, 6, 4, 2, 7, 1, 8, 8, 8, 5, 9, 1, 6, 3], 'scores': [0.47008365392684937, 0.5051496624946594, 0.4044620990753174, 0.5685331225395203, 0.6464390158653259, 0.6010673642158508, 0.4711681604385376, 0.48990583419799805, 0.6987853646278381, 0.6932163238525391, 0.5951236188411713, 0.8577184081077576, 0.483898401260376, 0.5002343654632568, 0.7635867595672607, 0.5753625631332397, 0.896155059337616, 0.5247454047203064, 0.6356528997421265, 0.6355030536651611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1190319061279297})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.591627836227417})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4454408288002014})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37641167640686035})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34744149446487427})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3684256970882416})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3463507294654846})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34152501821517944})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3565422594547272})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3389217257499695})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34894102811813354})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32474249601364136})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34198856353759766})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.404333233833313})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4007628262042999})
store['active_learning_steps'][15]['training']['best_epoch']=12
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.31586455078125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 47321], ['id', 24760], ['id', 40480], ['id', 16748], ['id', 13276], ['id', 4156], ['id', 31302], ['ood', 40962], ['id', 7386], ['id', 33], ['id', 36126], ['id', 34366], ['id', 47296], ['id', 43095], ['id', 58855], ['id', 34968], ['id', 59653], ['id', 48382], ['id', 6658], ['id', 137]], 'labels': [2, 8, 3, 3, 5, 3, 5, 5, 7, 9, 5, 3, 5, 6, 3, 8, 0, 8, 3, 8], 'scores': [0.689365565776825, 0.6991181075572968, 0.8125805854797363, 0.9465306401252747, 0.6552044153213501, 0.7051388025283813, 0.8017430305480957, 0.4682539701461792, 0.5501925945281982, 0.5550610721111298, 0.6765570938587189, 0.8138139247894287, 0.5978471040725708, 0.6381563544273376, 0.6112770438194275, 1.0274373292922974, 0.6767165064811707, 0.8213343620300293, 0.6748224496841431, 0.33418896794319153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2231459617614746})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5816364288330078})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41776585578918457})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4110877215862274})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36632877588272095})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32473599910736084})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3367025852203369})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30203795433044434})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3393235206604004})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3390512466430664})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3094697594642639})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9632, 'crossentropy': 0.3106220947265625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 51438], ['id', 8202], ['id', 13900], ['id', 53567], ['id', 29109], ['id', 15892], ['id', 42968], ['id', 8861], ['id', 3811], ['id', 28601], ['id', 23732], ['id', 1032], ['id', 34328], ['id', 24688], ['id', 46318], ['id', 50905], ['id', 30622], ['id', 27793], ['id', 20659], ['id', 28149]], 'labels': [6, 2, 7, 5, 7, 5, 1, 7, 1, 9, 9, 5, 8, 1, 9, 7, 5, 1, 1, 9], 'scores': [0.5112617909908295, 0.8392399549484253, 0.39930635690689087, 0.9383188486099243, 0.7195748686790466, 0.7267968058586121, 0.44934940338134766, 0.7187692523002625, 0.7973328828811646, 0.750739187002182, 1.0258578658103943, 0.7032337784767151, 0.8722527623176575, 0.6133958697319031, 0.30915316939353943, 0.7179285883903503, 0.8585266768932343, 0.8971741795539856, 0.702025830745697, 0.7938717901706696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0708706378936768})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.536867618560791})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34738314151763916})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37213605642318726})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33311891555786133})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3255596458911896})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30614733695983887})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32090333104133606})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3583669364452362})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30883705615997314})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.2860923828125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 50317], ['id', 38080], ['id', 22635], ['id', 58537], ['id', 57628], ['id', 17890], ['id', 47723], ['id', 8552], ['id', 36450], ['id', 30883], ['id', 29212], ['id', 3810], ['id', 36166], ['id', 11708], ['ood', 51279], ['id', 22283], ['id', 14715], ['id', 43950], ['ood', 46073], ['id', 50369]], 'labels': [3, 2, 2, 5, 2, 5, 8, 2, 2, 3, 7, 3, 2, 3, 3, 9, 4, 9, 7, 3], 'scores': [0.8194058537483215, 0.6787279844284058, 0.9089020490646362, 0.564426451921463, 0.7847217917442322, 0.6192959547042847, 0.6734482645988464, 0.664775013923645, 0.8769892454147339, 0.889381468296051, 0.7286196947097778, 0.980597972869873, 0.8441734910011292, 0.9810549020767212, 0.31667232513427734, 0.5942376255989075, 0.8372283577919006, 0.7561298608779907, 0.44851911067962646, 0.7733302116394043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0989165306091309})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5398805141448975})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44550859928131104})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36256128549575806})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40658509731292725})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3367895185947418})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30491238832473755})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2980937659740448})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3111371397972107})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32185959815979004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31459060311317444})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.278510595703125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 31184], ['id', 29179], ['id', 57718], ['id', 53584], ['id', 2406], ['id', 37080], ['id', 32774], ['id', 47036], ['id', 41560], ['id', 17592], ['id', 23919], ['id', 31690], ['id', 58275], ['id', 16951], ['id', 25857], ['id', 4050], ['ood', 24172], ['id', 34847], ['id', 47503], ['id', 56313]], 'labels': [9, 8, 7, 3, 4, 4, 8, 2, 8, 4, 9, 7, 0, 8, 1, 9, 4, 0, 5, 8], 'scores': [1.0425482392311096, 0.66215980052948, 0.8384266495704651, 0.3970472514629364, 0.6458553075790405, 0.42748990654945374, 0.8119088113307953, 0.8468680679798126, 0.4271800220012665, 0.7265063524246216, 0.5973526835441589, 0.6389189958572388, 0.6998671889305115, 0.7115492224693298, 0.3420529067516327, 0.6469472646713257, 0.584918737411499, 1.1014761924743652, 0.705955982208252, 0.5521483421325684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1692454814910889})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5668728947639465})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3866751790046692})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30005282163619995})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2962380349636078})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.281821608543396})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.283463716506958})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2737736105918884})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3041204810142517})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29432380199432373})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28563496470451355})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2645596435546875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 29611], ['id', 16911], ['id', 7984], ['id', 20211], ['id', 54885], ['id', 32453], ['id', 21023], ['id', 11837], ['id', 20171], ['ood', 9928], ['id', 39734], ['id', 48102], ['id', 38974], ['id', 53342], ['id', 16156], ['id', 42004], ['id', 4694], ['id', 45602], ['id', 54628], ['id', 19702]], 'labels': [2, 3, 4, 4, 6, 8, 2, 3, 5, 1, 2, 7, 1, 9, 3, 7, 3, 5, 4, 5], 'scores': [0.7456739246845245, 0.9490980505943298, 0.8305143713951111, 0.40480145812034607, 0.638852596282959, 0.8704431056976318, 0.7208212614059448, 0.49257373809814453, 0.9007255434989929, 0.5672355890274048, 0.7525128126144409, 0.9420382976531982, 0.8648085594177246, 0.6048048138618469, 0.5997602641582489, 0.686714768409729, 0.7186416387557983, 0.8859129548072815, 0.7816608548164368, 0.8127836585044861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1329149007797241})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5604337453842163})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42520391941070557})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34968966245651245})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3240625560283661})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3173028826713562})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2776542603969574})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3114359676837921})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29717719554901123})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.333188533782959})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.255068310546875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 53872], ['id', 31845], ['id', 27576], ['id', 52462], ['id', 45282], ['id', 49438], ['id', 43226], ['id', 22002], ['id', 24927], ['id', 44998], ['id', 8200], ['id', 33150], ['id', 45456], ['id', 49962], ['id', 10048], ['id', 50753], ['id', 30986], ['ood', 41587], ['id', 24990], ['id', 57728]], 'labels': [8, 8, 5, 9, 5, 8, 8, 3, 9, 4, 3, 8, 7, 2, 1, 2, 3, 5, 7, 9], 'scores': [0.891197681427002, 0.6331510543823242, 0.54323810338974, 0.9732598662376404, 0.6223421990871429, 0.6853148341178894, 0.5609050989151001, 0.6002266108989716, 0.548551082611084, 0.8008291721343994, 0.7356364727020264, 0.6490443348884583, 0.6137149333953857, 0.6751752495765686, 0.678650975227356, 0.7520864009857178, 0.599945604801178, 0.433587908744812, 0.5490720272064209, 0.8366175889968872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2166671752929688})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6419578790664673})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44016146659851074})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33076274394989014})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29278960824012756})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2753147482872009})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.3103540539741516})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.263967365026474})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30829286575317383})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2897270619869232})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.301259309053421})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.2403452392578125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 4646], ['id', 17079], ['id', 5845], ['id', 5276], ['id', 30688], ['ood', 50960], ['ood', 17221], ['id', 33812], ['ood', 12327], ['id', 50236], ['id', 8883], ['id', 36072], ['id', 53568], ['id', 18514], ['id', 59734], ['id', 7886], ['id', 56842], ['ood', 10566], ['id', 50090], ['id', 21471]], 'labels': [2, 6, 2, 9, 8, 5, 3, 6, 5, 0, 2, 2, 5, 2, 2, 9, 8, 1, 4, 9], 'scores': [0.8283588886260986, 0.8740655779838562, 0.559433102607727, 0.5389683842658997, 0.7160371541976929, 0.4643700122833252, 0.40322232246398926, 0.7483240365982056, 0.4784574508666992, 0.6729977130889893, 0.6142500638961792, 0.9124414324760437, 0.650156706571579, 0.752678394317627, 0.5350738763809204, 0.6869665682315826, 0.7110452651977539, 0.41690123081207275, 0.9026781916618347, 0.6295185685157776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2951374053955078})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.633746862411499})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.42776864767074585})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3356281816959381})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28050392866134644})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27500027418136597})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2967318892478943})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.252183198928833})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2558934688568115})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2530336380004883})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26806169748306274})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.25865673828125}
