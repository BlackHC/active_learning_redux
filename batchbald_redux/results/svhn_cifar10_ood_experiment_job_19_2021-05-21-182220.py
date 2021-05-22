store = {}
store['timestamp']=1621617740
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=19']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=19
store['worker_id']=19
store['num_workers']=24
store['config']={'seed': 1255, 'uniform_ood': False, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 12.271987915039062})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.08984375, 'crossentropy': 8.774750709533691})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 9.9423828125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1064453125, 'crossentropy': 9.939631462097168})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.11059465273509526, 'crossentropy': 12.925024969268593}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 5.731122016906738})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 5.333237648010254})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 5.782449722290039})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 30494], ['id', 47965], ['ood', 23158], ['id', 26097], ['id', 4831]], 'labels': [0, 1, -1, 7, 8], 'scores': [0.6501198936365933, 1.2130424738643582, 1.713622719392605, 2.1190519194068513, 2.446965213934682]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 9.166430473327637})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 8.531726837158203})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 9.16065502166748})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 9.168299674987793})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 10.618571281433105})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.091796875, 'crossentropy': 11.330974578857422})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 9.430212020874023})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.10759834050399508, 'crossentropy': 9.210303064497541}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 5.008937358856201})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 4.681571960449219})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 5.647217750549316})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 4.919336318969727})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 5.391470432281494})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 5.065308570861816})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 35859], ['ood', 16218], ['id', 71883], ['id', 24819], ['id', 71401]], 'labels': [7, -1, 1, 7, 8], 'scores': [0.604231494761489, 1.1186153312349902, 1.5893987929410476, 1.9838053998405663, 2.2828179318007797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 8.782241821289062})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 16.193145751953125})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 12.867403984069824})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 9.920982360839844})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 9.967498779296875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 10.268324851989746})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 8.711160659790039})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 9.857221603393555})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 9.883874893188477})
store['active_learning_steps'][2]['training']['best_epoch']=6
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.13936693300553166, 'crossentropy': 10.784453989320836}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 3.713533401489258})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.324995040893555})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 4.3270263671875})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 4.443325996398926})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 4.853110313415527})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 4.799267768859863})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 5.106624603271484})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 5.576238632202148})
store['active_learning_steps'][2]['eval_training']['best_epoch']=5
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 32450], ['id', 0], ['id', 1], ['id', 2], ['id', 3]], 'labels': [6, 2, 3, 0, 6], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 7.518353462219238})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 6.583573341369629})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 8.50790023803711})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 8.291531562805176})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 8.125513076782227})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.11520436385986478, 'crossentropy': 6.262308168792256}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 4.467447757720947})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 4.049397945404053})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 4.039520263671875})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 4.075070381164551})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 63603], ['id', 66940], ['id', 29833], ['id', 14613], ['id', 1835]], 'labels': [0, 6, 1, 9, 1], 'scores': [0.496786460331672, 0.9330219851696713, 1.3439254566170766, 1.6946540790886973, 2.0111203106831885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 7.82539701461792})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 8.491308212280273})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 7.019092082977295})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 7.551021575927734})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 7.625885963439941})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 7.698647499084473})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 8.101001739501953})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.11881530424093424, 'crossentropy': 7.192337795789797}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 4.117095470428467})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 3.9553709030151367})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 4.463232040405273})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 4.08361291885376})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 34987], ['id', 42595], ['id', 68855], ['id', 24213], ['ood', 24118]], 'labels': [1, 3, 8, 1, -1], 'scores': [0.61834110640053, 1.0733248422654271, 1.4930259669167785, 1.8547000909994207, 2.1795550583505268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 6.876008033752441})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 6.865448951721191})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 7.048705101013184})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 7.457282066345215})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 7.66062068939209})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1064453125, 'crossentropy': 7.976985931396484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 7.802028656005859})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.12749692685925015, 'crossentropy': 7.296977037876459}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 4.079030990600586})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.09375, 'crossentropy': 4.276735305786133})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 4.715279579162598})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 4.619349479675293})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 13223], ['id', 70673], ['ood', 722], ['id', 969], ['id', 8208]], 'labels': [-1, 6, -1, 0, 5], 'scores': [0.4869639651962825, 0.9036397970983145, 1.30653476390155, 1.6458864726252198, 1.9416202797864708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 7.708646774291992})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 8.22590446472168})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 9.275493621826172})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 8.083553314208984})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 7.179198265075684})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 8.06016731262207})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.14555162876459743, 'crossentropy': 9.192252564151813}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 4.168497085571289})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 4.300357341766357})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 5.44758415222168})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 4.857887268066406})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 5.138968467712402})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 13140], ['id', 13560], ['id', 61880], ['id', 62662], ['id', 43512]], 'labels': [1, 3, 8, 2, 8], 'scores': [0.7319226529192142, 1.308319491530673, 1.7929998180628586, 2.2125067035091006, 2.5936030760947952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 7.1024017333984375})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 6.42702054977417})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 6.70334529876709})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 8.186162948608398})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 9.183664321899414})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 7.002408027648926})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 7.375883102416992})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.13921327596803934, 'crossentropy': 7.83326530808236}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 3.9251022338867188})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 4.588919639587402})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 4.112648010253906})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 4.390999794006348})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 4.442328453063965})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 4.688785552978516})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 20423], ['id', 70880], ['id', 31394], ['id', 3161], ['ood', 32569]], 'labels': [1, 5, 0, 5, -1], 'scores': [0.6504926250953094, 1.196041252585892, 1.6853194414497341, 2.1091118408808365, 2.475870749896952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 6.357275009155273})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 7.027987480163574})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 7.3779144287109375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 7.705822467803955})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 8.062488555908203})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.11996773202212661, 'crossentropy': 6.826873535456361}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 3.7191381454467773})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 4.146331787109375})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 4.205729961395264})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 4.638694763183594})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 19704], ['id', 54545], ['id', 12916], ['id', 18807], ['id', 13266]], 'labels': [1, 9, 8, 2, 1], 'scores': [0.5473053681415367, 0.9685963285611261, 1.3601718457327845, 1.7010335733944792, 2.00473978316535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 6.954636573791504})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 7.269903659820557})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 7.090510845184326})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 8.168607711791992})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 8.152423858642578})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.12880301167793484, 'crossentropy': 7.08951302723571}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 3.9854726791381836})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 4.037425994873047})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.163207054138184})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 4.515211582183838})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 1790], ['id', 62128], ['id', 16702], ['id', 59112], ['id', 26230]], 'labels': [1, 9, 8, 9, 3], 'scores': [0.5521709767004926, 1.0294704773328882, 1.4450437270267649, 1.818912579282389, 2.134529005022648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.718158721923828})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 5.933598518371582})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 6.457152843475342})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.915288925170898})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 7.839598655700684})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 7.723919868469238})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 7.729907989501953})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.631062984466553})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 6.528836727142334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.6420745849609375})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.808767318725586})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.14082667486170866, 'crossentropy': 5.630094090926552}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 2.8389394283294678})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.1944901943206787})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.330313205718994})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 3.5775349140167236})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.37797212600708})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 61688], ['id', 68687], ['id', 11427], ['id', 48119], ['id', 12442]], 'labels': [6, 3, 8, 0, 2], 'scores': [0.5007388748014447, 0.9474771957619368, 1.3658859255485702, 1.7540440554267418, 2.0961516134859672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.321554183959961})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.726184844970703})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 6.731819152832031})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 7.557229042053223})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.14267055931161648, 'crossentropy': 6.052748180124462}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.413545608520508})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.775580406188965})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 4.2031731605529785})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 65679], ['id', 52129], ['id', 45529], ['id', 28286], ['id', 39563]], 'labels': [2, 5, 0, 1, 9], 'scores': [0.5048500822121089, 0.9386086003286389, 1.3120933508745547, 1.6344715562027918, 1.926962673600766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 6.82023811340332})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 6.564387798309326})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 6.882514476776123})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 7.915591716766357})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 7.460603713989258})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.770233154296875})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 7.493461608886719})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.12788106945298094, 'crossentropy': 7.866024868431162}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 3.6810050010681152})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 3.765188217163086})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 4.241973876953125})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 4.238559722900391})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 4.517278671264648})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 4.241103172302246})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 34029], ['id', 41245], ['id', 68256], ['id', 40221], ['id', 29452]], 'labels': [0, 4, 2, 0, 8], 'scores': [0.5406305457577926, 1.0423412369110183, 1.4894573129931163, 1.89824003691218, 2.2507397718503253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 4.997215270996094})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.616765022277832})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 7.339332103729248})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.324220657348633})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.1550783650891211, 'crossentropy': 4.936560651313767}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 3.6986167430877686})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 3.76688289642334})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 3.8510818481445312})
store['active_learning_steps'][13]['eval_training']['best_epoch']=1
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 54965], ['id', 8032], ['id', 66465], ['id', 57922], ['id', 16841]], 'labels': [8, 6, 0, 1, 1], 'scores': [0.45996334657664084, 0.8294807667111237, 1.1661787597222002, 1.4630655505557657, 1.7425883118797527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.196646690368652})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.134369850158691})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.2796430587768555})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.954439163208008})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.14086508912108175, 'crossentropy': 6.339231522741241}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 3.636746883392334})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.9263057708740234})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 3.750999927520752})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 13362], ['id', 30043], ['id', 68048], ['id', 15352], ['id', 5502]], 'labels': [1, 3, 3, 1, 1], 'scores': [0.5854703474615378, 1.0535250675744012, 1.4566930032051384, 1.8214697012676542, 2.1091079570222537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.316244125366211})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 6.556752681732178})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 7.390658378601074})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 6.392814636230469})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 6.719162940979004})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 5.892020225524902})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.684734344482422})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.14701137062077443, 'crossentropy': 6.340322127573756}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.264026641845703})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.819147109985352})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.3701677322387695})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 4.296606540679932})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 3.9916577339172363})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 70822], ['id', 45311], ['id', 55041], ['id', 58815], ['id', 701]], 'labels': [7, 5, 1, 6, 8], 'scores': [0.5180312220459646, 0.9715022915788871, 1.3924290697813302, 1.7629188168544279, 2.0826661647079945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.136658191680908})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 7.394573211669922})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 6.647289276123047})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 7.514322757720947})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.1357559926244622, 'crossentropy': 6.063788678357406}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 4.75611686706543})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 4.281233310699463})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 4.04224157333374})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 41878], ['id', 32384], ['id', 2291], ['id', 16919], ['id', 35589]], 'labels': [-1, 9, 1, 1, 3], 'scores': [0.5674356058960602, 0.9662805285317255, 1.3510211191444466, 1.6951385719917456, 2.0142527884200065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.761012077331543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.774980068206787})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.283118724822998})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 7.029562950134277})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.737030982971191})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.950868606567383})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.16748617086662568, 'crossentropy': 5.438663231791641}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.175508975982666})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 3.2806901931762695})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.394160270690918})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 3.50903058052063})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.5010242462158203})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 39550], ['id', 53088], ['id', 24076], ['id', 63076], ['ood', 2806]], 'labels': [1, 1, 5, 1, -1], 'scores': [0.5458005824207158, 1.040612335307919, 1.433696469418645, 1.7664285880283674, 2.0780934840281384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.658097267150879})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 4.7668657302856445})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.78128719329834})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 7.120119094848633})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.158420405654579, 'crossentropy': 7.212905030347265}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 3.9763143062591553})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 3.9012229442596436})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 3.783639907836914})
store['active_learning_steps'][18]['eval_training']['best_epoch']=1
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 46380], ['id', 61945], ['ood', 45494], ['ood', 21403], ['id', 57968]], 'labels': [3, 1, -1, -1, 9], 'scores': [0.7241176243699333, 1.3066918496377444, 1.75717869215873, 2.075899435251482, 2.337885447397432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.706090450286865})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.731242656707764})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.293310165405273})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.354433059692383})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.668909549713135})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.526294708251953})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 7.323441028594971})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.636236190795898})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.1954517516902274, 'crossentropy': 5.672173910955747}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.428366184234619})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.400087594985962})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.6607823371887207})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.6582279205322266})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.5698094367980957})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.601318836212158})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.741649866104126})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 13223], ['id', 4], ['id', 5], ['id', 6], ['id', 7]], 'labels': [-1, 9, 1, 2, 2], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.945929527282715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.8362531661987305})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.129956245422363})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.2967681884765625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 7.542985916137695})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 7.519454002380371})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.248703956604004})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.15534726490473263, 'crossentropy': 6.765322487707437}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 3.004014253616333})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.7229087352752686})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.1474151611328125})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.7432661056518555})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.859452247619629})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.040223121643066})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 5386], ['id', 22342], ['id', 17358], ['ood', 26630], ['id', 29575]], 'labels': [-1, 2, 2, -1, 5], 'scores': [0.5388430575851262, 1.020674439651601, 1.4249566051616065, 1.8067552289907356, 2.138274358838445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.125059127807617})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.017571449279785})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.124161720275879})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.0342607498168945})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.561881065368652})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.1684081130915796, 'crossentropy': 5.96819299323909}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.2834572792053223})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.218276023864746})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 3.7180185317993164})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 3.829702854156494})
store['active_learning_steps'][21]['eval_training']['best_epoch']=2
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 62723], ['id', 18332], ['id', 18465], ['id', 852], ['id', 52980]], 'labels': [3, 0, 2, 2, 1], 'scores': [0.42845173341193865, 0.8095467718803429, 1.1525002613275586, 1.4588573414541237, 1.7265797963518263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 5.267285346984863})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 7.414016246795654})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.609503746032715})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 7.9103240966796875})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.0170698165893555})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.18112323294406885, 'crossentropy': 7.008338295175169}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.2607011795043945})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.268893241882324})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 4.5009765625})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 4.277068138122559})
store['active_learning_steps'][22]['eval_training']['best_epoch']=1
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 13248], ['id', 27716], ['id', 30996], ['id', 70524], ['id', 67798]], 'labels': [1, 4, 5, 0, 0], 'scores': [0.6847354143723, 1.1038782163676533, 1.48965959406371, 1.8292032420717215, 2.1281678361118086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.49364709854126})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.7000017166137695})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.875783920288086})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.598655700683594})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.18150737553779964, 'crossentropy': 5.451309926244622}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.409235954284668})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.5632357597351074})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.7207343578338623})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 4266], ['id', 63182], ['id', 23909], ['id', 30085], ['id', 29369]], 'labels': [0, 9, 1, 4, 1], 'scores': [0.4674626046452077, 0.9057099998383092, 1.286049369878182, 1.6210854661233811, 1.9098850732295927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 5.087873935699463})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.86501407623291})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.511037826538086})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.023074150085449})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.167915344238281})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.659844398498535})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.697614669799805})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.17732022126613398, 'crossentropy': 5.921588093500307}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 2.883358955383301})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.2605695724487305})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.7067346572875977})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.7082483768463135})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.5013608932495117})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.637787103652954})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 58370], ['id', 40742], ['id', 70906], ['id', 13714], ['id', 9138]], 'labels': [8, 0, 2, 6, 5], 'scores': [0.5081409419313365, 0.998306882104895, 1.4620387207070555, 1.8487124424215233, 2.1984991781691026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 4.843682289123535})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.779414653778076})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.62928581237793})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.1047749519348145})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.464677810668945})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.82999324798584})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.6266093254089355})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.28730583190918})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.34885311126709})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.20198217578365088, 'crossentropy': 5.872882413952059}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 3.0525808334350586})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.164668560028076})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.429069995880127})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.229739189147949})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.4018301963806152})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.3161678314208984})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.3241372108459473})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.1870672702789307})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 59252], ['id', 56938], ['id', 4560], ['id', 41950], ['id', 42497]], 'labels': [5, 8, 1, 9, 1], 'scores': [0.5207916301997177, 0.9847550504106559, 1.413525526787148, 1.816394582825183, 2.154215866934094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.073269844055176})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.1044769287109375})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.070244789123535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.99407958984375})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.20186693300553166, 'crossentropy': 4.8869654415719115}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.271699905395508})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.5380520820617676})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.387603282928467})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 29267], ['id', 13454], ['id', 44619], ['id', 70990], ['id', 61287]], 'labels': [8, 1, 8, 0, 1], 'scores': [0.5032817188261975, 0.9137412561027342, 1.25916541783653, 1.565096114536166, 1.8367088024036327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.84122371673584})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.348818778991699})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.5343828201293945})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.575433731079102})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.042864799499512})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.390799522399902})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.469222068786621})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.305017471313477})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.20889674247080517, 'crossentropy': 6.117260126959128}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.1156318187713623})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.644702672958374})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.6440939903259277})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.5723581314086914})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.7042949199676514})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.6236562728881836})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.702125072479248})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 58485], ['id', 21286], ['id', 5415], ['id', 59810], ['id', 68104]], 'labels': [0, 2, 2, 3, 1], 'scores': [0.5240871122150377, 0.9761649240722181, 1.3938520320650434, 1.7570855246680894, 2.0723490000763305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 4.253445625305176})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.531859397888184})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.461828231811523})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.280893325805664})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.22474479675293})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.911843299865723})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.998364448547363})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.383173942565918})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.233944416046143})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.646829605102539})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.004343032836914})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.8018903732299805})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.964756011962891})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.092232704162598})
store['active_learning_steps'][28]['training']['best_epoch']=11
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.19168715427166563, 'crossentropy': 5.69881480005378}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.343134880065918})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 3.3338112831115723})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 3.6354517936706543})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.663550615310669})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.489711046218872})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.2938413619995117})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.478619337081909})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 5993], ['ood', 11835], ['id', 54165], ['id', 14225], ['id', 47522]], 'labels': [4, -1, 6, 7, 6], 'scores': [0.5165367724250913, 0.9840885612573604, 1.4092603839337166, 1.767652279650552, 2.0920725828463116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.494479656219482})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.734858512878418})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.047774791717529})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.681451797485352})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.110532760620117})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.911225318908691})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.812963485717773})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.334813117980957})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.769660949707031})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.21930700676090964, 'crossentropy': 5.106402696681008}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 2.8890504837036133})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.999800205230713})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.132660388946533})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.320711135864258})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.2085258960723877})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 2.9411392211914062})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.0867819786071777})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.040163993835449})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 10560], ['ood', 36444], ['id', 30868], ['id', 71761], ['id', 55031]], 'labels': [4, -1, 1, 5, 6], 'scores': [0.5141578647013947, 1.010233439811079, 1.4557211262140235, 1.850829285752507, 2.1986668506074283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 4.968963623046875})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.467530250549316})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.636111736297607})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.680191993713379})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.520027160644531})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2002919483712354, 'crossentropy': 5.339704498309772}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.2726030349731445})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.2688612937927246})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.222733497619629})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.1342530250549316})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 19658], ['id', 28602], ['id', 54386], ['id', 27110], ['id', 56957]], 'labels': [-1, 8, 6, 3, 9], 'scores': [0.5198536396403485, 0.920655394860707, 1.2742367869287528, 1.5759694779664324, 1.8582228684055089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 4.9678544998168945})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.5187458992004395})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.367132663726807})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.853957176208496})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.439788818359375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.4484076499938965})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.20540104486785496, 'crossentropy': 5.088981229832513}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.351844072341919})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.1913435459136963})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.206362724304199})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.856315851211548})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.547703266143799})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 54194], ['id', 63236], ['id', 29579], ['id', 14199], ['id', 42950]], 'labels': [6, 1, 9, 0, 5], 'scores': [0.4940412268598262, 0.9178264214204943, 1.2815149683855402, 1.6159787968309907, 1.9066681387415478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.014251232147217})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.049144744873047})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.52960205078125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.951006889343262})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.23701810836792})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.1943377381684081, 'crossentropy': 5.439232843231408}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.3742430210113525})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.083806991577148})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.430328369140625})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.626476764678955})
store['active_learning_steps'][32]['eval_training']['best_epoch']=2
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 2967], ['id', 14259], ['ood', 25843], ['id', 51814], ['ood', 37757]], 'labels': [7, 1, -1, 0, -1], 'scores': [0.4296370852711656, 0.831718478313034, 1.2160200932685763, 1.5309065910426845, 1.8102862827854294]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.205373764038086})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.202200889587402})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.135127067565918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.465615272521973})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.220825672149658})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.138775825500488})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.29919958114624})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 4.962115287780762})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.18822987092808852, 'crossentropy': 5.159542822295636}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 2.900834560394287})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.1887271404266357})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.205660581588745})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.204195022583008})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.183088541030884})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.4888737201690674})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.2059550285339355})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 8355], ['ood', 37379], ['id', 59078], ['ood', 42507], ['id', 69964]], 'labels': [1, -1, 4, -1, 3], 'scores': [0.49427052208842825, 0.9559217340500314, 1.3583917879257728, 1.6913405942469462, 1.9962802362058367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 4.3438401222229})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.177833557128906})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.031240940093994})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.106878280639648})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.923609256744385})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 4.993111610412598})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.232955455780029})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.19403042409342347, 'crossentropy': 5.157425236247695}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 3.2029573917388916})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.7937464714050293})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.119673728942871})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 3.438788414001465})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.640766143798828})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.3554413318634033})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 5487], ['ood', 11479], ['id', 44674], ['id', 5171], ['id', 2218]], 'labels': [5, -1, 6, 2, 4], 'scores': [0.5654073680800105, 1.0570801086536379, 1.4930500725361104, 1.8833540128540847, 2.1690125096955697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.6293864250183105})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.143471717834473})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.842564582824707})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.86391544342041})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.32139778137207})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.132754802703857})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.348152160644531})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.725520133972168})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.876643657684326})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.1678318992009834, 'crossentropy': 5.011703744429933}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 3.351113796234131})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 2.9979958534240723})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.1376953125})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.083435297012329})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.087329387664795})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.2221627235412598})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.1192007064819336})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.1418728828430176})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 66716], ['id', 1096], ['id', 31251], ['id', 53134], ['id', 18048]], 'labels': [5, 7, 1, 2, 9], 'scores': [0.5018006368717203, 0.9892471180999576, 1.383803348692814, 1.713154064695372, 2.00638708911812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.128409385681152})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.435589790344238})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.574045181274414})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.275012969970703})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.393833160400391})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.328490257263184})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.958568572998047})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.229211807250977})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.706159591674805})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.368731498718262})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.325112342834473})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2197679778733866, 'crossentropy': 5.892997080516287}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 3.107609272003174})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 2.9672255516052246})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.2263448238372803})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.358231544494629})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.472986936569214})
store['active_learning_steps'][36]['eval_training']['best_epoch']=2
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 10055], ['id', 71626], ['id', 49597], ['ood', 40154], ['id', 70305]], 'labels': [1, 1, 0, -1, 3], 'scores': [0.5620190728862846, 1.0721612251896957, 1.5583842541903152, 1.9762285489276135, 2.3448499261504594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 4.362031936645508})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.283945083618164})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.362894058227539})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.635923385620117})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.436951637268066})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.300121307373047})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.004575729370117})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.481863975524902})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.21127842655193607, 'crossentropy': 5.3076171875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.0500388145446777})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 2.707921028137207})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.281069040298462})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.267850399017334})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.6542515754699707})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.2699546813964844})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.4837989807128906})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 52401], ['id', 48850], ['id', 51779], ['ood', 41456], ['id', 15467]], 'labels': [1, 1, 8, -1, 2], 'scores': [0.5451065401823949, 0.9950626963334293, 1.3560556576389293, 1.6658361896683096, 1.9434118039426798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.314159870147705})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.898229122161865})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.5901641845703125})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.327989101409912})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.498156547546387})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.065070152282715})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.21573448063921327, 'crossentropy': 5.325983405039951}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.0449042320251465})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.207590103149414})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.0037009716033936})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.4077625274658203})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.298631429672241})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 61892], ['id', 41393], ['id', 8245], ['id', 33102], ['id', 22383]], 'labels': [0, 1, 1, 8, 6], 'scores': [0.7245744065288089, 1.2399744971439868, 1.643189165277904, 2.0145116554585942, 2.346903985839147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.5558648109436035})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.21085262298584})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.950691223144531})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.134694576263428})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.032499313354492})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.19718039336201598, 'crossentropy': 5.397793460932698}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 2.715512275695801})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 2.903552770614624})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.9267525672912598})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.478198289871216})
store['active_learning_steps'][39]['eval_training']['best_epoch']=3
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 36337], ['id', 40862], ['id', 19170], ['ood', 15252], ['id', 27668]], 'labels': [4, 1, 6, -1, 2], 'scores': [0.4357794874927303, 0.8272333909268768, 1.1810718612873554, 1.4816304274261878, 1.7586568715644475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 3.99277925491333})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.810690879821777})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.3858442306518555})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.316347122192383})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.247028350830078})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.098573684692383})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.81036376953125})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2081284572833436, 'crossentropy': 4.004709948332821}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.3051846027374268})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 2.9665045738220215})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 2.8467907905578613})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 2.8654260635375977})
store['active_learning_steps'][40]['eval_training']['best_epoch']=1
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 47646], ['ood', 15363], ['ood', 44710], ['id', 26907], ['id', 24392]], 'labels': [4, -1, -1, 2, 1], 'scores': [0.47873829085793806, 0.901933049181221, 1.2869667836909118, 1.6379974646204944, 1.9499669360707124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.554364204406738})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.402284622192383})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.259038925170898})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.0066070556640625})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.125197410583496})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.207043647766113})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.556300163269043})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.776187896728516})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.728720664978027})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.91626501083374})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.935173988342285})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.22948678549477566, 'crossentropy': 5.560161531960664}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.2134594917297363})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 2.917941093444824})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.254657506942749})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.2612457275390625})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.2602133750915527})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.3763785362243652})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.3392858505249023})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.231924057006836})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.202000141143799})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.335310459136963})
store['active_learning_steps'][41]['eval_training']['best_epoch']=9
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 3891], ['id', 70135], ['id', 28657], ['ood', 39466], ['id', 51620]], 'labels': [-1, 8, 5, -1, 1], 'scores': [0.648663348937157, 1.1258984197827056, 1.5777425638475362, 1.9655824390233039, 2.3055582725134247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.576554298400879})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.411232948303223})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.482939720153809})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.560880184173584})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.20978027043638597, 'crossentropy': 6.011400631914567}
