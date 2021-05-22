store = {}
store['timestamp']=1621608543
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=10']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=24
store['config']={'seed': 1245, 'uniform_ood': False, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('SVHN (Train, seed=0, 73257 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 10.352483749389648})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 9.362070083618164})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 9.203985214233398})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 11.14476203918457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 11.665771484375})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 11.917619705200195})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 14.124574661254883})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 12.28691291809082})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1721, 'crossentropy': 11.8341671875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 4.765851974487305})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 4.692678451538086})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 4.760173797607422})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 4.852289199829102})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.060214519500732})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.267216682434082})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.8109636306762695})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 39513], ['id', 0], ['id', 1], ['id', 2], ['id', 3]], 'labels': [0, 1, 4, 6, 7], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 10.70358657836914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 9.015809059143066})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 10.511340141296387})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 11.596418380737305})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 10.517168045043945})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1962, 'crossentropy': 8.82558125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.9451889991760254})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.069223403930664})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.223419189453125})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 4.807211875915527})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 42736], ['id', 4288], ['id', 28650], ['ood', 33395], ['id', 8190]], 'labels': [5, 4, 8, -1, 8], 'scores': [0.7036224756175291, 1.2770337030180126, 1.794206057702926, 2.177835901725996, 2.4944285096179954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 8.040776252746582})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 9.132753372192383})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 9.244677543640137})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 9.603015899658203})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 8.834779739379883})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 9.549002647399902})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 11.898128509521484})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 10.553810119628906})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.208, 'crossentropy': 9.306765625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.325098037719727})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.042186737060547})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.05788516998291})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.736724376678467})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 69130], ['ood', 14082], ['id', 34228], ['id', 30307], ['id', 38125]], 'labels': [-1, -1, 5, 0, 0], 'scores': [0.6525223903993439, 1.224664340953487, 1.745750162600495, 2.1970927792397745, 2.5334003797485876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 10.250848770141602})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 8.240848541259766})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 10.249130249023438})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 10.529598236083984})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 10.171297073364258})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2017, 'crossentropy': 8.232}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.7971668243408203})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.110852241516113})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.9524974822998047})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.911106586456299})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 13296], ['id', 4], ['id', 5], ['id', 6], ['id', 7]], 'labels': [3, 8, 4, 7, 5], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.635560989379883})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.934946537017822})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 9.379464149475098})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 9.521053314208984})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2289, 'crossentropy': 6.84323359375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.161156177520752})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.420781373977661})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.8709158897399902})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 41020], ['ood', 9075], ['id', 7134], ['id', 3276], ['ood', 61646]], 'labels': [-1, -1, 1, 3, -1], 'scores': [0.547294480742379, 1.055665185719183, 1.5351567614685773, 1.8738689200207208, 2.1645518999753808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 10.345545768737793})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 8.345968246459961})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 7.753795623779297})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 7.550052642822266})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 8.136967658996582})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 8.836456298828125})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.2095, 'crossentropy': 7.801075}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.6251144409179688})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.4625449180603027})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.800112724304199})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.274937629699707})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 17921], ['ood', 27115], ['id', 10364], ['ood', 18638], ['ood', 28449]], 'labels': [7, -1, 0, -1, -1], 'scores': [0.5762687164822351, 1.0539155042517128, 1.509489835096232, 1.9252007642136215, 2.2633432145264276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 7.188477993011475})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.555095195770264})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 8.468186378479004})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 8.5218505859375})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.2109, 'crossentropy': 7.00728359375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.47194242477417})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.8560256958007812})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.790874481201172})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 19081], ['id', 30605], ['id', 20365], ['id', 6466], ['id', 14366]], 'labels': [-1, 8, 4, 8, 1], 'scores': [0.48549665746265996, 0.913863371361791, 1.2819723237645912, 1.5506867953680346, 1.8016457683229858]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 8.249425888061523})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 7.45556640625})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 8.201385498046875})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 9.468815803527832})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 8.758113861083984})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2033, 'crossentropy': 7.374228125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.187685012817383})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.5378479957580566})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.7082555294036865})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.998222827911377})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 71156], ['id', 19358], ['id', 46434], ['ood', 967], ['id', 44086]], 'labels': [-1, 1, 6, -1, 4], 'scores': [0.5328927784358004, 1.0070328853218977, 1.4245339929940908, 1.7787300332256315, 2.0908112810171913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.343021392822266})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.092259407043457})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 7.4091644287109375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 7.653938293457031})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 7.54852294921875})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 7.897639274597168})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 7.2396650314331055})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 7.413796424865723})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 8.379940032958984})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 9.956989288330078})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.251588821411133})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.834803581237793})
store['active_learning_steps'][8]['training']['best_epoch']=9
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2282, 'crossentropy': 8.47478046875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.7725565433502197})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.478724241256714})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.7657814025878906})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.740177631378174})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.492031097412109})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 2608], ['ood', 23483], ['ood', 56956], ['ood', 53438], ['id', 15505]], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.7043028611383705, 1.3118593483486354, 1.811773427590565, 2.2692481435380527, 2.5984597919826515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 6.285834312438965})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 7.618298530578613})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.5283918380737305})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 11.740748405456543})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 8.316222190856934})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 7.852560520172119})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2239, 'crossentropy': 6.8358796875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.5235252380371094})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.3344297409057617})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.9976282119750977})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.5233821868896484})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 45551], ['id', 42631], ['id', 7586], ['id', 26195], ['ood', 3280]], 'labels': [4, 0, 8, 0, -1], 'scores': [0.5212337726457774, 1.0093157387372813, 1.4281742954460794, 1.813061160215549, 2.140150422992736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.266900062561035})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.265765190124512})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.931822776794434})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.034348487854004})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2094, 'crossentropy': 6.027256640625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.488919258117676})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.429805040359497})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.752077341079712})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 46923], ['ood', 55357], ['id', 23190], ['ood', 16311], ['ood', 24196]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.5872135122657136, 1.1023617998339885, 1.5882440487360692, 1.9466850145978225, 2.262510777598515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.316596984863281})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 7.7008280754089355})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.7399444580078125})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 8.199816703796387})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 8.228979110717773})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 9.201493263244629})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2106, 'crossentropy': 6.91892890625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.800755739212036})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.381077766418457})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.389756679534912})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.936398983001709})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.108936309814453})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 310], ['ood', 63258], ['id', 30588], ['ood', 43486], ['id', 36892]], 'labels': [-1, -1, 9, -1, 3], 'scores': [0.5892530142306458, 1.1334964905720724, 1.5956548456103934, 1.984303562395029, 2.2877005845087437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.527618408203125})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.547364711761475})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.226029396057129})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 7.7639265060424805})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.076226234436035})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 7.313313007354736})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2343, 'crossentropy': 6.53439375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.1077187061309814})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.7461938858032227})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.5380661487579346})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.212204933166504})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.556527614593506})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 5395], ['id', 48350], ['ood', 54975], ['id', 9014], ['id', 22174]], 'labels': [2, 0, -1, 7, 0], 'scores': [0.5427674908799238, 0.9704079561322945, 1.3510691245244324, 1.7024039633446986, 2.0251798736564908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.819159030914307})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 8.805784225463867})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.257250785827637})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 7.94769287109375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 7.029893398284912})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 7.328719139099121})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.077281951904297})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2348, 'crossentropy': 7.8656703125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.122386932373047})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.5947959423065186})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.6204395294189453})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.8763022422790527})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.081378936767578})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.114141464233398})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 21218], ['id', 37040], ['ood', 28637], ['id', 5906], ['ood', 30384]], 'labels': [-1, 2, -1, 1, -1], 'scores': [0.5950453496088489, 1.1625086783600143, 1.623749237051614, 2.0443016665996936, 2.389959506954617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.81297492980957})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.489323616027832})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.170239448547363})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.331354141235352})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.188629150390625})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 8.664020538330078})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.783556938171387})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 7.767216205596924})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 8.241918563842773})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 8.300338745117188})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2283, 'crossentropy': 7.00066953125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.0008625984191895})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.8639512062072754})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.506558418273926})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.2962422370910645})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.5797317028045654})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.774930238723755})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 3916], ['ood', 39962], ['id', 29344], ['ood', 16220], ['ood', 64639]], 'labels': [-1, -1, 7, -1, -1], 'scores': [0.5730515857453841, 1.0499235020193949, 1.445048025259366, 1.7932281197285542, 2.105153541264828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.386923789978027})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.504528999328613})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.8597002029418945})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.015063762664795})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 6.765900135040283})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2287, 'crossentropy': 5.934282421875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 4.133376121520996})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.8976950645446777})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.0958075523376465})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.3748059272766113})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 29577], ['ood', 26232], ['id', 9424], ['ood', 46389], ['ood', 38043]], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.5534665353735312, 1.0273114402655108, 1.4627984773748783, 1.7860758011199782, 2.0743115474178966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.953291893005371})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.710062026977539})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 7.454565048217773})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 8.244867324829102})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.843479156494141})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2206, 'crossentropy': 6.77740234375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.003606081008911})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.3435535430908203})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.469144582748413})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.294452667236328})
store['active_learning_steps'][16]['eval_training']['best_epoch']=1
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 44057], ['id', 35109], ['id', 3801], ['id', 48455], ['ood', 2991]], 'labels': [6, 8, 8, 1, -1], 'scores': [0.5931746948688026, 1.121468622965546, 1.4925938969180836, 1.8222623440009418, 2.1179412554118855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.101390361785889})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.579611778259277})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.334150791168213})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.727819442749023})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 8.437658309936523})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2253, 'crossentropy': 4.834139453125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.0662591457366943})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.1645307540893555})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 2.872326374053955})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.0506582260131836})
store['active_learning_steps'][17]['eval_training']['best_epoch']=2
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 69418], ['ood', 26880], ['ood', 22867], ['ood', 20215], ['ood', 38203]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.5128946719611086, 0.96435255839503, 1.3853931270971613, 1.7263854674436157, 1.9986967991003306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.449254035949707})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.952653884887695})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.3877787590026855})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 9.213637351989746})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 7.365403175354004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.093035697937012})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 6.968228340148926})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 7.449614524841309})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.993953227996826})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 6.69869327545166})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.481259346008301})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2383, 'crossentropy': 7.74719609375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.706007480621338})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.2660598754882812})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.2663733959198})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.0653462409973145})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.2669966220855713})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.2429842948913574})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.968245506286621})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 342], ['id', 8017], ['ood', 10829], ['id', 22864], ['ood', 18312]], 'labels': [-1, 7, -1, 8, -1], 'scores': [0.7637965244215276, 1.361454774756957, 1.8883173150344352, 2.2801332067535958, 2.6250564679116284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.961263418197632})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.849449157714844})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.3819169998168945})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.499137878417969})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 8.060776710510254})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2346, 'crossentropy': 5.927407421875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.1093602180480957})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.1700387001037598})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.4499287605285645})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.7705163955688477})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 65363], ['id', 13417], ['id', 36728], ['ood', 7083], ['ood', 64074]], 'labels': [-1, 4, 1, -1, -1], 'scores': [0.47599520753714575, 0.9076451063080289, 1.2729161044457498, 1.6120464163404016, 1.9131830192749195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.657651901245117})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.819283485412598})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.770829200744629})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.145447731018066})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2497, 'crossentropy': 5.0071515625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.791964054107666})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.072366237640381})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.3461592197418213})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 25088], ['id', 17244], ['id', 24708], ['id', 23159], ['ood', 56208]], 'labels': [-1, 5, 0, 0, -1], 'scores': [0.6208037268255314, 1.0667785963170402, 1.4331114175825221, 1.7481418272263358, 2.0101162593125688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.246340751647949})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.847013473510742})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.0896406173706055})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.5692877769470215})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.663637161254883})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.2763166427612305})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 6.272330284118652})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.246, 'crossentropy': 5.45891015625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.358895778656006})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.001376152038574})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.955014705657959})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.118967056274414})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.212721347808838})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.278214454650879})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 72502], ['id', 41419], ['ood', 12130], ['ood', 43191], ['ood', 33702]], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.5584978388471298, 0.9734917627191981, 1.3769014919968523, 1.7552870224421602, 2.090418495210546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.8863091468811035})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.777907848358154})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.078950881958008})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.33438777923584})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.271692276000977})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2446, 'crossentropy': 4.92248203125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.6849727630615234})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.7097291946411133})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.817385673522949})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.9461352825164795})
store['active_learning_steps'][22]['eval_training']['best_epoch']=1
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5601], ['ood', 10540], ['id', 33391], ['id', 14975], ['id', 8882]], 'labels': [6, -1, 1, 8, 0], 'scores': [0.44808162227832526, 0.7986815176374757, 1.1102600978052397, 1.382277287839635, 1.626451031000407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.886460781097412})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.187196731567383})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.5989274978637695})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.630889892578125})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 6.228997230529785})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.600046634674072})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.671746253967285})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 7.352513790130615})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.061334133148193})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2527, 'crossentropy': 5.597087109375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.937967300415039})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.6235756874084473})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.981569290161133})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.911001682281494})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.248135566711426})
store['active_learning_steps'][23]['eval_training']['best_epoch']=2
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 29040], ['id', 5314], ['id', 47298], ['ood', 32409], ['id', 5128]], 'labels': [-1, 8, 7, -1, 7], 'scores': [0.4817860746315037, 0.9292372380645388, 1.3253234530694447, 1.6915394940172117, 2.0214892312100217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.6994142532348633})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.7461934089660645})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.217654228210449})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.695499897003174})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.889280796051025})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2361, 'crossentropy': 6.8355578125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.0834078788757324})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.6931238174438477})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.8674585819244385})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.056488513946533})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 45881], ['id', 14711], ['id', 32111], ['id', 1537], ['ood', 20645]], 'labels': [8, 7, 9, 0, -1], 'scores': [0.4539514017141792, 0.8414829874235996, 1.175338632306587, 1.4706943274970254, 1.7294840492261687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.783731460571289})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.338429927825928})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.759213447570801})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.138952255249023})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.950952053070068})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.744051933288574})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2455, 'crossentropy': 4.885937109375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 2.7898120880126953})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.977174997329712})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.0136046409606934})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.970834255218506})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.6423959732055664})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 17600], ['id', 486], ['ood', 35436], ['ood', 54601], ['id', 38051]], 'labels': [4, 4, -1, -1, 0], 'scores': [0.42420890721786075, 0.7970569118694266, 1.120099640852346, 1.3950286494169095, 1.651222655243414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.5696473121643066})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.865849494934082})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.502041339874268})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.4388813972473145})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2438, 'crossentropy': 3.6214125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.9311065673828125})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.0903244018554688})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 2.810452938079834})
store['active_learning_steps'][26]['eval_training']['best_epoch']=1
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 35911], ['id', 15877], ['ood', 13826], ['ood', 51461], ['id', 12921]], 'labels': [-1, 0, -1, -1, 1], 'scores': [0.22245749127939685, 0.43705217231366644, 0.6446748106175866, 0.8237950268881047, 0.9930117175041797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.5624608993530273})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.7830047607421875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.440994739532471})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.531373977661133})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2681, 'crossentropy': 3.6249453125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.486665725708008})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.891690254211426})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.480433940887451})
store['active_learning_steps'][27]['eval_training']['best_epoch']=1
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 15375], ['ood', 70436], ['ood', 65196], ['ood', 2118], ['ood', 30096]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.3484199213040351, 0.678013385269884, 0.9264176586415127, 1.146560396813359, 1.3513690436303358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.3481173515319824})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.251716613769531})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.029054641723633})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.095026969909668})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.847012519836426})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.958946704864502})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.27069091796875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 6.831347465515137})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.676281452178955})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2468, 'crossentropy': 6.004115625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 2.7527613639831543})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 2.7866318225860596})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.048135995864868})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.411884307861328})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.2924704551696777})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.0090487003326416})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.3725085258483887})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.077122211456299})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 48677], ['id', 40821], ['id', 8765], ['id', 10647], ['id', 37964]], 'labels': [6, 0, 1, 2, 2], 'scores': [0.5160923036057594, 0.9670072475135605, 1.3764388910342507, 1.7352198147915168, 2.0514092611027968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.185336589813232})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.5521240234375})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.82400369644165})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.504030227661133})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.810635566711426})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 6.84003210067749})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.690964698791504})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.533717632293701})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 7.426892280578613})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2738, 'crossentropy': 7.00405390625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.700664520263672})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.9695215225219727})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.9722421169281006})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.3847508430480957})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.241142749786377})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.53762149810791})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.4859447479248047})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 3.208928108215332})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 23235], ['ood', 71903], ['ood', 40671], ['id', 6473], ['ood', 72360]], 'labels': [2, -1, -1, 8, -1], 'scores': [0.5647868314181625, 1.033373952405019, 1.4540245806264491, 1.7826174188159567, 2.0867628204290978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.860966682434082})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.9629876613616943})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.827980041503906})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.229897975921631})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.535651683807373})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.16951847076416})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2435, 'crossentropy': 5.11571171875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.2902824878692627})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.1391055583953857})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.8437514305114746})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.1736159324645996})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.066375970840454})
store['active_learning_steps'][30]['eval_training']['best_epoch']=2
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 47120], ['id', 6623], ['ood', 20874], ['ood', 47972], ['id', 44929]], 'labels': [-1, 8, -1, -1, 7], 'scores': [0.3996360575884981, 0.7616115512543429, 1.1108868344038374, 1.4364978465025793, 1.7128813364473583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 2.9354817867279053})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.819889068603516})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.035654067993164})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.095478534698486})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.792489051818848})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.873291969299316})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.827960014343262})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2661, 'crossentropy': 5.2668640625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.2546000480651855})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 3.1203575134277344})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.273918628692627})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.143366813659668})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.75309419631958})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.318359375})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 56407], ['ood', 71158], ['id', 534], ['ood', 58376], ['ood', 18581]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.4980869724136605, 0.9485555132395929, 1.3705080553807267, 1.7124184924605483, 2.0066869067157684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.3249995708465576})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.250890731811523})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.776609897613525})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.504543304443359})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.2428, 'crossentropy': 3.376020703125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.5777127742767334})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.732727527618408})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 2.9731357097625732})
store['active_learning_steps'][32]['eval_training']['best_epoch']=2
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 69598], ['id', 45923], ['id', 2899], ['id', 33561], ['ood', 62503]], 'labels': [-1, 2, 3, 5, -1], 'scores': [0.5646803566800322, 0.9150156867786239, 1.1872793556619765, 1.3893286839777037, 1.5778707243526782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.7144224643707275})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.759169340133667})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.083153247833252})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.507151126861572})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.533981800079346})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.31256103515625})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2394, 'crossentropy': 4.1487015625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.626978874206543})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.383762836456299})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.9390947818756104})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.9246973991394043})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.284837245941162})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 41537], ['ood', 55358], ['ood', 35521], ['ood', 61330], ['ood', 30034]], 'labels': [1, -1, -1, -1, -1], 'scores': [0.33884743989590094, 0.6150916188922442, 0.8800390303813623, 1.1292618505301615, 1.3538304235422443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.596681594848633})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.4712629318237305})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.470759391784668})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.388439178466797})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.663931846618652})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2482, 'crossentropy': 3.5781421875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.5002923011779785})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.5165510177612305})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.5372695922851562})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.589594602584839})
store['active_learning_steps'][34]['eval_training']['best_epoch']=1
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 68258], ['ood', 22383], ['ood', 23862], ['id', 8871], ['id', 46315]], 'labels': [-1, -1, -1, 9, 9], 'scores': [0.4517224101635238, 0.771329696420525, 1.0678556921519422, 1.3543431712718244, 1.5812046087537102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.82641339302063})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.790229797363281})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.354360580444336})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.373844623565674})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.906948089599609})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.8502655029296875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.377386093139648})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 6.040250778198242})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.252, 'crossentropy': 4.959589453125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.8089311122894287})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.811596393585205})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.129093647003174})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.314143657684326})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.208550453186035})
store['active_learning_steps'][35]['eval_training']['best_epoch']=2
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 33948], ['ood', 36537], ['ood', 39600], ['id', 14014], ['ood', 20294]], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.5379588275821532, 0.9875562506982805, 1.3218874515576413, 1.6230733383191103, 1.8988664688585084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.1624155044555664})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.538495063781738})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.573234558105469})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.8499250411987305})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.94856595993042})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.9033732414245605})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.867034912109375})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 6.7490739822387695})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.931471824645996})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.255, 'crossentropy': 6.054617578125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.0140531063079834})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.6978888511657715})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.1620893478393555})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.2386837005615234})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.8092825412750244})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.404348611831665})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.164397716522217})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.285339832305908})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 9345], ['id', 26307], ['ood', 47697], ['id', 4879], ['id', 24529]], 'labels': [0, 3, -1, 1, 8], 'scores': [0.5636110127767109, 1.0374178609647657, 1.4768970088260676, 1.8663820831425446, 2.1929701564604205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.275872230529785})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.320924282073975})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.927914142608643})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 6.5970611572265625})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.172359466552734})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.779418468475342})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.714563369750977})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.8311614990234375})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.5464863777160645})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 5.136440277099609})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 6.7406415939331055})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.312251567840576})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 6.01879358291626})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.2711, 'crossentropy': 5.073478515625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 2.945512294769287})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.6542673110961914})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.4917778968811035})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.9526000022888184})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.8841114044189453})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.860189914703369})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.194744110107422})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.946591377258301})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.965663194656372})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 22229], ['id', 14783], ['id', 34444], ['ood', 2040], ['id', 33991]], 'labels': [4, 0, 5, -1, 4], 'scores': [0.5182705740475061, 1.0189504482044884, 1.4444247329784372, 1.8254458586937763, 2.149957340457151]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.0020651817321777})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.5734739303588867})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.074482440948486})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.2508134841918945})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.1011457443237305})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.944011688232422})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.2692, 'crossentropy': 4.201362109375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.6639466285705566})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.495331287384033})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.70327091217041})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.6769914627075195})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.8623805046081543})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 38450], ['id', 5259], ['id', 18387], ['ood', 11965], ['id', 10776]], 'labels': [-1, 7, 1, -1, 6], 'scores': [0.37575863575178237, 0.7083555900007852, 1.0348244409803056, 1.313307824392516, 1.5491868750031377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.216327667236328})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.2797584533691406})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.9086754322052})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.242361068725586})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.842145919799805})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.07046365737915})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.528323173522949})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 5.3633880615234375})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 6.159780502319336})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.016385078430176})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.83653450012207})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.2691, 'crossentropy': 5.428683984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 2.6507961750030518})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.8519668579101562})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.8888869285583496})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.69140625})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.7955451011657715})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.091928005218506})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.950178861618042})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.135587215423584})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 28450], ['id', 24377], ['id', 39645], ['ood', 50809], ['ood', 66582]], 'labels': [8, 6, 2, -1, -1], 'scores': [0.5415467137220527, 1.0267486373520907, 1.4775083944430119, 1.8400353687081834, 2.1486711037167376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.4867048263549805})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.7510459423065186})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.7736918926239014})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.928380966186523})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.124452590942383})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 6.017894268035889})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.879125595092773})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 5.3971710205078125})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.586272239685059})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.724294185638428})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.909799575805664})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2699, 'crossentropy': 5.535583203125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.8661742210388184})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.7071986198425293})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.1156554222106934})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.985259532928467})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.7758116722106934})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.028512477874756})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.478093147277832})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 2.701014518737793})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.342989683151245})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.637275218963623})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 35926], ['id', 31584], ['ood', 37852], ['ood', 7048], ['id', 45329]], 'labels': [-1, 4, -1, -1, 8], 'scores': [0.42287686406901887, 0.7950715201748992, 1.1508093963458328, 1.482564326150193, 1.7731407533471844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.953869342803955})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.641451358795166})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.943045139312744})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.442478179931641})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.2507, 'crossentropy': 2.959476953125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.217996597290039})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.4555110931396484})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.4386041164398193})
store['active_learning_steps'][41]['eval_training']['best_epoch']=1
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 47609], ['ood', 21652], ['id', 10864], ['id', 30897], ['id', 30713]], 'labels': [6, -1, 0, 6, 9], 'scores': [0.29399062437519063, 0.5668925422757858, 0.8013890263587822, 0.9982835329834181, 1.1607130598664384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.4845807552337646})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.5276694297790527})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 3.427178144454956})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.1721343994140625})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.46138334274292})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.294394016265869})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.2841, 'crossentropy': 3.6468265625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.7123541831970215})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.681413173675537})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.6855039596557617})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.543067455291748})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.5059947967529297})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 15539], ['id', 1199], ['id', 10716], ['id', 20252], ['ood', 62307]], 'labels': [3, 6, 6, 1, -1], 'scores': [0.568591549231573, 0.9701543279167284, 1.3091905231238967, 1.6231630448010579, 1.8431986200924735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.926572322845459})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.385162115097046})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.8354830741882324})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.6660261154174805})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.499760150909424})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 4.647796630859375})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 5.126128196716309})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.33298397064209})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 5.057929039001465})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.2924, 'crossentropy': 4.715356640625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.2339465618133545})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.7275805473327637})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.7841553688049316})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.6814866065979004})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 3.027620553970337})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 3.1343331336975098})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.6480188369750977})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 3.017516613006592})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 37061], ['id', 11724], ['id', 40720], ['ood', 19752], ['id', 739]], 'labels': [-1, 9, 0, -1, 1], 'scores': [0.49996776378312313, 0.9279556792812076, 1.2690475095990772, 1.575247821608592, 1.839337115505387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.7651422023773193})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.183998107910156})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 3.5499110221862793})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.656732559204102})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.172545433044434})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.662932872772217})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.2782, 'crossentropy': 3.6361515625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.6927921772003174})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.372149705886841})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 2.3698294162750244})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.6954684257507324})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.528951644897461})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 32383], ['id', 28431], ['id', 26956], ['ood', 29032], ['ood', 16266]], 'labels': [-1, 7, 7, -1, -1], 'scores': [0.32724119400645957, 0.6296301559058852, 0.9011909624215826, 1.1550451705489069, 1.382523524581332]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.8266584873199463})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.050978183746338})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.8841915130615234})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.3293328285217285})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.445603370666504})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.956358909606934})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.842301368713379})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.658875942230225})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.682811260223389})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.848742485046387})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 6.495150566101074})
store['active_learning_steps'][45]['training']['best_epoch']=8
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.2835, 'crossentropy': 4.695809765625}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.5405826568603516})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.661792755126953})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.8025708198547363})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.57895565032959})
store['active_learning_steps'][45]['eval_training']['best_epoch']=1
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 20330], ['id', 275], ['ood', 64602], ['ood', 8633], ['ood', 48165]], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.556997632167723, 0.9921118406287155, 1.36891345881957, 1.7118182849793762, 2.008916610899491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.5710599422454834})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.4047439098358154})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.751598358154297})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 3.8046112060546875})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.231565475463867})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.693321228027344})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.101413249969482})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.2773, 'crossentropy': 3.80339453125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.236959457397461})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.6029701232910156})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.5329623222351074})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.752542018890381})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.413175106048584})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.6428070068359375})
store['active_learning_steps'][46]['eval_training']['best_epoch']=5
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 5114], ['ood', 42211], ['ood', 22810], ['ood', 63502], ['id', 44959]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.47560029731974873, 0.8445023691841556, 1.1828951071790161, 1.4605794774449095, 1.6817698049468888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.680877208709717})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.421783447265625})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 3.903594493865967})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.6094565391540527})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.846521377563477})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.666845321655273})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.867692947387695})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.2688, 'crossentropy': 3.681183203125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.5647449493408203})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.6505813598632812})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.4798359870910645})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.6043617725372314})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.609180450439453})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.6573214530944824})
store['active_learning_steps'][47]['eval_training']['best_epoch']=5
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 60764], ['id', 11082], ['ood', 18656], ['ood', 26973], ['id', 21333]], 'labels': [-1, 8, -1, -1, 1], 'scores': [0.45064635416460463, 0.8174882550097871, 1.1211207279914048, 1.4122750304842722, 1.6529547001660116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.64068603515625})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.2273812294006348})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.100861549377441})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.193593978881836})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.928514003753662})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.246376991271973})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.379972457885742})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.897355079650879})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 4.993391513824463})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 6.0632123947143555})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 6.355047225952148})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 5.817704200744629})
store['active_learning_steps'][48]['training']['best_epoch']=9
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.3035, 'crossentropy': 5.051424609375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.138157367706299})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.792705774307251})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.4877567291259766})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.5987374782562256})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.526850938796997})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.6038129329681396})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 2.5569047927856445})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.5790655612945557})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.663186550140381})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.807387351989746})
store['active_learning_steps'][48]['eval_training']['best_epoch']=7
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 66422], ['ood', 30834], ['ood', 16154], ['ood', 72837], ['id', 46731]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.5342657988011204, 1.0088577713133247, 1.4462962904125671, 1.806768397838713, 2.109638020658285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.256162643432617})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.3273048400878906})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.6406476497650146})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.5615344047546387})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.6939191818237305})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.122794151306152})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.272139549255371})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.149433135986328})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.2761, 'crossentropy': 4.780611328125}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.9916398525238037})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.4179372787475586})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.6132171154022217})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.583765745162964})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.005553960800171})
store['active_learning_steps'][49]['eval_training']['best_epoch']=2
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 27145], ['id', 12600], ['ood', 35039], ['id', 35914], ['id', 44516]], 'labels': [-1, 0, -1, 1, 8], 'scores': [0.5182544796942505, 0.9501234878652731, 1.3031620849964693, 1.6369058240725582, 1.9016422414191263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.0976157188415527})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.477234363555908})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.094491958618164})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.1309614181518555})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.072857856750488})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.2703, 'crossentropy': 3.530890625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.674072027206421})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.740513324737549})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.72072172164917})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.613405227661133})
store['active_learning_steps'][50]['eval_training']['best_epoch']=1
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 26694], ['id', 28628], ['id', 37514], ['id', 35764], ['id', 24108]], 'labels': [8, 0, 4, 8, 0], 'scores': [0.3287088779119165, 0.6342262107335337, 0.8904192514063536, 1.1214956265268095, 1.3097556182152115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.932337760925293})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.2465758323669434})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.574774742126465})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.341169834136963})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.696338176727295})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.705707550048828})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.300433158874512})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.429444313049316})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.189455032348633})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.2918, 'crossentropy': 4.7617546875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.1957662105560303})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.6305510997772217})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.7134530544281006})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.8143577575683594})
store['active_learning_steps'][51]['eval_training']['best_epoch']=1
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 63036], ['id', 38055], ['ood', 32013], ['id', 26964], ['id', 46968]], 'labels': [-1, 0, -1, 7, 8], 'scores': [0.5912966884258364, 1.034906938386337, 1.4574165907863366, 1.8181714530478512, 2.1481790650671435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.462341070175171})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.391611099243164})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.6448967456817627})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.465398788452148})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.219898223876953})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.844755172729492})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.991812705993652})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.289963722229004})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.9659857749938965})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.748839378356934})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.236207962036133})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.710556507110596})
store['active_learning_steps'][52]['training']['best_epoch']=9
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.2901, 'crossentropy': 5.95906171875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 2.43984317779541})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.55342698097229})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.9164299964904785})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 2.848278284072876})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.814141273498535})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.7922110557556152})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.9856550693511963})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.807694673538208})
store['active_learning_steps'][52]['eval_training']['best_epoch']=5
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 37532], ['ood', 17648], ['id', 31458], ['id', 23416], ['ood', 33776]], 'labels': [-1, -1, 4, 1, -1], 'scores': [0.496744833671527, 0.9543873940760275, 1.3582360240809588, 1.7225176784116822, 2.0479799566778363]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.761615753173828})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.147878646850586})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.3543806076049805})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.720247268676758})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.3871636390686035})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.9097580909729})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.478289604187012})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.2787, 'crossentropy': 3.720671875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 2.3384361267089844})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.2981722354888916})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.49190616607666})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.5780720710754395})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.5225586891174316})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.9129438400268555})
store['active_learning_steps'][53]['eval_training']['best_epoch']=5
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 48192], ['ood', 22623], ['id', 28671], ['ood', 38404], ['id', 46822]], 'labels': [-1, -1, 0, -1, 4], 'scores': [0.37338517798635573, 0.6624163103306933, 0.9289020706765463, 1.173013746795263, 1.3845502338949665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.575641632080078})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.831246852874756})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.8129611015319824})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 3.5850162506103516})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.053047180175781})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.571371555328369})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 4.637187957763672})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.2918, 'crossentropy': 3.77561015625}
