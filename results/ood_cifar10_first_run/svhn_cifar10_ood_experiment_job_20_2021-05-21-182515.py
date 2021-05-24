store = {}
store['timestamp']=1621617915
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=20']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=20
store['worker_id']=20
store['num_workers']=24
store['config']={'seed': 1256, 'uniform_ood': True, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('SVHN (Train, seed=0, 73257 samples)' | uniform_targets{'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 13.296768188476562})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 9.375965118408203})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 9.42388916015625})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 12.129905700683594})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 10.732376098632812})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 10.112564086914062})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 11.611311912536621})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1784, 'crossentropy': 12.6072453125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36096], ['id', 35815], ['id', 35509], ['ood', 36064], ['ood', 67508]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7438942058446121, 1.4492048230095924, 2.113673070055741, 2.666572946264478, 3.1608467070237456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 8.109910011291504})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 9.388101577758789})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 7.425780296325684})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 8.373353958129883})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1796, 'crossentropy': 8.49097109375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 60551], ['ood', 39981], ['ood', 40096], ['ood', 69570], ['id', 8782]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8986786759386924, 1.6584646250152986, 2.3128124257373557, 2.818705227642001, 3.237531017989392]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.097993850708008})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 10.904581069946289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 9.570262908935547})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.382857322692871})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.576955318450928})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.678195953369141})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.861000061035156})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.6909074783325195})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.798954010009766})
store['active_learning_steps'][2]['training']['best_epoch']=6
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.1851, 'crossentropy': 5.414998046875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 17624], ['id', 34759], ['id', 17159], ['id', 17759], ['id', 7922]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9340985569598421, 1.7828297507458108, 2.3701196073241655, 2.8597563654599707, 3.292960232658448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 6.993081092834473})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.628748893737793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 11.82586669921875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.191398620605469})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.759406089782715})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 9.858268737792969})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 7.230818748474121})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2078, 'crossentropy': 6.4896953125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 3729], ['id', 19470], ['id', 6926], ['id', 30535], ['id', 28841]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7944029677022443, 1.3947806023216534, 1.92532489582182, 2.3910802903302786, 2.7934561674663456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.981724262237549})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.672268867492676})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.524814605712891})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.202333450317383})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 7.1607441902160645})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.607183456420898})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.838482856750488})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.1865, 'crossentropy': 6.5886234375}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 29741], ['id', 31556], ['id', 45268], ['ood', 42702], ['id', 7236]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8670637858151529, 1.6091608967058137, 2.1955567311600164, 2.695947165252175, 3.097810381478155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 7.374714374542236})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 4.452535629272461})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.556868553161621})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.785799980163574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.262651443481445})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 6.282244682312012})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.8733320236206055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.5688958168029785})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.216, 'crossentropy': 6.16498125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 18076], ['ood', 61672], ['ood', 48696], ['ood', 3160], ['id', 27545]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8791209674077349, 1.5540952327393036, 2.0699442716070195, 2.5537065278401805, 2.9592097197866982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.041595458984375})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.189352512359619})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.555874824523926})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.545612335205078})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.227911949157715})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.205, 'crossentropy': 6.402446875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 7209], ['id', 35694], ['id', 545], ['id', 17620], ['ood', 39340]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7929342760118241, 1.4336953516948285, 2.0005543784798068, 2.49959269811799, 2.9244848009688607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.9887757301330566})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 7.583090782165527})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.799592971801758})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.028390884399414})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.444601535797119})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 7.885039329528809})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.549015998840332})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.207590103149414})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2524, 'crossentropy': 5.553914453125}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 11725], ['id', 35906], ['id', 30446], ['id', 22537], ['id', 20279]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6276944667378028, 1.1996524525908003, 1.6915864126679176, 2.1494411287413637, 2.5632046360131238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.321231365203857})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.453833103179932})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.1598310470581055})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.192609786987305})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.588280200958252})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.2976765632629395})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.273992538452148})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 6.873767852783203})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.350353240966797})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.855343818664551})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.193840026855469})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2508, 'crossentropy': 6.6239734375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 30722], ['id', 47410], ['id', 23016], ['id', 2303], ['id', 47909]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.845984102688065, 1.5331887799688633, 2.1041722857210683, 2.6093124148346067, 3.0294012598555193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.654340744018555})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.907877445220947})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.410882949829102})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.80977725982666})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.455981254577637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.4401512145996094})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.0021867752075195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.565506935119629})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.0419769287109375})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.803882122039795})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.275, 'crossentropy': 5.08743125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 15744], ['id', 9581], ['id', 18711], ['ood', 57845], ['id', 12334]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7550753439244569, 1.4820524680803961, 2.053178492620179, 2.5541467083890153, 3.003658801674433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.758656024932861})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.9052681922912598})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.881991863250732})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.725308418273926})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.821457862854004})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.499758720397949})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.931572914123535})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.153417110443115})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2608, 'crossentropy': 4.606180078125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 10401], ['id', 4890], ['id', 22874], ['ood', 16450], ['id', 48116]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8528905056249685, 1.4030725240725714, 1.923322913224455, 2.381558784149398, 2.7493145415193467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.8736279010772705})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.6876516342163086})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.8123998641967773})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.215778350830078})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.380640983581543})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.6070547103881836})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.625338554382324})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.8294572830200195})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.41768741607666})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.309266090393066})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2533, 'crossentropy': 4.5812015625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 36002], ['id', 43194], ['id', 27328], ['id', 22209], ['id', 13832]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8285867708203243, 1.3998898152000336, 1.9353251499310593, 2.3849029611836166, 2.7699640050252974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.067937850952148})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.5004591941833496})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.927280426025391})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.547645568847656})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.293455123901367})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2585, 'crossentropy': 3.595071484375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 17136], ['id', 23159], ['id', 19745], ['id', 8756], ['id', 47244]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5646914772025577, 1.089374290739511, 1.5676893431594667, 1.9741255246556575, 2.3593570089542713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.3788137435913086})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.140933036804199})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.859683036804199})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.3962931632995605})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.493342399597168})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2644, 'crossentropy': 4.1743078125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 26995], ['id', 28333], ['id', 25112], ['id', 2620], ['id', 34161]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5746670065783368, 1.0782705471195615, 1.529557753072731, 1.9184801259550603, 2.2662886873157273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 3.0088071823120117})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.46467399597168})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.9538614749908447})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.495095252990723})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2582, 'crossentropy': 3.225912890625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 17774], ['id', 6389], ['id', 34812], ['id', 35593], ['id', 7054]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42040479048719304, 0.8191542979346744, 1.1662681556472654, 1.4920566617332032, 1.7665271260621642]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.3603224754333496})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.8383235931396484})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.508841514587402})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.18802547454834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.303805351257324})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2512, 'crossentropy': 3.04627421875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 44940], ['id', 36728], ['id', 13475], ['id', 11046], ['id', 45532]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.43393345543842887, 0.803768083906232, 1.1492567396152849, 1.4811014610514475, 1.7695695358633454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.0332679748535156})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.9722728729248047})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.995748519897461})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.789179801940918})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.532958984375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.069674491882324})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.749753475189209})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2813, 'crossentropy': 3.81213671875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 39513], ['id', 48582], ['id', 47723], ['id', 2677], ['id', 27852]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7017348529208101, 1.2835212934647626, 1.7894437977568916, 2.2264218976603405, 2.596781850721788]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 2.657371997833252})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.558847427368164})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.281851291656494})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.594291925430298})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.646727561950684})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 3.7482333183288574})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.122592449188232})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.20524787902832})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.50843620300293})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2553, 'crossentropy': 3.91115}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 4372], ['id', 27323], ['id', 2026], ['id', 40025], ['id', 35989]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5647821516972167, 1.0613649666747165, 1.5211355681735048, 1.939962037829642, 2.322047750069303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.7911643981933594})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.5939154624938965})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.48958420753479})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.3105857372283936})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.134714126586914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.038572311401367})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.90858793258667})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.1662468910217285})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.212554931640625})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.83543062210083})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.3336334228515625})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2676, 'crossentropy': 4.132694921875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 32556], ['id', 28436], ['id', 17535], ['id', 34212], ['id', 2673]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5727764227776282, 1.0837034522362803, 1.5677951686480238, 2.008567174679299, 2.3891324239756173]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.0952510833740234})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.788912773132324})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.6519508361816406})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.169849395751953})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.9299564361572266})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.8897409439086914})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2234, 'crossentropy': 3.7468546875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 22871], ['id', 1258], ['id', 39489], ['id', 37577], ['id', 15994]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5296737588136184, 0.9568485267009943, 1.3298003471303215, 1.6686325641063764, 1.9798810115354577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.1479735374450684})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.195408821105957})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.286609649658203})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.803832530975342})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.9779343605041504})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2552, 'crossentropy': 4.319728125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 44494], ['id', 23829], ['id', 42660], ['id', 11115], ['id', 2808]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5947528192660188, 1.167959876509617, 1.6760780983492194, 2.11918238660858, 2.4933052342167503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 2.6687488555908203})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.2042717933654785})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.432826042175293})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.6451077461242676})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.744485378265381})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2745, 'crossentropy': 3.209862890625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 20430], ['id', 32114], ['id', 30094], ['id', 22042], ['id', 486]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45134935732225534, 0.8522158481876487, 1.1966266395334735, 1.5318127891542943, 1.8285941682908256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.891286849975586})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.996145248413086})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.405979633331299})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.9064621925354004})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2927, 'crossentropy': 2.9656470703125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 42687], ['id', 25199], ['id', 19967], ['id', 2140], ['id', 47612]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5237399866915862, 0.9038968980905824, 1.25871459510472, 1.5369895200282775, 1.7792743539994014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.9071216583251953})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.5275373458862305})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.5934619903564453})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.320067882537842})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.299748420715332})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 3.8571343421936035})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.6579976081848145})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.396683692932129})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 3.7978262901306152})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2959, 'crossentropy': 3.897904296875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 47269], ['id', 13581], ['id', 12849], ['id', 33324], ['id', 10352]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5648720380926102, 1.0823904646500448, 1.5152435236198007, 1.9098696796260892, 2.267023582246779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.49138069152832})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.8798253536224365})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.9252405166625977})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.329482078552246})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.308296203613281})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.485930919647217})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2656, 'crossentropy': 2.9940052734375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 34218], ['id', 25481], ['ood', 30764], ['id', 16526], ['id', 7040]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4543041970430175, 0.8769296553101817, 1.278495235405102, 1.60182548336812, 1.8874572990424294]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 2.4708118438720703})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.8044381141662598})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.873465061187744})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.4917354583740234})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 4.511794567108154})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.710099220275879})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2758, 'crossentropy': 2.9497640625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 4536], ['id', 43840], ['id', 38608], ['id', 45398], ['id', 21679]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4783515362096866, 0.8891107559722848, 1.268052547199705, 1.6324086554317487, 1.968517394789428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 2.801833152770996})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.8194165229797363})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 3.5754690170288086})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.5386803150177})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.759909629821777})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.061216831207275})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2834, 'crossentropy': 3.4429640625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 52861], ['id', 2785], ['id', 46993], ['id', 22026], ['id', 22651]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7508634906271638, 1.2646186735822535, 1.6853126466180992, 2.079504269649534, 2.422707883096747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.2418503761291504})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 2.440992832183838})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.5434212684631348})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.7032995223999023})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 3.1399312019348145})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.0370330810546875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 4.480541229248047})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 4.097932815551758})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.291129112243652})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.780014514923096})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2924, 'crossentropy': 4.60684765625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 29511], ['id', 40663], ['id', 33736], ['id', 46110], ['id', 39117]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5717828344561813, 1.0938714414192852, 1.5559079556279425, 1.9915476123350215, 2.3419408155899255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.34421443939209})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.2558584213256836})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.085041046142578})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.9590446949005127})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.3471856117248535})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2876, 'crossentropy': 2.2672970703125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 34619], ['id', 44161], ['id', 32816], ['id', 35159], ['id', 28565]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34305131888800533, 0.6541564382099905, 0.9335868125960314, 1.1791156546732502, 1.417896865120996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.582207441329956})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.742971420288086})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.0959062576293945})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.367392539978027})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.615734100341797})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.3369154930114746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.2822041511535645})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.441293239593506})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.617824554443359})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.7757792472839355})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2825, 'crossentropy': 3.319019140625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 43187], ['id', 33453], ['ood', 13301], ['id', 43866], ['id', 22222]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5672669331865114, 1.0531464102434676, 1.5126169951054735, 1.91520263233107, 2.2682670279038106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.3330187797546387})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.805762767791748})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.8940062522888184})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.7476296424865723})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.8390016555786133})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.8772389888763428})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.7451272010803223})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2859, 'crossentropy': 3.5091140625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 33507], ['id', 47173], ['id', 29101], ['id', 35821], ['id', 45288]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4559375123375773, 0.8881945858804745, 1.2833887833120041, 1.6595136989664416, 2.0096464022095653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.269362688064575})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.7229745388031006})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.222792148590088})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.323641300201416})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.271486282348633})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.0647335052490234})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.3056, 'crossentropy': 2.992547265625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 43746], ['id', 19387], ['id', 25646], ['id', 26633], ['id', 26384]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5188719207450208, 0.9332578391975765, 1.2774781772548267, 1.587726405624048, 1.8911687019001677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.6636199951171875})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.2562832832336426})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.9271481037139893})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 3.025526523590088})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.9618520736694336})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.672851324081421})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.1732053756713867})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.3148, 'crossentropy': 3.0460505859375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 7641], ['id', 35275], ['id', 27845], ['id', 33550], ['id', 30451]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4520347670073743, 0.8515519931555864, 1.2136236494687083, 1.515119519956614, 1.799191063518201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.5942015647888184})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.5826733112335205})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.8705358505249023})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.1743781566619873})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.12577486038208})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2767, 'crossentropy': 2.546614453125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 1790], ['id', 42423], ['id', 2155], ['id', 3001], ['id', 35563]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.41720098087106905, 0.8032718796444422, 1.1709217963410605, 1.4780527017558782, 1.7438869965851893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.4688258171081543})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.3000850677490234})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.4368505477905273})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 3.749286651611328})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.7127010822296143})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 3.7793617248535156})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.8608438968658447})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.3206, 'crossentropy': 3.500448046875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 3788], ['id', 20830], ['id', 610], ['id', 47454], ['id', 27392]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4959014663303396, 0.9563279233263966, 1.356267697184121, 1.7074817477349225, 2.0422022111176945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.3949790000915527})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.3396167755126953})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.7905197143554688})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.089776039123535})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2793, 'crossentropy': 2.431022265625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 20503], ['ood', 58411], ['id', 26895], ['ood', 4177], ['ood', 3756]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3745404239233624, 0.6828438528237748, 0.9652123055899153, 1.233961560319167, 1.478651197325691]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.282196521759033})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.6661648750305176})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.659755229949951})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.0852441787719727})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.703059196472168})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.37803840637207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.060467004776001})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2863, 'crossentropy': 3.039935546875}
