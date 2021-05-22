store = {}
store['timestamp']=1621608534
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=2']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=24
store['config']={'seed': 1236, 'uniform_ood': False, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('SVHN (Train, seed=0, 73257 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 11.836912155151367})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 10.632655143737793})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 10.835405349731445})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 10.795881271362305})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 10.510699272155762})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 10.480644226074219})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 12.674060821533203})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.181, 'crossentropy': 10.77981953125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.19034481048584})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 4.436766624450684})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.18082332611084})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 4.7408857345581055})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.525513648986816})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.890775680541992})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 38935], ['ood', 48256], ['id', 8089], ['ood', 7792], ['id', 25396]], 'labels': [8, -1, 0, -1, 6], 'scores': [0.7438677153941857, 1.292709388284897, 1.7721616853569562, 2.2195507864987647, 2.5740934912269307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 9.418701171875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 8.997245788574219})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 8.524709701538086})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 22.425439834594727})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.689562797546387})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 9.203998565673828})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 9.865251541137695})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 10.218047142028809})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.2064, 'crossentropy': 8.11305078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.559750556945801})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.6094205379486084})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.4148621559143066})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.467075824737549})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.77189302444458})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.025206565856934})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 14902], ['ood', 21036], ['id', 11249], ['id', 1750], ['id', 9683]], 'labels': [3, -1, 2, 2, 0], 'scores': [0.7857331098908379, 1.4557407770941109, 2.020673148218002, 2.5195389775972283, 2.8375504351337097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 7.522598743438721})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 8.49951457977295})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 8.97488784790039})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 14.40284538269043})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.1652, 'crossentropy': 7.88403046875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.084329128265381})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 3.4763808250427246})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 3.7834575176239014})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 66080], ['id', 43582], ['ood', 3329], ['id', 32738], ['ood', 51366]], 'labels': [-1, 9, -1, 8, -1], 'scores': [0.7843845527653398, 1.3543252130286034, 1.82614303368889, 2.243513227528324, 2.5854945711995048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.418558120727539})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.856125831604004})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 8.381879806518555})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 8.022930145263672})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 8.668745040893555})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2093, 'crossentropy': 7.9546}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.232753276824951})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.7875444889068604})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.119081497192383})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.6677751541137695})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 19143], ['id', 26156], ['id', 29331], ['id', 48640], ['ood', 69757]], 'labels': [-1, 8, 0, 0, -1], 'scores': [0.5649363600678008, 1.0763319476035464, 1.553925865336668, 2.0018271416250655, 2.3411212180176553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 7.950549125671387})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.696128845214844})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 7.981134414672852})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 9.125243186950684})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 10.188712120056152})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2159, 'crossentropy': 6.7861609375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.570418357849121})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.0239663124084473})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.377359390258789})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.650740623474121})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 7275], ['ood', 48980], ['id', 315], ['ood', 42288], ['id', 28764]], 'labels': [-1, -1, 0, -1, 4], 'scores': [0.619534614509968, 1.0795285436428395, 1.486606322237221, 1.8436562469435414, 2.1641119126971127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 8.286684036254883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 8.839816093444824})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 7.659911155700684})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 8.032617568969727})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 9.036998748779297})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 8.517251968383789})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 8.944397926330566})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.2121, 'crossentropy': 8.03336796875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.63675594329834})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 3.2610573768615723})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.7879605293273926})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.543018341064453})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 4.139918327331543})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.506265640258789})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 12395], ['id', 34230], ['id', 35267], ['ood', 7496], ['id', 30274]], 'labels': [4, 7, 6, -1, 6], 'scores': [0.5689123069299401, 1.0261349648276137, 1.4260716401390716, 1.799402506268887, 2.108385917895089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.491175651550293})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.804871559143066})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 10.557161331176758})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.948762893676758})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.2213, 'crossentropy': 7.326971875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.8934528827667236})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.691073417663574})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.01770544052124})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 57819], ['id', 42752], ['ood', 69221], ['ood', 37195], ['id', 8712]], 'labels': [-1, 4, -1, -1, 3], 'scores': [0.540050598815799, 1.0397395602684103, 1.4470510066547355, 1.7802953864767703, 2.0400304915738623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 7.0037031173706055})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 8.299266815185547})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 8.026833534240723})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.917766571044922})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 7.574367523193359})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 11.15754508972168})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 7.218715667724609})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2283, 'crossentropy': 7.3858625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.581125259399414})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.299713373184204})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.65958309173584})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.276724100112915})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.768453598022461})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.468609094619751})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 22291], ['ood', 66157], ['ood', 8714], ['ood', 47316], ['ood', 41380]], 'labels': [3, -1, -1, -1, -1], 'scores': [0.6755933083407903, 1.2681966942599965, 1.7521429196208325, 2.130542434063936, 2.4587737161850627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.954777717590332})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 7.88868522644043})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 8.299625396728516})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 8.322932243347168})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2428, 'crossentropy': 5.9801265625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.353245735168457})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.537818431854248})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.9578235149383545})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 6945], ['ood', 43055], ['id', 8033], ['id', 41251], ['id', 15124]], 'labels': [4, -1, 3, 3, 6], 'scores': [0.5468450973332009, 0.9651598060589279, 1.3172573115476087, 1.6189029242953863, 1.8489437583767634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.727737903594971})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.096826553344727})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 7.870776176452637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.673488616943359})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 7.093972206115723})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 9.360795974731445})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2207, 'crossentropy': 8.0334796875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 3.4234812259674072})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.417552947998047})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.6369152069091797})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.7296080589294434})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 23451], ['ood', 68040], ['ood', 44206], ['id', 24681], ['ood', 56124]], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.5366874307487679, 1.0444155758336404, 1.526523209067376, 1.9573136456292346, 2.303326141267766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.385622024536133})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.290709495544434})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.279995918273926})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 7.823539733886719})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 8.42250919342041})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 7.657155990600586})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 10.709061622619629})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2282, 'crossentropy': 8.1857578125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.5638537406921387})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.636634349822998})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.7417140007019043})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.853976249694824})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.195997714996338})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.051887512207031})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 58374], ['id', 16343], ['id', 7538], ['id', 15289], ['ood', 68382]], 'labels': [-1, 5, 4, 2, -1], 'scores': [0.6423705824491857, 1.135465109789391, 1.5906339606142272, 1.9578855368679466, 2.272261423374654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.712139129638672})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.336917877197266})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.484333515167236})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 7.088774681091309})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 7.737058162689209})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 7.107502460479736})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 8.39042854309082})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 8.862759590148926})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.130641460418701})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2464, 'crossentropy': 7.3004}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.9151039123535156})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.733992099761963})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.8449974060058594})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.4587819576263428})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.1329498291015625})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.3973031044006348})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.6215219497680664})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.613835334777832})
store['active_learning_steps'][11]['eval_training']['best_epoch']=7
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 55900], ['id', 12503], ['id', 42312], ['id', 26708], ['ood', 3071]], 'labels': [-1, 4, 4, 7, -1], 'scores': [0.6127910477775013, 1.1265017460224254, 1.6105510482966499, 2.0242177411218836, 2.3526984588514592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.0330915451049805})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.328108787536621})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.576206684112549})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 7.072927474975586})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 8.174072265625})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.6753435134887695})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.378075122833252})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2242, 'crossentropy': 7.040421875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.7011544704437256})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.789808750152588})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.4372506141662598})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.2372307777404785})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.7517471313476562})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.5968403816223145})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 63555], ['ood', 68612], ['ood', 25507], ['id', 34342], ['ood', 44144]], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.6687960545045163, 1.1623916490760149, 1.5560982616794314, 1.9141979744170214, 2.2340239986789023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 7.954923629760742})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.147282600402832})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 7.587508201599121})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.864299774169922})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.5001349449157715})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 9.172294616699219})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2213, 'crossentropy': 7.8631921875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.164669990539551})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.2601659297943115})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.137685775756836})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.376490592956543})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.760352611541748})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 61876], ['ood', 45576], ['ood', 14309], ['id', 9404], ['ood', 53454]], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.5516307905868323, 1.0785782406997626, 1.5005789035067676, 1.865884206674827, 2.1826406882180116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.4087934494018555})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 8.198020935058594})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.072268486022949})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 7.305060386657715})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 7.601737022399902})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.635810852050781})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2087, 'crossentropy': 7.02400390625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 3.8372225761413574})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.517124652862549})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.841660499572754})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.862886905670166})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 4.012363433837891})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 38614], ['id', 11535], ['id', 23800], ['id', 28196], ['ood', 575]], 'labels': [-1, 5, 4, 1, -1], 'scores': [0.5953445505185495, 1.063224282691942, 1.45503988508346, 1.8052092523765748, 2.1387908672199676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.249541282653809})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.926637649536133})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.047366142272949})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 7.347437381744385})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 8.31143569946289})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 10.528306007385254})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2407, 'crossentropy': 6.093191796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.1247682571411133})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.6984939575195312})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.3243751525878906})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.609433174133301})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.8112878799438477})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 67088], ['id', 25318], ['id', 13268], ['id', 9352], ['id', 3135]], 'labels': [-1, 3, 8, 8, 0], 'scores': [0.588790248453543, 1.0060526695475103, 1.3829741628243464, 1.7297391520350258, 2.037825817727577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.776918888092041})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.82680606842041})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.614234447479248})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.892236232757568})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 7.134596347808838})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.19950008392334})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.514102935791016})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 7.564883232116699})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2208, 'crossentropy': 6.992240625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.267512559890747})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.026122570037842})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.141712665557861})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.2959485054016113})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.5513248443603516})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 36532], ['id', 34064], ['ood', 6332], ['id', 44940], ['ood', 21938]], 'labels': [1, 2, -1, 2, -1], 'scores': [0.5005107576305349, 0.9542075816055959, 1.371882992415062, 1.7273639430772896, 2.0539969243040668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.8181915283203125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.996703624725342})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.500107765197754})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 8.279446601867676})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.838171005249023})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 7.0737504959106445})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2449, 'crossentropy': 6.508676171875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.436256170272827})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.5974745750427246})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.464700937271118})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.8128323554992676})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.760605573654175})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 33778], ['ood', 61904], ['id', 13154], ['id', 42515], ['id', 6192]], 'labels': [8, -1, 3, 0, 7], 'scores': [0.5426243635991884, 1.0806303879768198, 1.5462718831896032, 1.9340542570859718, 2.2716104264051884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.700122833251953})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.558724403381348})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 7.454787254333496})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 7.289355278015137})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.691461563110352})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2475, 'crossentropy': 5.7984953125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.4717488288879395})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.0125043392181396})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.929067611694336})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.3140244483947754})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 34956], ['ood', 64003], ['id', 36316], ['ood', 22247], ['ood', 60051]], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.5356820958721906, 0.9777072963620046, 1.3699626475107225, 1.7287476157340893, 2.020907473059906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.612317085266113})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 6.343145370483398})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 8.530223846435547})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 9.447465896606445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.340227127075195})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2448, 'crossentropy': 6.62828828125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.439120292663574})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.2739198207855225})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.2906670570373535})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.627748489379883})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 36955], ['ood', 25793], ['ood', 70810], ['id', 22794], ['id', 4867]], 'labels': [1, -1, -1, 9, 8], 'scores': [0.48478957225483676, 0.9203478113759491, 1.2850145906883919, 1.6085861411479128, 1.9037523999155619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.7767486572265625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.159017562866211})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 9.292888641357422})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 6.349922180175781})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 6.557468414306641})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 6.78026819229126})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 7.962817668914795})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 7.634078025817871})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2513, 'crossentropy': 6.74826953125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.2170798778533936})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.333580255508423})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.2311172485351562})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.5675697326660156})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.633871555328369})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.2857351303100586})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 34620], ['id', 24001], ['id', 37108], ['id', 22352], ['ood', 16342]], 'labels': [-1, 5, 2, 2, -1], 'scores': [0.7180699386431748, 1.2313383724649074, 1.6732572747362324, 2.062296610307684, 2.398695494132724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.187660217285156})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.516351222991943})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.126660346984863})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.789355278015137})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 6.259679794311523})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.314725875854492})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.261737823486328})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 9.177057266235352})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.236488342285156})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 7.366575241088867})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2677, 'crossentropy': 6.60395390625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.110900402069092})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.6341092586517334})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.9797208309173584})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.926076889038086})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.8925228118896484})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.2639694213867188})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.1501922607421875})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.173461437225342})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 32593], ['id', 11796], ['ood', 125], ['ood', 33171], ['ood', 7195]], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.6026425007500873, 1.125684770922072, 1.6266215311055119, 2.069430849479488, 2.4127805600143803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.15589714050293})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.1752424240112305})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 5.295948028564453})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.325344085693359})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 6.222536087036133})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.828417778015137})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 6.614917755126953})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 6.613450050354004})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 6.976241588592529})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2588, 'crossentropy': 5.924006640625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.763371467590332})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.788607120513916})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.688326358795166})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.5161514282226562})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.488497734069824})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 9223], ['id', 1740], ['ood', 677], ['id', 12023], ['ood', 1026]], 'labels': [-1, 8, -1, 9, -1], 'scores': [0.5239762634753586, 1.0238797649538176, 1.4326183871446228, 1.8139783224891701, 2.1584946545150565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.9895873069763184})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.749577045440674})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.468038558959961})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.471141338348389})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 6.903285503387451})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 6.836126327514648})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.329061985015869})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 8.886780738830566})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.897444725036621})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.450738430023193})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 6.195435523986816})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.689722061157227})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 7.656648635864258})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 6.865471363067627})
store['active_learning_steps'][23]['training']['best_epoch']=11
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2665, 'crossentropy': 6.480976953125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.70816707611084})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.745846748352051})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.8245816230773926})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.1567344665527344})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.8164620399475098})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.0567052364349365})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.6001317501068115})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.1043591499328613})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.326890707015991})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 32468], ['ood', 47659], ['id', 47175], ['id', 21043], ['ood', 26439]], 'labels': [-1, -1, 5, 1, -1], 'scores': [0.8072955553675782, 1.3046312329974987, 1.7236521106544185, 2.0928503220670045, 2.4165553441002476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.072393417358398})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.1257147789001465})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.400617599487305})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.482194900512695})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.3997955322265625})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.709895133972168})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2546, 'crossentropy': 5.77418828125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.6524829864501953})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.710824966430664})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.839541435241699})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.1291890144348145})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.969400644302368})
store['active_learning_steps'][24]['eval_training']['best_epoch']=2
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 34559], ['id', 22873], ['id', 17626], ['ood', 4313], ['id', 19543]], 'labels': [2, 1, 1, -1, 2], 'scores': [0.6190149780631713, 1.0788269332468459, 1.506502151873209, 1.9137556736571293, 2.1834079672157634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.077305793762207})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.621584892272949})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.363838195800781})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.652941703796387})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.194347381591797})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 7.18609619140625})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.775689125061035})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.593993186950684})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 5.498315334320068})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 6.626128673553467})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 7.185995101928711})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 8.570074081420898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 7.780194282531738})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 7.233445167541504})
store['active_learning_steps'][25]['training']['best_epoch']=11
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2541, 'crossentropy': 8.0434453125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.9760680198669434})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.8589882850646973})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.020050525665283})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 3.009143829345703})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.2528140544891357})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.2030439376831055})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.2395248413085938})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 38525], ['id', 24078], ['ood', 65664], ['ood', 58583], ['ood', 52479]], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.7082321014927525, 1.2517998638748709, 1.703564609233597, 2.1204596267175737, 2.492368918659489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.609393119812012})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.983242511749268})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.936011791229248})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.906599521636963})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 6.300668716430664})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.859418869018555})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.1684370040893555})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.264, 'crossentropy': 5.9799171875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.6271371841430664})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.7700726985931396})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.394660234451294})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.2473978996276855})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.240535020828247})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.5934317111968994})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 7966], ['ood', 67970], ['id', 20048], ['id', 12887], ['ood', 5994]], 'labels': [-1, -1, 8, 8, -1], 'scores': [0.7437907040734277, 1.2759075222041885, 1.759291605851537, 2.163278845855375, 2.494143760300234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.412484169006348})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.750546455383301})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.280550003051758})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.786205291748047})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 6.940569877624512})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.267158031463623})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.2826457023620605})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.160426139831543})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 6.728728294372559})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 6.860175132751465})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 8.229859352111816})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 6.548561096191406})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 6.540866374969482})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 7.282288551330566})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 7.441839218139648})
store['active_learning_steps'][27]['training']['best_epoch']=12
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2684, 'crossentropy': 6.870484375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.8427178859710693})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.2210469245910645})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.193209171295166})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 3.4174275398254395})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.1007277965545654})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.102010726928711})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.481255531311035})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.230903387069702})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.408663272857666})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.17639422416687})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.186554193496704})
store['active_learning_steps'][27]['eval_training']['best_epoch']=8
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 957], ['ood', 51257], ['id', 42499], ['ood', 34217], ['id', 31463]], 'labels': [7, -1, 1, -1, 1], 'scores': [0.6196891520631386, 1.1871843448416095, 1.690426963196105, 2.1412231868775793, 2.51943167876248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.197552680969238})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.048658847808838})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 7.317575454711914})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.296932220458984})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 6.012472152709961})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.828900337219238})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 8.717081069946289})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.778459548950195})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2625, 'crossentropy': 6.457148046875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 2.9327621459960938})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.1013095378875732})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.0337073802948})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.131472110748291})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.406379461288452})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.4721016883850098})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.1361899375915527})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 24748], ['ood', 65374], ['id', 16992], ['ood', 2863], ['ood', 26736]], 'labels': [1, -1, 4, -1, -1], 'scores': [0.657149028956743, 1.1773344337490608, 1.6393136710725553, 2.007165607525489, 2.320364909815372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.264598369598389})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.869224548339844})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 5.373293399810791})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.550630569458008})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.548576354980469})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.613254547119141})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.303827285766602})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 6.903304576873779})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 5.9917449951171875})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 8.251794815063477})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 7.754851341247559})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.323302745819092})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.261, 'crossentropy': 6.5913421875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.1815011501312256})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.6215219497680664})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.0046892166137695})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.8681399822235107})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.07332444190979})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.148013114929199})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.330843448638916})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.1505980491638184})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.264688730239868})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.6748876571655273})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.291625738143921})
store['active_learning_steps'][29]['eval_training']['best_epoch']=11
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 979], ['id', 25488], ['id', 42080], ['ood', 27363], ['id', 38204]], 'labels': [-1, 6, 5, -1, 8], 'scores': [0.6086667466350206, 1.1584460079142196, 1.644619335697664, 2.0764133660748723, 2.4331257303141625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.370036602020264})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.1433515548706055})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.410224914550781})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 6.231830596923828})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.752990245819092})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.493437767028809})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.554121017456055})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2569, 'crossentropy': 6.4787328125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.2652974128723145})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.901130199432373})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.1926231384277344})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.0800483226776123})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.0517048835754395})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.319544792175293})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 38815], ['ood', 43620], ['id', 24704], ['ood', 25683], ['ood', 37025]], 'labels': [4, -1, 1, -1, -1], 'scores': [0.6685577842290953, 1.2170531336328807, 1.733034014631187, 2.1079066447900736, 2.442070546182375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.2938098907470703})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.285402297973633})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.899050712585449})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 6.165989875793457})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.697707653045654})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.790142059326172})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2573, 'crossentropy': 6.5535234375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.2845253944396973})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.844428539276123})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.0495707988739014})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.111846685409546})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.6614646911621094})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 21169], ['ood', 13077], ['ood', 45932], ['ood', 9845], ['ood', 40221]], 'labels': [0, -1, -1, -1, -1], 'scores': [0.6391426705277163, 1.2370602549972944, 1.7014269976758807, 2.093758135954025, 2.4056587244862904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.566459655761719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.089629650115967})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.059791564941406})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.512576103210449})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 7.361852645874023})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.2405, 'crossentropy': 4.3392328125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.0534629821777344})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.005443811416626})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.8703672885894775})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.926860809326172})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 7925], ['ood', 15077], ['ood', 45431], ['id', 41885], ['ood', 61923]], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.4416047124793163, 0.7660620792882593, 1.0828057206373303, 1.3760501123144664, 1.6426761641077707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.571213722229004})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.803150177001953})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.139684200286865})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.598592758178711})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 5.549777030944824})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.282351016998291})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 6.28774881362915})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 6.237279891967773})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2497, 'crossentropy': 5.835025390625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.1848270893096924})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.7912213802337646})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.245063543319702})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.9150047302246094})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.0599136352539062})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.6624698638916016})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.933572769165039})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 19818], ['id', 40217], ['ood', 19899], ['id', 12199], ['ood', 40968]], 'labels': [1, 3, -1, 7, -1], 'scores': [0.4716430740400625, 0.9186182016950255, 1.349980384375916, 1.7136701893700614, 1.999712416904301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.9839932918548584})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 5.079981803894043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.2553510665893555})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.827298641204834})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.523109436035156})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2628, 'crossentropy': 5.39632421875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 2.9204206466674805})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.2397563457489014})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.9120025634765625})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 3.032597541809082})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 71221], ['ood', 16777], ['id', 28501], ['ood', 6298], ['id', 31308]], 'labels': [-1, -1, 9, -1, 0], 'scores': [0.5683148241118343, 1.0104829789729395, 1.3876313597863463, 1.7097394547358693, 2.007990496887053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.901512622833252})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.766350746154785})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.815532207489014})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.673001289367676})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 5.042181491851807})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2724, 'crossentropy': 5.03356328125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.9557814598083496})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.385031223297119})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.326812744140625})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.1445064544677734})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 49918], ['ood', 49891], ['id', 29414], ['id', 12492], ['id', 12413]], 'labels': [-1, -1, 8, 9, 0], 'scores': [0.4902538562403913, 0.9512510021859724, 1.358529223685724, 1.7406979486879957, 2.0510557986412783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.93013334274292})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.35033655166626})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.130696773529053})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.6411895751953125})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 5.34533166885376})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 6.827897071838379})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 6.068816184997559})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.603998184204102})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.255, 'crossentropy': 5.6049703125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.4150876998901367})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.903689384460449})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.6828036308288574})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.0920400619506836})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.7522573471069336})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 3.0586435794830322})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.688026189804077})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 2172], ['id', 12256], ['ood', 68186], ['ood', 31036], ['id', 10880]], 'labels': [8, 2, -1, -1, 1], 'scores': [0.6452229806995646, 1.0752251904790584, 1.4606316406072852, 1.7951338183332055, 2.062730340757795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.537703514099121})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.426156997680664})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.610443115234375})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.357363700866699})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.204226016998291})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.950016498565674})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.852727890014648})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.886932373046875})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 6.565800666809082})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.85960578918457})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 7.122377395629883})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 7.541252136230469})
store['active_learning_steps'][37]['training']['best_epoch']=9
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.25, 'crossentropy': 6.83696796875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.0530693531036377})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 2.8357696533203125})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.9081645011901855})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.272364854812622})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.2744340896606445})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.3417861461639404})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 16708], ['ood', 1080], ['ood', 1045], ['ood', 5786], ['ood', 8197]], 'labels': [6, -1, -1, -1, -1], 'scores': [0.8640360050564796, 1.4909711160695691, 2.0256453320812575, 2.3976085711464563, 2.7264956739012156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.187889337539673})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.5919456481933594})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.851351737976074})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.678069114685059})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.867020130157471})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.2383, 'crossentropy': 3.74745703125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.7715046405792236})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.6009511947631836})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.5428261756896973})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.7115750312805176})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 45158], ['id', 37207], ['id', 20564], ['ood', 11692], ['id', 29978]], 'labels': [-1, 7, 8, -1, 9], 'scores': [0.3261657438584685, 0.6237085626009007, 0.8641131094536476, 1.0905021828958423, 1.303889606219717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.1106133460998535})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.4802398681640625})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.778318405151367})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.949890613555908})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.747511386871338})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.6461310386657715})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.5657958984375})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.426543235778809})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.262, 'crossentropy': 5.95023984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.3192434310913086})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.4033708572387695})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.3154563903808594})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.255075216293335})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.632333517074585})
store['active_learning_steps'][39]['eval_training']['best_epoch']=2
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 15188], ['ood', 11118], ['ood', 69185], ['id', 48934], ['ood', 1451]], 'labels': [5, -1, -1, 2, -1], 'scores': [0.4463364666362588, 0.8424155486863927, 1.2213797509852569, 1.5696296068016098, 1.872877347840899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.430300235748291})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.409313201904297})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.8800764083862305})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.6763129234313965})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.744724750518799})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.662184715270996})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.459178924560547})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 6.372182846069336})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 6.712326526641846})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 7.606183052062988})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2789, 'crossentropy': 5.8853828125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.8989334106445312})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.9541373252868652})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.9102110862731934})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.0243022441864014})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.280641794204712})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.2788047790527344})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 2.862387180328369})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.3545775413513184})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.257741689682007})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 26313], ['ood', 62815], ['id', 368], ['id', 16355], ['ood', 61827]], 'labels': [0, -1, 0, 4, -1], 'scores': [0.5058054237355843, 0.9748204828157201, 1.4035538437375852, 1.7914749082961654, 2.131806881064553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.800874710083008})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.1616010665893555})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.553038597106934})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.097105026245117})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.531896591186523})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 6.346695899963379})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 6.477537155151367})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.2681, 'crossentropy': 5.142858203125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 2.818920612335205})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 2.6830573081970215})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.659479856491089})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.888719081878662})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.8680648803710938})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.306720495223999})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 26961], ['ood', 33447], ['ood', 61827], ['ood', 67311], ['id', 48074]], 'labels': [9, -1, -1, -1, 0], 'scores': [0.4687741279285828, 0.8943514667014489, 1.260767803861317, 1.5849716776227134, 1.870268647375065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.798640727996826})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.359962463378906})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.140033721923828})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.668155670166016})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.830264568328857})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.924736022949219})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 8.260184288024902})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 7.115997314453125})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 6.00958251953125})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.890986442565918})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 6.314493179321289})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 6.9357194900512695})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 6.4827775955200195})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 7.577408790588379})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 6.709375381469727})
store['active_learning_steps'][42]['training']['best_epoch']=12
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.2678, 'crossentropy': 7.18056171875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 2.8257617950439453})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.4803292751312256})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.2644567489624023})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 3.145859479904175})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.462339401245117})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.293879985809326})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.1050524711608887})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.384629964828491})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.5100696086883545})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.4094181060791016})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 20285], ['ood', 49454], ['id', 30813], ['id', 1432], ['id', 43802]], 'labels': [-1, -1, 2, 1, 7], 'scores': [0.606846381554601, 1.1135870110270756, 1.5419522383865392, 1.9280962133771355, 2.255794675095925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.074742317199707})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.5427796840667725})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.3632659912109375})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 5.052842617034912})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.887628555297852})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.301589012145996})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 6.428082466125488})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.2796, 'crossentropy': 5.103744140625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.62052583694458})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.951385498046875})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 2.694819450378418})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 2.931428909301758})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.9502506256103516})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 3.2385659217834473})
store['active_learning_steps'][43]['eval_training']['best_epoch']=4
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 8023], ['id', 27290], ['ood', 61668], ['id', 35273], ['id', 5252]], 'labels': [-1, 6, -1, 9, 7], 'scores': [0.5000082443216054, 0.9535724054772432, 1.332247588959449, 1.6661354674105189, 1.9763342067854817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.701012372970581})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.258305549621582})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.797466278076172})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.517110824584961})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.916245937347412})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 6.589543342590332})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.067286491394043})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.2676, 'crossentropy': 5.88600390625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.9685606956481934})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 3.093679904937744})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.7846503257751465})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.302574634552002})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.8686041831970215})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.516089916229248})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 68391], ['ood', 2785], ['id', 39513], ['ood', 61129], ['id', 13588]], 'labels': [-1, -1, 0, -1, 8], 'scores': [0.5667469749485354, 0.9904517867059195, 1.386300125400008, 1.7444092512960845, 2.0384530622559334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.8941659927368164})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.9292097091674805})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.441644668579102})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.402130126953125})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.9698991775512695})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.626965522766113})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 6.822841644287109})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 5.140751838684082})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.9118499755859375})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 6.863315582275391})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 7.098605632781982})
store['active_learning_steps'][45]['training']['best_epoch']=8
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.2911, 'crossentropy': 5.31458984375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.2050793170928955})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.904071569442749})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.847869634628296})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.9187231063842773})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 2.7616114616394043})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.732665538787842})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.772230386734009})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 2.6974639892578125})
store['active_learning_steps'][45]['eval_training']['best_epoch']=5
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 59081], ['ood', 18139], ['id', 18599], ['id', 48921], ['ood', 67794]], 'labels': [-1, -1, 1, 9, -1], 'scores': [0.6139541517773598, 1.1434048295323547, 1.5949615553672247, 1.9835668913794962, 2.3004584703703284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.117302894592285})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.857119560241699})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.446384906768799})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.535284996032715})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 5.6479573249816895})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.353521823883057})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 5.7722578048706055})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.5890421867370605})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 5.493958950042725})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 6.593558311462402})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.2793, 'crossentropy': 5.7589578125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 2.5449299812316895})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.721224308013916})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.951176881790161})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.862455129623413})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.783224105834961})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.138350248336792})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.944765567779541})
store['active_learning_steps'][46]['eval_training']['best_epoch']=4
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 34443], ['ood', 30567], ['ood', 46214], ['ood', 48197], ['ood', 53454]], 'labels': [4, -1, -1, -1, -1], 'scores': [0.6255507002722327, 1.137015091009332, 1.5561702014879928, 1.9308156545395914, 2.2536799596731516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.9689955711364746})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.5315093994140625})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.323924541473389})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 4.954014778137207})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.466701984405518})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.572368621826172})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.703986167907715})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.2732, 'crossentropy': 5.111466796875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.1568984985351562})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.6697447299957275})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.7952632904052734})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.8222479820251465})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.9165050983428955})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.1370038986206055})
store['active_learning_steps'][47]['eval_training']['best_epoch']=4
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 64071], ['ood', 9234], ['ood', 24038], ['id', 48184], ['id', 3687]], 'labels': [-1, -1, -1, 3, 3], 'scores': [0.488751541677825, 0.9409671397137388, 1.3410987060884316, 1.7190495452367491, 2.059993981355011]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.849142551422119})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.9166955947875977})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.613372802734375})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.1698126792907715})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.224448204040527})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.2504, 'crossentropy': 3.9132265625}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 2.5806124210357666})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.741755485534668})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.701054334640503})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.759812116622925})
store['active_learning_steps'][48]['eval_training']['best_epoch']=4
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 29722], ['ood', 46598], ['id', 41735], ['ood', 41356], ['id', 20252]], 'labels': [6, -1, 9, -1, 1], 'scores': [0.3254446491025048, 0.6390944728225885, 0.8978644482784137, 1.1291858165624022, 1.315353210192832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 4.047285556793213})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.764799118041992})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.962890625})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.206927299499512})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.576279640197754})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.180484771728516})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 5.2746477127075195})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.993302345275879})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.2667, 'crossentropy': 5.78102421875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.033914566040039})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.824810028076172})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.8441102504730225})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.966531276702881})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.7672266960144043})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.918931007385254})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 3.1098403930664062})
store['active_learning_steps'][49]['eval_training']['best_epoch']=6
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 62511], ['ood', 67678], ['ood', 13391], ['ood', 10229], ['id', 1542]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.5805045472070016, 1.1141998626967533, 1.5057042491123322, 1.8703157525967695, 2.1759742815971252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.019920349121094})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.131500244140625})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.294175386428833})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.948098182678223})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.662546157836914})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 6.399167537689209})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.673123359680176})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 6.167074203491211})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.509431838989258})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 7.664166450500488})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 6.461933135986328})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 8.044848442077637})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 6.628475666046143})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.853933334350586})
store['active_learning_steps'][50]['training']['best_epoch']=11
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.294, 'crossentropy': 6.348851171875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.674642562866211})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.6989474296569824})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.8406286239624023})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.835387945175171})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 2.9322447776794434})
store['active_learning_steps'][50]['eval_training']['best_epoch']=2
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 27836], ['ood', 31566], ['id', 14425], ['ood', 59323], ['id', 3723]], 'labels': [0, -1, 5, -1, 4], 'scores': [0.6638586858238273, 1.170057385734086, 1.6463223832695575, 2.0413793870585186, 2.384494173608811]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.3383877277374268})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.343636512756348})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 4.721960544586182})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.790737152099609})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.462568283081055})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 5.400965213775635})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 6.012838363647461})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.398797035217285})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 6.108988285064697})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.3052, 'crossentropy': 5.327837890625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.832332134246826})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.529054641723633})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.578709602355957})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.786862850189209})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 2.4544241428375244})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.852301597595215})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.0012130737304688})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.912571907043457})
store['active_learning_steps'][51]['eval_training']['best_epoch']=5
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 35023], ['ood', 23070], ['id', 22508], ['ood', 22013], ['id', 20476]], 'labels': [-1, -1, 9, -1, 1], 'scores': [0.5808349051171999, 1.0219001685796343, 1.4330685692544898, 1.7921729920489646, 2.1241580482371702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.0740532875061035})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.9508228302001953})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.667351722717285})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.874267578125})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.545771598815918})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.2617, 'crossentropy': 4.056490234375}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.557889699935913})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.3916988372802734})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.717006206512451})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.853990077972412})
store['active_learning_steps'][52]['eval_training']['best_epoch']=3
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 47408], ['id', 15697], ['ood', 35714], ['ood', 4859], ['ood', 38614]], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.545452616504696, 0.9101457078582075, 1.2021920874665288, 1.4616567762489807, 1.6986406205704676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.7841413021087646})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.151715278625488})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.879428863525391})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.230146408081055})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 6.23123836517334})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.460721492767334})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.774575233459473})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 6.1391401290893555})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 6.120511531829834})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 7.134969234466553})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 6.470847129821777})
store['active_learning_steps'][53]['training']['best_epoch']=8
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.2744, 'crossentropy': 6.377939453125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.7844552993774414})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.812234401702881})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.7288260459899902})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.0830307006835938})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.915482997894287})
store['active_learning_steps'][53]['eval_training']['best_epoch']=2
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 36281], ['id', 16082], ['ood', 66814], ['ood', 47582], ['ood', 61156]], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.5547762530640759, 1.0359172916378676, 1.4420550961600767, 1.8260871423644236, 2.139501304990885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.374295711517334})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.112386703491211})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.850690841674805})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.974559783935547})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.846793174743652})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.778561592102051})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 6.785194396972656})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.061858177185059})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.080549240112305})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.2763, 'crossentropy': 5.747309765625}
