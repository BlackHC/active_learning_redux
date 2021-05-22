store = {}
store['timestamp']=1621614331
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=14']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=24
store['config']={'seed': 1249, 'uniform_ood': False, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('SVHN (Train, seed=0, 73257 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 11.903768539428711})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 10.608186721801758})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 10.928616523742676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 13.149679183959961})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 13.291670799255371})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1768, 'crossentropy': 10.94850859375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 739], ['id', 0], ['id', 1], ['id', 2], ['id', 3]], 'labels': [1, 1, 4, 6, 7], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 10.612411499023438})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 15.026851654052734})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 9.75377082824707})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 9.246223449707031})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1965, 'crossentropy': 10.88112109375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 30848], ['ood', 56758], ['id', 1529], ['id', 8992], ['ood', 985]], 'labels': [2, -1, 0, 0, -1], 'scores': [0.8913730330430747, 1.5753909716691439, 2.191994948357749, 2.762094883600019, 3.171764642503673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 11.974163055419922})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 9.100587844848633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 9.014314651489258})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 9.189557075500488})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 10.27641487121582})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 11.149890899658203})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 12.4651460647583})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.1909, 'crossentropy': 9.45972734375}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 42640], ['ood', 35909], ['ood', 26556], ['id', 19910], ['id', 364]], 'labels': [-1, -1, -1, 2, 8], 'scores': [0.7754146304496721, 1.50603320616062, 2.0937221813373035, 2.6105175840915162, 3.0365113481514747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 9.2337007522583})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.687358856201172})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.091083526611328})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 8.599283218383789})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 7.575754165649414})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2184, 'crossentropy': 6.7715359375}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 51024], ['id', 12515], ['ood', 31309], ['id', 26275], ['ood', 51928]], 'labels': [-1, 5, -1, 0, -1], 'scores': [0.6650045292151361, 1.243576318576185, 1.7693112189698295, 2.1917058012450763, 2.5713102222028494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 12.251753807067871})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 8.64899730682373})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 8.771886825561523})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 9.024805068969727})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 10.121402740478516})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 18.81800079345703})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 8.52038288116455})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 8.819009780883789})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.1971, 'crossentropy': 10.26500390625}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 50413], ['ood', 70154], ['ood', 49319], ['ood', 71968], ['id', 13782]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.8470632518107828, 1.5961495443017815, 2.2536508295380973, 2.792975193620711, 3.2105932563560993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 8.349611282348633})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 7.74448823928833})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 7.343609809875488})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 7.774558067321777})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 9.994354248046875})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.1905, 'crossentropy': 8.4543890625}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 5656], ['ood', 16450], ['ood', 70435], ['id', 41236], ['ood', 45090]], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.6696178763348473, 1.2749964970300578, 1.810817288357613, 2.3067696428559934, 2.733539294021244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 7.0926055908203125})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.659550666809082})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 8.977611541748047})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 9.311819076538086})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 8.571361541748047})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.2185, 'crossentropy': 6.60109921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 4860], ['ood', 51559], ['ood', 16266], ['ood', 37984], ['ood', 68346]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7713432243027769, 1.4146287753435098, 2.0202245692090877, 2.5292676923618673, 2.9463695682072153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 7.456453323364258})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 9.240242958068848})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 8.410078048706055})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 10.228015899658203})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1914, 'crossentropy': 7.48653984375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 6513], ['ood', 48135], ['id', 20896], ['ood', 30753], ['id', 21010]], 'labels': [4, -1, 3, -1, 9], 'scores': [0.6544404687335008, 1.2559616892033438, 1.7566290197400645, 2.1794179935968634, 2.569497431753333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.821516036987305})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 8.258943557739258})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 8.121753692626953})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 7.620702266693115})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 7.000802040100098})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 8.625276565551758})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.270877838134766})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 8.809038162231445})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 11.310076713562012})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 9.577966690063477})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 9.42294979095459})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.1932, 'crossentropy': 9.034684375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 11218], ['id', 6894], ['id', 25164], ['ood', 17142], ['ood', 17110]], 'labels': [6, 0, 5, -1, -1], 'scores': [0.8825607686170058, 1.6759276299137804, 2.365605188428346, 2.8610285583051507, 3.280541695097038]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.534100532531738})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 7.6770172119140625})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 7.400022029876709})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.3766937255859375})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 7.301856994628906})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 8.739935874938965})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 8.700811386108398})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2232, 'crossentropy': 6.6326265625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 57288], ['ood', 59510], ['ood', 2779], ['id', 33989], ['id', 36367]], 'labels': [-1, -1, -1, 8, 2], 'scores': [0.7563322405321069, 1.4714801801938324, 2.075091455305673, 2.550989824379883, 2.9407892100772113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.934884071350098})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 7.574196815490723})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 7.317738056182861})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 7.553289890289307})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.758813858032227})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 7.983872413635254})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2244, 'crossentropy': 7.27748125}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 27658], ['ood', 2831], ['id', 4678], ['ood', 26107], ['id', 38236]], 'labels': [-1, -1, 7, -1, 9], 'scores': [0.6111337923435141, 1.1337232753490376, 1.615688933070094, 2.0252244240007116, 2.408327304649702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.953441619873047})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.687483787536621})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 6.664666175842285})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 6.9305267333984375})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.415047645568848})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2305, 'crossentropy': 5.82311015625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 11197], ['id', 48943], ['ood', 41531], ['ood', 61646], ['id', 2381]], 'labels': [9, 3, -1, -1, 7], 'scores': [0.7964863487408391, 1.3396555346453045, 1.824036666984342, 2.2760196868636964, 2.665675858136333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.110910415649414})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.703258514404297})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.14738655090332})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.358135223388672})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 6.06015157699585})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 7.495798110961914})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 8.144847869873047})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.535845756530762})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.236, 'crossentropy': 6.39020703125}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 70849], ['id', 25794], ['ood', 3869], ['ood', 68975], ['ood', 30555]], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.6641494031376709, 1.2313980620275142, 1.7509986908014286, 2.1994576484783774, 2.6069313500892903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.608894348144531})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.561652660369873})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.214198112487793})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.566253662109375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.227689743041992})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.0629072189331055})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.798484802246094})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 7.074216842651367})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 7.197465896606445})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 7.73507022857666})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.189478397369385})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2232, 'crossentropy': 7.5182234375}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 66571], ['ood', 62007], ['id', 44196], ['ood', 46175], ['id', 43240]], 'labels': [-1, -1, 4, -1, 1], 'scores': [0.6071212138453341, 1.1713766708847206, 1.7070830522089881, 2.1804809902263873, 2.600476106386104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.220320701599121})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.032238006591797})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.7632012367248535})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.19938850402832})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 7.008527755737305})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 8.202011108398438})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 7.287319660186768})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 7.831943988800049})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 7.305160999298096})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.75779914855957})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 7.021063804626465})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 6.531307220458984})
store['active_learning_steps'][14]['training']['best_epoch']=9
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2251, 'crossentropy': 7.80192578125}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 61920], ['id', 7540], ['id', 784], ['id', 42066], ['ood', 54053]], 'labels': [-1, 0, 8, 8, -1], 'scores': [0.7522071222795674, 1.4288031308772493, 1.9920205908871491, 2.4897869670737975, 2.89484898870617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.1907548904418945})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.396577835083008})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.2356367111206055})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.244049072265625})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.93309211730957})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 7.626163482666016})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 6.860547065734863})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.777085304260254})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 9.066656112670898})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.120929718017578})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 7.3347673416137695})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2376, 'crossentropy': 7.19032734375}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 40553], ['id', 24134], ['ood', 22864], ['ood', 2117], ['id', 24500]], 'labels': [-1, 2, -1, -1, 0], 'scores': [0.6563051414693235, 1.2743447060009592, 1.8488103534219653, 2.3688263976436694, 2.809670773371538]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.155014991760254})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.170375823974609})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.790863037109375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.9957122802734375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.9543867111206055})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.79282283782959})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.476131439208984})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2357, 'crossentropy': 5.302432421875}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 16158], ['ood', 71458], ['ood', 44235], ['ood', 27829], ['ood', 8726]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.6924312889507052, 1.3131625765953148, 1.8109320310602124, 2.2179555989092883, 2.5982432099270625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.141674995422363})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.23565673828125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.431140422821045})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.942612648010254})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.823037147521973})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 6.91081428527832})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 7.694208145141602})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 7.682384490966797})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2184, 'crossentropy': 5.9790765625}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 16888], ['ood', 8718], ['ood', 36537], ['id', 19755], ['ood', 1688]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.8198447182132538, 1.382856145060087, 1.8907759692288022, 2.358618583671502, 2.7411418534475196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.898430824279785})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 9.990030288696289})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.995608329772949})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.6652069091796875})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.829751014709473})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 7.523049354553223})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2243, 'crossentropy': 6.272594140625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 31047], ['id', 43743], ['ood', 10987], ['id', 4238], ['id', 34292]], 'labels': [0, 8, -1, 8, 4], 'scores': [0.7209777880218269, 1.3789759777948367, 1.9944892028289885, 2.4337853385441512, 2.82002203850828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.9791102409362793})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.293286323547363})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.910479545593262})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.598855972290039})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2449, 'crossentropy': 4.183618359375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 24014], ['ood', 34097], ['id', 35878], ['ood', 41021], ['id', 19928]], 'labels': [-1, -1, 9, -1, 8], 'scores': [0.4972543604918682, 0.9584484392733819, 1.4050785256731633, 1.7632590379117214, 2.0649032244663053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.935171127319336})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.683879852294922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.626964569091797})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 6.2427215576171875})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 7.178906440734863})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.514009475708008})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.702334403991699})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.234, 'crossentropy': 6.408138671875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 39621], ['ood', 10416], ['id', 10957], ['ood', 34446], ['ood', 1373]], 'labels': [-1, -1, 7, -1, -1], 'scores': [0.6750532027070062, 1.2617516219806615, 1.787906972979842, 2.2581509634735255, 2.68427212059793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.100226402282715})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.405139446258545})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.524953365325928})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.648306846618652})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.911352157592773})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.988231658935547})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2125, 'crossentropy': 6.638728125}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 23840], ['ood', 61129], ['id', 12176], ['ood', 44516], ['ood', 13728]], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.6317695485452814, 1.119876850341912, 1.5660648271727062, 1.9884392344526916, 2.347139330968055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.905876636505127})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.373346328735352})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 7.136143684387207})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.897396564483643})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.125814437866211})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.901740550994873})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.49327278137207})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.770563125610352})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.25, 'crossentropy': 6.3097234375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 70613], ['ood', 9782], ['ood', 65521], ['id', 46672], ['id', 11878]], 'labels': [-1, -1, -1, 1, 3], 'scores': [0.7095098991697688, 1.3566881186806787, 1.925443397477431, 2.3809982788375104, 2.7870830961937703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.012661933898926})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.567934989929199})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.819740295410156})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.6070876121521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.146751403808594})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.767770290374756})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.438260555267334})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 6.867654800415039})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.726408004760742})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2392, 'crossentropy': 6.212442578125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 56790], ['id', 14746], ['ood', 3917], ['ood', 41375], ['ood', 14912]], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.6757696312447512, 1.2505730262748749, 1.7980012272402286, 2.2948790201677935, 2.703037036948716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.482598781585693})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.086700439453125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.553781509399414})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.048069953918457})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.139817237854004})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.0035552978515625})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 6.295425891876221})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2518, 'crossentropy': 4.959762109375}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 59198], ['ood', 28085], ['id', 19228], ['id', 33616], ['ood', 31188]], 'labels': [-1, -1, 8, 9, -1], 'scores': [0.5777176312642414, 1.0795676717549485, 1.4907590326563773, 1.867098777691858, 2.2128812487751466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.045538425445557})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.709056854248047})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 7.698424339294434})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.505390167236328})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.274631977081299})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2344, 'crossentropy': 4.784509375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 9800], ['ood', 34138], ['id', 39938], ['id', 12285], ['id', 27251]], 'labels': [1, -1, 5, 1, 2], 'scores': [0.5356960181529008, 0.9992994699763589, 1.4423722592232981, 1.8668684063564083, 2.2302219496664843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.044961452484131})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.260122299194336})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.684263706207275})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.493707180023193})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.359683036804199})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.8872456550598145})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.787096977233887})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 5.747321128845215})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.309814453125})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2548, 'crossentropy': 4.985095703125}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 1713], ['ood', 36828], ['ood', 55811], ['id', 46099], ['ood', 71853]], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.757659616432484, 1.3097739120867686, 1.8323501033220433, 2.3133716255054306, 2.754343276418437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.800320148468018})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.058349132537842})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 5.558753490447998})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 5.60428524017334})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 7.815020561218262})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 5.727322101593018})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.891350746154785})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2735, 'crossentropy': 5.673615234375}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 71310], ['ood', 11364], ['ood', 70941], ['id', 3581], ['id', 23930]], 'labels': [-1, -1, -1, 5, 8], 'scores': [0.6920718160064745, 1.3190007144365405, 1.830739700041292, 2.302971407156159, 2.708765557522896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.953741073608398})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.891735076904297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.698863983154297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 5.430964946746826})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 5.588379859924316})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.792178630828857})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.35305118560791})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2711, 'crossentropy': 5.619866796875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 1358], ['ood', 65688], ['id', 25012], ['ood', 54190], ['ood', 6273]], 'labels': [9, -1, 1, -1, -1], 'scores': [0.6668473103927257, 1.228908868876104, 1.7090661338031965, 2.143799149939828, 2.5174830928272893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.00152063369751})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.138952255249023})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.176327705383301})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.914906024932861})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.687610626220703})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.790020942687988})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.615804672241211})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2699, 'crossentropy': 5.330889453125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 10812], ['ood', 22808], ['ood', 11939], ['ood', 50754], ['id', 33705]], 'labels': [9, -1, -1, -1, 1], 'scores': [0.6500187572516976, 1.2141563415723287, 1.7298678633029798, 2.2032255267983025, 2.6199594623467277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.7383551597595215})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.948713302612305})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.006389617919922})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 5.107585430145264})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.703200340270996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.266300201416016})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 5.526492595672607})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 5.169595718383789})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.864941596984863})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 6.125942230224609})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 6.296328544616699})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2795, 'crossentropy': 5.283779296875}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 13056], ['ood', 2972], ['ood', 65233], ['ood', 17108], ['ood', 60020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.663751418249674, 1.233814757774494, 1.7273384046263685, 2.185531678816293, 2.5965577340309833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.810221195220947})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.4761505126953125})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.351016044616699})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 5.096775054931641})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.4623260498046875})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2635, 'crossentropy': 4.902208203125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 25126], ['ood', 8454], ['id', 20564], ['ood', 47059], ['ood', 15380]], 'labels': [5, -1, 8, -1, -1], 'scores': [0.6891242857620166, 1.2969540767725718, 1.801241927020957, 2.269472765444495, 2.664490755883847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.071598529815674})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.50628662109375})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.451302528381348})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.681952476501465})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.272, 'crossentropy': 4.095259375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 61463], ['id', 8357], ['id', 12460], ['id', 31462], ['ood', 16590]], 'labels': [-1, 9, 4, 1, -1], 'scores': [0.421643888455125, 0.815958135556814, 1.1825844180346294, 1.4888071675396617, 1.7678448768999502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 3.492812156677246})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.497135162353516})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.333574295043945})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.964267730712891})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.447535514831543})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 7.170246601104736})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 6.27205228805542})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2634, 'crossentropy': 5.0870625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 40178], ['id', 32021], ['ood', 39287], ['id', 14692], ['id', 3384]], 'labels': [0, 1, -1, 3, 6], 'scores': [0.5396161867770175, 1.0521446680347055, 1.4867040029184304, 1.864338584676278, 2.2226449040791465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.4047040939331055})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.903230667114258})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.913303375244141})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.594472885131836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.4977216720581055})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2629, 'crossentropy': 4.13401640625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 35341], ['ood', 72885], ['id', 19966], ['ood', 8909], ['ood', 24684]], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.46354988542398257, 0.8961541300870062, 1.2521793598930206, 1.585111347819936, 1.9018232966338768]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.857480049133301})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.445163249969482})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.688986778259277})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 5.83759880065918})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 5.590384006500244})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.5090250968933105})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.669970512390137})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.5675249099731445})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2696, 'crossentropy': 5.798397265625}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 13874], ['ood', 38681], ['ood', 40602], ['ood', 45518], ['ood', 37193]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.6938324734226957, 1.2310082019395625, 1.7175367696666743, 2.181662323586533, 2.5787317057396004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.011463165283203})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.622653961181641})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.741994857788086})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.810744285583496})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.166047096252441})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.221213340759277})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 6.478151321411133})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.522351264953613})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2635, 'crossentropy': 5.402177734375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 2107], ['ood', 23489], ['id', 45845], ['ood', 10426], ['ood', 38681]], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.7172714091032935, 1.2833193574135007, 1.7803537774724285, 2.2187541050868678, 2.5960363020634034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.755878448486328})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.295897483825684})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.676966667175293})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 4.883144378662109})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.5200910568237305})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 5.624421119689941})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.951166152954102})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.2909, 'crossentropy': 5.045487890625}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 41660], ['id', 8452], ['id', 32193], ['id', 41081], ['id', 2603]], 'labels': [-1, 2, 0, 8, 7], 'scores': [0.5107293240067159, 0.9635456742724893, 1.3876461751693538, 1.7431352021115618, 2.07976894249701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.719762802124023})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.827311038970947})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.811310768127441})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.143746376037598})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.060316562652588})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 5.021749496459961})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.908297538757324})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.988811492919922})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.924602508544922})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.287, 'crossentropy': 5.101094921875}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 40498], ['ood', 20185], ['id', 3210], ['ood', 25815], ['id', 35137]], 'labels': [-1, -1, 8, -1, 0], 'scores': [0.6778591653934318, 1.2555604865158636, 1.762333888824351, 2.2314345048756774, 2.662183495066909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.584205150604248})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.204259872436523})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.355258941650391})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.505679607391357})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.2536, 'crossentropy': 4.600068359375}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 46591], ['id', 8524], ['id', 39601], ['ood', 72745], ['id', 23480]], 'labels': [-1, 7, 8, -1, 0], 'scores': [0.5239215243957058, 1.0222135078232206, 1.434670676804032, 1.7840865868086553, 2.1170863493435723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.082167148590088})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.376127243041992})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.4110822677612305})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.901632785797119})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 6.873379707336426})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.872613906860352})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 6.299750328063965})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 6.585327625274658})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 6.6580705642700195})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 7.150959014892578})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2885, 'crossentropy': 6.2203171875}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 71711], ['ood', 26936], ['id', 46181], ['id', 13124], ['ood', 29458]], 'labels': [-1, -1, 9, 6, -1], 'scores': [0.6390269275591942, 1.1878965415509066, 1.6821804549476629, 2.148226257810321, 2.5453591906573187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.9650397300720215})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.631415367126465})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.202574729919434})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.3251953125, 'crossentropy': 4.727259159088135})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 5.0633649826049805})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.3134765625, 'crossentropy': 4.87412691116333})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 5.985469341278076})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.3086, 'crossentropy': 4.807875}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 39516], ['ood', 22617], ['ood', 3126], ['id', 20430], ['ood', 32003]], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.6410091828555777, 1.208891763430331, 1.6752791836359981, 2.106125725217783, 2.486536916210099]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.6037631034851074})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.704597473144531})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.483860969543457})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.587032318115234})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.6425323486328125})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 5.114246368408203})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.5682830810546875})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.889187812805176})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.74886417388916})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.2833, 'crossentropy': 5.146607421875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 5684], ['id', 29733], ['id', 25330], ['ood', 42752], ['id', 20894]], 'labels': [8, 7, 6, -1, 1], 'scores': [0.6784914615860063, 1.2734948915795887, 1.8206297055065366, 2.302043499233786, 2.69573512505937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.8298702239990234})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.40914249420166})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.336971282958984})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.523600101470947})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 5.716639041900635})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 5.605528831481934})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.3193359375, 'crossentropy': 5.618586540222168})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 5.769093990325928})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.326171875, 'crossentropy': 6.524173259735107})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 6.6795454025268555})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 6.889727592468262})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 6.527539253234863})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.3075, 'crossentropy': 6.88220625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 71984], ['ood', 29916], ['ood', 47828], ['id', 10320], ['id', 41153]], 'labels': [-1, -1, -1, 2, 9], 'scores': [0.6771714686589523, 1.3104458109560806, 1.8590069047342834, 2.352322185530335, 2.790696434075607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.8420238494873047})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.8440146446228027})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.274071216583252})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.3203125, 'crossentropy': 4.088497638702393})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.247085094451904})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 5.181524753570557})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 4.707846641540527})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.3079, 'crossentropy': 4.0871453125}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 5963], ['id', 43180], ['ood', 51766], ['ood', 65294], ['ood', 25866]], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.5308259525791685, 1.040612330988067, 1.4729252211174564, 1.8787846239100503, 2.2164294839472234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 3.255009651184082})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 3.847435712814331})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.298041820526123})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 3.9210071563720703})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.372959136962891})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.298, 'crossentropy': 3.9204328125}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 59313], ['id', 17771], ['ood', 41713], ['id', 41533], ['ood', 21258]], 'labels': [-1, 1, -1, 7, -1], 'scores': [0.5458872558227008, 0.9975875771348903, 1.4220447248821233, 1.8127502051331499, 2.180565795039712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.4746766090393066})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.6645545959472656})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 4.160110950469971})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.779470920562744})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 4.977093696594238})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.8557305335998535})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 5.733431339263916})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.384199619293213})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.3214, 'crossentropy': 5.004015234375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 38369], ['id', 17759], ['ood', 15606], ['id', 26369], ['id', 34218]], 'labels': [9, 0, -1, 1, 2], 'scores': [0.5464333322472705, 1.0565298904161713, 1.53225758449034, 1.9673095676652883, 2.360926747454398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.7835655212402344})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 4.260983467102051})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.7181644439697266})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 4.571619987487793})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.541770935058594})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.115833282470703})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 4.877548694610596})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.2948, 'crossentropy': 4.54869609375}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 18434], ['id', 16296], ['ood', 27133], ['id', 13658], ['id', 41571]], 'labels': [-1, 1, -1, 1, 1], 'scores': [0.5157129779269574, 1.0185115510353926, 1.4565489247700487, 1.8657977489696291, 2.2179268615511383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.7805306911468506})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 3.6931233406066895})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 5.572035789489746})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.452268123626709})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 4.261113166809082})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 4.9104437828063965})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 5.992337703704834})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.3330078125, 'crossentropy': 5.832435131072998})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 4.887414932250977})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 5.442010879516602})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.0331010818481445})
store['active_learning_steps'][48]['training']['best_epoch']=8
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.3024, 'crossentropy': 6.002633984375}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 70897], ['id', 46157], ['ood', 48719], ['id', 44447], ['id', 24379]], 'labels': [-1, 7, -1, 2, 0], 'scores': [0.838309156558982, 1.4892385060568065, 2.0701721346713464, 2.5515752209133806, 2.979604446096838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.195378065109253})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.637059211730957})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.532055854797363})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.922051429748535})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 4.609309196472168})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 6.332858085632324})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.330078125, 'crossentropy': 4.902432441711426})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 5.049038887023926})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.3193359375, 'crossentropy': 5.80649995803833})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 5.0103840827941895})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.3138, 'crossentropy': 5.102236328125}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 12797], ['ood', 72364], ['ood', 70912], ['ood', 63649], ['id', 20100]], 'labels': [1, -1, -1, -1, 3], 'scores': [0.5569470219964008, 1.060222315082651, 1.5433239051775685, 1.9715941698027484, 2.3539967052597213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.8928282260894775})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.0162672996521})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.286226749420166})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.3232421875, 'crossentropy': 4.90158224105835})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 4.831840515136719})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.3203125, 'crossentropy': 5.459999084472656})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.3251953125, 'crossentropy': 4.705854892730713})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.691488742828369})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 6.0141401290893555})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 4.8022942543029785})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.2991, 'crossentropy': 4.83479296875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 31529], ['id', 15177], ['ood', 17303], ['id', 42572], ['id', 13879]], 'labels': [-1, 0, -1, 0, 4], 'scores': [0.6455346942746256, 1.1814613765048554, 1.6696238358484514, 2.089171709595605, 2.4659488785465626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 3.1759884357452393})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 3.5078444480895996})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.9166173934936523})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.143547058105469})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.784856796264648})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.370521545410156})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.2905, 'crossentropy': 3.88342421875}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 42733], ['ood', 3322], ['ood', 40281], ['id', 8607], ['ood', 49290]], 'labels': [7, -1, -1, 8, -1], 'scores': [0.5463777664844269, 0.9366188657019636, 1.3077358162776882, 1.6587573923355876, 1.972468326254834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.1075992584228516})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.4329304695129395})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 4.077210903167725})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.189515113830566})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.788931846618652})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.3271484375, 'crossentropy': 4.896622657775879})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.3330078125, 'crossentropy': 4.83597469329834})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 4.677402973175049})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.3291015625, 'crossentropy': 5.04439115524292})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.3232421875, 'crossentropy': 5.292311668395996})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.3033, 'crossentropy': 5.066121484375}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 71587], ['ood', 7047], ['id', 12325], ['ood', 10159], ['ood', 59511]], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.7155774925602394, 1.2420574757092337, 1.7565279902086712, 2.216851389687549, 2.632499648527606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.5311763286590576})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.1741840839385986})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.907110691070557})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.925588607788086})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.3271484375, 'crossentropy': 4.766652584075928})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.322265625, 'crossentropy': 4.281017303466797})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 5.730112075805664})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 5.055939674377441})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.2927, 'crossentropy': 5.197268359375}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 12846], ['ood', 59622], ['id', 23583], ['ood', 21990], ['id', 21999]], 'labels': [5, -1, 7, -1, 0], 'scores': [0.5130044119042616, 0.9976317363468068, 1.443052568238544, 1.8699518233091208, 2.2517988147050048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.7272629737854004})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.8328232765197754})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.33203125, 'crossentropy': 4.305946350097656})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 3.9165234565734863})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 5.215651988983154})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.933917999267578})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.3012, 'crossentropy': 4.74839609375}
