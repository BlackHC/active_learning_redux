store = {}
store['timestamp']=1621618509
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=23']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=23
store['worker_id']=23
store['num_workers']=24
store['config']={'seed': 1259, 'uniform_ood': False, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 13.10053539276123})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 9.483945846557617})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 17.151622772216797})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 12.098943710327148})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 13.413082122802734})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.11159342347879533, 'crossentropy': 9.983961446488937}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 17143], ['id', 9907], ['id', 9428], ['id', 26889], ['id', 41146]], 'labels': [4, 1, 2, 0, 1], 'scores': [0.703245683516377, 1.2543606881837324, 1.7273123855919974, 2.159366942911543, 2.553948453262036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 8.082170486450195})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 7.839356422424316})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 7.695037841796875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 7.905521392822266})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 9.015534400939941})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 10.798563003540039})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 9.735607147216797})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 9.916747093200684})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 10.012566566467285})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 10.026321411132812})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 9.998577117919922})
store['active_learning_steps'][1]['training']['best_epoch']=8
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1251920712968654, 'crossentropy': 10.9707475414874}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 33314], ['id', 27553], ['id', 64874], ['ood', 16526], ['ood', 41897]], 'labels': [8, 0, 2, -1, -1], 'scores': [0.9050893226350176, 1.6859313893956314, 2.315257828768411, 2.8490647970763234, 3.2950468448635872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 7.997611999511719})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 8.87785816192627})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 11.350574493408203})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 12.450322151184082})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 9.373451232910156})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 8.072240829467773})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 8.597736358642578})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 14.913863182067871})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 13.731310844421387})
store['active_learning_steps'][2]['training']['best_epoch']=6
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.12822679778733867, 'crossentropy': 8.760988879071911}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 18599], ['ood', 40154], ['id', 14833], ['id', 26222], ['id', 20392]], 'labels': [-1, -1, 1, 5, 6], 'scores': [0.7192422322181913, 1.3588867334490766, 1.8986172696915595, 2.3825938785886596, 2.784333334523046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.0966796875, 'crossentropy': 7.058615207672119})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 5.957059860229492})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 8.547479629516602})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 7.610901832580566})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 7.6962080001831055})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 8.146272659301758})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 8.168691635131836})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 8.232961654663086})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 7.668332576751709})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 8.381475448608398})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 9.084793090820312})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 9.948953628540039})
store['active_learning_steps'][3]['training']['best_epoch']=9
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.1127458512599877, 'crossentropy': 9.064924299900122}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 40605], ['id', 24456], ['id', 33223], ['id', 5258], ['ood', 47314]], 'labels': [6, 2, 1, 8, -1], 'scores': [0.6352961570880895, 1.2085818032450302, 1.703164743158732, 2.1685503563666853, 2.5817720549088916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 7.591280937194824})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 8.612478256225586})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.668529510498047})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 6.834637641906738})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 7.2729082107543945})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 7.601678848266602})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.13713890596189304, 'crossentropy': 7.816202774469883}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 49801], ['id', 17827], ['id', 16427], ['id', 27653], ['id', 7424]], 'labels': [-1, 5, 1, 4, 1], 'scores': [0.7075991405448803, 1.3704635845472333, 1.9944527884127163, 2.472665337188566, 2.9030875571719568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 6.724978923797607})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 6.265589237213135})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 6.538103103637695})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 8.073566436767578})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 6.8706207275390625})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.1589582052858021, 'crossentropy': 6.367438393131531}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 4887], ['id', 33662], ['id', 33793], ['id', 13279], ['id', 42650]], 'labels': [9, 1, 8, 0, 1], 'scores': [0.6427470391904184, 1.2081917527390829, 1.7312511821041938, 2.14351945558343, 2.51460538703817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 6.995749473571777})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 8.387090682983398})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 7.210402488708496})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.812888145446777})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.543971538543701})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.322175979614258})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1544637369391518, 'crossentropy': 7.671771761677935}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 30389], ['id', 24669], ['id', 13723], ['id', 16655], ['id', 14920]], 'labels': [-1, 1, 1, 0, 9], 'scores': [1.2030958778075689, 1.901179902614205, 2.452080966025352, 2.9009133656420367, 3.276092633302042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 8.719917297363281})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 6.298002243041992})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.785436630249023})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.522468566894531})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.858219623565674})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 7.001352310180664})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1570759065765212, 'crossentropy': 6.8112773461508915}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 49442], ['ood', 3259], ['ood', 171], ['ood', 45020], ['id', 16896]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.6795351031442398, 1.2238938014656209, 1.7334224411639418, 2.2007029273043006, 2.617811889768677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.457468032836914})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.395707130432129})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.846865177154541})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.599031448364258})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.14831745543945912, 'crossentropy': 6.54803343000922}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 6751], ['ood', 415], ['id', 38634], ['ood', 24791], ['id', 59392]], 'labels': [-1, -1, 3, -1, 0], 'scores': [0.719648582147582, 1.2213022155484508, 1.6719120265865608, 2.0852297674633338, 2.429702162202572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.554169654846191})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.702373504638672})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.533693790435791})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 6.069738388061523})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.15772894898586357, 'crossentropy': 5.930226500076828}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 49076], ['id', 9693], ['id', 23775], ['id', 57740], ['id', 23387]], 'labels': [7, 8, 1, 1, 1], 'scores': [0.6633310358143987, 1.18893737526989, 1.6485607469172923, 2.0413370853881228, 2.4034464859304547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 5.492746353149414})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.419838905334473})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.673160552978516})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 7.12946081161499})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.484336853027344})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.721928596496582})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.14151813153042408, 'crossentropy': 6.660437754494469}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 8717], ['id', 42846], ['id', 42577], ['ood', 41878], ['id', 60720]], 'labels': [5, 9, 4, -1, 9], 'scores': [0.65063190335341, 1.2345975615070803, 1.7865635444295171, 2.2404142120787522, 2.6455122969229423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.308468341827393})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.485417366027832})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.872318267822266})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 7.152716636657715})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.18888291333743085, 'crossentropy': 6.339247128534112}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 4067], ['id', 60384], ['id', 284], ['id', 18695], ['id', 47866]], 'labels': [3, 4, 9, 4, 1], 'scores': [0.6064789130269586, 1.1891141285319042, 1.6915403367049833, 2.12398908408192, 2.4798430034875425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.289661407470703})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.070008277893066})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.981869220733643})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.2007646560668945})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.909619331359863})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.3579301834106445})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.910470962524414})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.1737476951444376, 'crossentropy': 6.4134964898970495}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 30084], ['id', 71664], ['ood', 12079], ['id', 60670], ['id', 21363]], 'labels': [5, 7, -1, 1, 3], 'scores': [0.5586280161649948, 1.0962327952070763, 1.5662257318303023, 2.0103123889648424, 2.409589883083532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 9.191145896911621})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.577762603759766})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.192646503448486})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.3817219734191895})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.238959312438965})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.392690658569336})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.662447929382324})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.447222709655762})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.16652581438229871, 'crossentropy': 6.244504960241241}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 17539], ['id', 8842], ['ood', 12258], ['ood', 17592], ['id', 11636]], 'labels': [-1, 0, -1, -1, 4], 'scores': [0.8407438991762095, 1.4390863944079357, 1.9757974516873316, 2.455959052788163, 2.8746198959708495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 5.625024318695068})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.46946907043457})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 7.249011039733887})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 6.2216362953186035})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 6.090865135192871})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 6.647458553314209})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.14082667486170866, 'crossentropy': 6.7624270129071915}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 50136], ['id', 27442], ['ood', 29442], ['id', 23546], ['id', 35791]], 'labels': [5, 0, -1, 6, 9], 'scores': [0.8253654147203258, 1.3949348013153484, 1.9237105434586086, 2.3292410416992855, 2.700342218570561]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 4.665445804595947})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.685283184051514})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.723957061767578})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 7.730866432189941})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.56962251663208})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 5.635892391204834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.993711471557617})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.394463539123535})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.376368522644043})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.833897590637207})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 7.029904365539551})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.16103257529194837, 'crossentropy': 6.193599464121082}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 17696], ['id', 46227], ['id', 28962], ['ood', 17336], ['id', 39186]], 'labels': [-1, 7, 1, -1, 5], 'scores': [0.6734209829029743, 1.2648719412207114, 1.7823282607497855, 2.2511241320336097, 2.6804562382300574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.960175514221191})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.624355316162109})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.936687469482422})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.344539165496826})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.273955345153809})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.779660224914551})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.614480018615723})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.16399047326367547, 'crossentropy': 5.529790258143823}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 35036], ['id', 35437], ['ood', 17221], ['ood', 29866], ['id', 61286]], 'labels': [0, 3, -1, -1, 5], 'scores': [0.5251992152484757, 1.0295661900193043, 1.5049654787905031, 1.9315143891461712, 2.316038211545848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.932614326477051})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.374073505401611})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.531351089477539})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.781917572021484})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.055445671081543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.282087802886963})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.14270897357098955, 'crossentropy': 5.937409966579595}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 46537], ['id', 10076], ['ood', 35504], ['ood', 43649], ['ood', 47412]], 'labels': [7, 6, -1, -1, -1], 'scores': [0.5969014892266038, 1.1393010244699826, 1.6518115169493992, 2.0909391654564846, 2.481635066945219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 4.633903503417969})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.569624900817871})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.77794885635376})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.73139762878418})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.01768159866333})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.573672294616699})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 6.230757713317871})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.866810321807861})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 6.650722026824951})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.646183967590332})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.830479621887207})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.917867660522461})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.1639520590043024, 'crossentropy': 6.492827337507683}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 38047], ['id', 37085], ['id', 16509], ['id', 43249], ['id', 6254]], 'labels': [-1, 0, 5, 6, 5], 'scores': [0.716878664305149, 1.259525309108203, 1.771596851868897, 2.2562331138159726, 2.668859372422613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.648543357849121})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.982039928436279})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 7.244840621948242})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.020498275756836})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.824174880981445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 7.390730857849121})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.6259002685546875})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.15941917639827904, 'crossentropy': 5.2460493335126}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 9475], ['id', 59772], ['id', 55760], ['id', 20169], ['ood', 12083]], 'labels': [1, 9, 4, 4, -1], 'scores': [0.62558704472676, 1.1788510126288498, 1.6417028882633735, 2.0717012253897105, 2.4665869243805396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.83941650390625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 7.90287971496582})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.194243431091309})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.393800735473633})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 7.249759197235107})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.1461278426551936, 'crossentropy': 7.753767598532575}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 21001], ['id', 67141], ['id', 67343], ['ood', 13223], ['id', 1868]], 'labels': [0, 7, 1, -1, 1], 'scores': [0.6077935108769175, 1.1615999873975449, 1.6853377502245448, 2.1565176507421597, 2.565823873179145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 5.211186408996582})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.189675807952881})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 6.412445068359375})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.409653663635254})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.733138561248779})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.35648775100708})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 7.290746688842773})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.686341762542725})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.201106071472168})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.056545734405518})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.166353702545166})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.6162428855896})
store['active_learning_steps'][21]['training']['best_epoch']=9
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.14236324523663182, 'crossentropy': 5.867898163798402}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 13436], ['ood', 28474], ['id', 9249], ['ood', 10650], ['ood', 41578]], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.68217369972866, 1.288909500139038, 1.8187743479052063, 2.314960692212545, 2.737828095482481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.046539783477783})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.069235324859619})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 5.609424591064453})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 5.74069881439209})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.593631744384766})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.161517143249512})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.454704284667969})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.890410423278809})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.62856912612915})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.181548595428467})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.504789352416992})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.7176737785339355})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.16022587584511372, 'crossentropy': 6.515015773855255}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 41119], ['id', 15874], ['id', 13772], ['id', 61765], ['id', 29210]], 'labels': [1, 3, 3, 6, 8], 'scores': [0.6618144649116942, 1.285752491649648, 1.8417029015810495, 2.324202972104696, 2.7605291588740632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.716302871704102})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 5.918744087219238})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.717453956604004})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 5.357389450073242})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.14866318377381685, 'crossentropy': 5.70695802281807}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 49291], ['ood', 40154], ['ood', 29866], ['id', 10002], ['id', 67243]], 'labels': [0, -1, -1, 0, 3], 'scores': [0.5808228572948928, 1.105300324380602, 1.5875411737500738, 2.012340386513519, 2.3529475111100417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.309957504272461})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.9790802001953125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.437663555145264})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.548954486846924})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.571738243103027})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.15588506453595574, 'crossentropy': 5.223953931699447}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 14982], ['id', 5392], ['id', 7049], ['ood', 9176], ['id', 45284]], 'labels': [2, 1, 5, -1, 7], 'scores': [0.5405484942937733, 1.0223120031452684, 1.4425637718761415, 1.844968810031122, 2.2053938445127077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.25798225402832})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 6.189537525177002})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.59407901763916})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.734862327575684})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.775138854980469})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.662690162658691})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.7256364822387695})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.14954671173939765, 'crossentropy': 5.708031821412108}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 70183], ['id', 50277], ['id', 8631], ['id', 43981], ['id', 67034]], 'labels': [1, 3, 1, 9, 2], 'scores': [0.6366080763927344, 1.142370317168976, 1.6078326350467371, 2.044568123026245, 2.437415756389628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.544093132019043})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.39333963394165})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.325721740722656})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.657553672790527})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.137925148010254})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.685676574707031})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.651772499084473})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.212673664093018})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.19245543945912721, 'crossentropy': 5.912802032114321}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 47792], ['id', 54501], ['id', 3064], ['id', 58557], ['id', 48954]], 'labels': [1, 0, 1, 1, 9], 'scores': [0.6069257081316877, 1.1987742092672615, 1.6806254953219906, 2.1242795949326325, 2.523221308504132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 5.052464485168457})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.222977638244629})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.385476112365723})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.537337779998779})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.8087158203125})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.444615364074707})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.99501895904541})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.721621513366699})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.8423261642456055})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.889217853546143})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.18354333128457284, 'crossentropy': 5.327149037722803}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 20554], ['id', 44994], ['id', 13362], ['ood', 33767], ['id', 6683]], 'labels': [9, 1, 1, -1, 1], 'scores': [0.5711284149802556, 1.1046325803453088, 1.6187231024855304, 2.0652984576532534, 2.474514838216722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.876628398895264})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.634838104248047})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.206250190734863})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.85638427734375})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.494833946228027})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.151885509490967})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.7759318351745605})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.7978105545043945})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.1898816840811309, 'crossentropy': 5.415671097111248}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 2065], ['ood', 25434], ['ood', 9881], ['id', 24564], ['ood', 16526]], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.6358912777546339, 1.2441387594017312, 1.7814459664018907, 2.261658091181996, 2.6908831510917803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.352370262145996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 6.043950080871582})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.351000785827637})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 6.40225887298584})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.190574645996094})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.910679817199707})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.118512153625488})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.355226516723633})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.081207275390625})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.014042854309082})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.18811462814996927, 'crossentropy': 6.095919805431777}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 49039], ['id', 3522], ['ood', 34002], ['id', 33758], ['id', 40839]], 'labels': [9, 5, -1, 1, 5], 'scores': [0.7764686836785293, 1.40052766548712, 1.9257424916390766, 2.403122963113109, 2.8031134126126407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.226311206817627})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.580381393432617})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.355222225189209})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.448098182678223})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.222999095916748})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.415773391723633})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.83449125289917})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.474282264709473})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.17870313460356485, 'crossentropy': 6.045774191379841}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 4987], ['id', 5347], ['id', 3220], ['ood', 24791], ['id', 66536]], 'labels': [1, 6, 3, -1, 1], 'scores': [0.6688288106605218, 1.310056859902601, 1.884932498655572, 2.3918574319398083, 2.7832061196144355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.14494514465332})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.67005729675293})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.962333679199219})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.762512683868408})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.356259346008301})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.18227566072526122, 'crossentropy': 5.470140116011064}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 51454], ['id', 62706], ['id', 51848], ['id', 63360], ['id', 5885]], 'labels': [1, 8, 0, 3, 3], 'scores': [0.5712842673491514, 1.0866950762865946, 1.5639780662017344, 1.9903446409370567, 2.3765020404605366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.135836124420166})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.263877868652344})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.011885643005371})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 4.95161771774292})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.382867336273193})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.606240749359131})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.645949363708496})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 6.0592041015625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.294748306274414})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.486982345581055})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.674648761749268})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.20647664413030117, 'crossentropy': 6.532398226221574}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 42676], ['id', 69032], ['id', 42813], ['id', 17629], ['id', 52797]], 'labels': [-1, 8, 1, 5, 5], 'scores': [0.6304320173530287, 1.2399211595194077, 1.775128372139703, 2.224674098544745, 2.63398784569525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.763521671295166})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.808274269104004})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.951774597167969})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.206194877624512})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.810616493225098})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.203402519226074})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.169605255126953})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.538904190063477})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.665362358093262})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.660958290100098})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.6625847816467285})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.436069488525391})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.487664699554443})
store['active_learning_steps'][33]['training']['best_epoch']=10
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2585663798401967, 'crossentropy': 4.4555159875345725}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 52953], ['ood', 48529], ['id', 65703], ['id', 59805], ['ood', 38078]], 'labels': [1, -1, 6, 5, -1], 'scores': [0.6085734736524526, 1.145126215899566, 1.619036248775231, 2.042763766663027, 2.423172999848787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.516359329223633})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.33161735534668})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.410196304321289})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.690840244293213})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.183659553527832})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.845283508300781})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2042102028272895, 'crossentropy': 5.1500340926551935}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 26999], ['ood', 34393], ['ood', 31012], ['id', 58061], ['ood', 11241]], 'labels': [7, -1, -1, 4, -1], 'scores': [0.526286062461307, 1.0006884974733303, 1.4528850168557215, 1.8670871219330092, 2.2528633981547976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.371763229370117})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.071904182434082})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.1485676765441895})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.670729637145996})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.60445499420166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.525242805480957})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.712208271026611})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2053242163491088, 'crossentropy': 5.581291775507069}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 5208], ['id', 60157], ['id', 13312], ['id', 4115], ['id', 31172]], 'labels': [3, 0, 5, 1, 1], 'scores': [0.7235974528065239, 1.3143136934866284, 1.8618376677283126, 2.342359910768603, 2.728131178207372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.548026084899902})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.9579620361328125})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.040647029876709})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.331016540527344})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.186135768890381})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.69317102432251})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.629087924957275})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.629741191864014})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 5.897482872009277})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.499546051025391})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.055910110473633})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.22760448678549478, 'crossentropy': 5.638610652274124}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 35504], ['id', 47070], ['id', 50616], ['ood', 27170], ['id', 46177]], 'labels': [-1, 9, 1, -1, 1], 'scores': [0.6418289343101935, 1.2558173322353579, 1.8199185896591645, 2.2833077191949434, 2.6773485864164517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 4.708323955535889})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 4.896698951721191})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.601434230804443})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.587140083312988})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.5527215003967285})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.137038707733154})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.649503707885742})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.6487884521484375})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.20751382913337432, 'crossentropy': 5.977498847572218}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 28439], ['id', 39210], ['id', 68131], ['ood', 29695], ['id', 15273]], 'labels': [8, 9, 8, -1, 1], 'scores': [0.6762437617433879, 1.309073983552091, 1.8085397627870883, 2.2675598372935664, 2.6812579685628686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.409459114074707})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.571242332458496})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.343178749084473})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.686699867248535})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.832952976226807})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.234473705291748})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.612327575683594})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.580217361450195})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.6002726554870605})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.8197221755981445})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.739531517028809})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.041620254516602})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.479742527008057})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.482938289642334})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.685069561004639})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.567240238189697})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.752397537231445})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.747647285461426})
store['active_learning_steps'][38]['training']['best_epoch']=15
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.23102335586969883, 'crossentropy': 5.67553936021051}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 41032], ['id', 67013], ['id', 60188], ['id', 28372], ['id', 29912]], 'labels': [-1, 2, 5, 6, 0], 'scores': [0.7666341211699739, 1.424096889960094, 1.9753524946317165, 2.468319006501128, 2.899711250525227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.454042434692383})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.642491340637207})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.351227760314941})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.253686428070068})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.255847930908203})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.311495780944824})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.19756453595574677, 'crossentropy': 5.023400286186233}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 34471], ['id', 12044], ['ood', 24791], ['id', 17652], ['id', 55482]], 'labels': [3, 1, -1, 1, 1], 'scores': [0.5152163491800588, 1.0151047952022867, 1.4642176354384504, 1.8657727383331553, 2.2153329138565834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.312371253967285})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.123154163360596})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.687971115112305})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.136362075805664})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.536820888519287})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.328207015991211})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.753005504608154})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.952732086181641})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.17178856791641056, 'crossentropy': 5.613998516249231}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 23234], ['ood', 12754], ['id', 65878], ['id', 17784], ['id', 2164]], 'labels': [1, -1, 0, 9, 5], 'scores': [0.6114156221221361, 1.1755442897736588, 1.654920037657317, 2.0953850979629145, 2.496321946186331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.15916633605957})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.422162055969238})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.024542808532715})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.357480049133301})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.110389232635498})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.8356451988220215})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.463643550872803})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.866952419281006})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.755868911743164})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.422107696533203})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 6.007584095001221})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.978446006774902})
store['active_learning_steps'][41]['training']['best_epoch']=9
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.2258758451137062, 'crossentropy': 5.836784414374616}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 66860], ['ood', 28232], ['id', 24328], ['id', 20511], ['ood', 8627]], 'labels': [6, -1, 6, 9, -1], 'scores': [0.7715130324660591, 1.375249304749457, 1.9434711916993157, 2.4638625042944335, 2.9228035851561343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.8399767875671387})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.1043782234191895})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.580556869506836})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.040956497192383})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.680218696594238})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.995573997497559})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.625514507293701})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.305476188659668})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.501084327697754})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.49497127532959})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.867907524108887})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.144542694091797})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.948295593261719})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.5271735191345215})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.604445934295654})
store['active_learning_steps'][42]['training']['best_epoch']=12
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.2585279655808236, 'crossentropy': 5.053480451943762}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 68926], ['id', 42060], ['ood', 19670], ['id', 65004], ['ood', 36519]], 'labels': [1, 7, -1, 8, -1], 'scores': [0.6453924995689622, 1.238911841384629, 1.8006057245389835, 2.271657586750293, 2.6799091523519527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.44011116027832})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.911415100097656})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.388176918029785})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.646059036254883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.316532135009766})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.655030250549316})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.91924524307251})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.846050262451172})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.771182060241699})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.915265083312988})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.22760448678549478, 'crossentropy': 4.841967938498771}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 5533], ['ood', 6241], ['id', 14245], ['id', 66914], ['id', 59888]], 'labels': [-1, -1, 7, 1, 1], 'scores': [0.6578766062630388, 1.2825903223251531, 1.792188504386056, 2.2341820201394853, 2.607078424042701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 4.410651683807373})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.073024749755859})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.458049774169922})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.020832538604736})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.491700649261475})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.282065391540527})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.907500267028809})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 7.1894426345825195})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.10533332824707})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.867776393890381})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.4986748695373535})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.910398483276367})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.804840564727783})
store['active_learning_steps'][44]['training']['best_epoch']=10
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.23448063921327597, 'crossentropy': 6.000736473378918}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 29695], ['ood', 36182], ['id', 69286], ['id', 36656], ['id', 38952]], 'labels': [-1, -1, 1, 3, 9], 'scores': [0.7143192908204985, 1.36128466917433, 1.9324415170454876, 2.4485640095595196, 2.85835582624553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 4.621667861938477})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.188485622406006})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.269204139709473})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 4.903445243835449})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.4998979568481445})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.399924278259277})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.475255966186523})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.834908962249756})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.052756309509277})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.9078826904296875})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.17013675476336818, 'crossentropy': 6.384951694068838}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 31575], ['id', 58612], ['id', 66726], ['ood', 192], ['id', 12130]], 'labels': [-1, 6, 2, -1, 0], 'scores': [0.7594115061961324, 1.3560766580036452, 1.9189931931686135, 2.4065596128261335, 2.814023262304289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.644223213195801})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.1805572509765625})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.876662254333496})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.283750534057617})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.451983451843262})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.84304141998291})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.514057159423828})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.52526330947876})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.24577443146896127, 'crossentropy': 5.334109221342962}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 4277], ['ood', 8680], ['id', 48581], ['ood', 650], ['id', 39378]], 'labels': [-1, -1, 7, -1, 5], 'scores': [0.6700827133987755, 1.3190804865828554, 1.8223368652888157, 2.2834563682670685, 2.7020876920986865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.23911190032959})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.895692348480225})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.505582332611084})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.877617835998535})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.287993431091309})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.16556545789797172, 'crossentropy': 4.854720572276429}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 31575], ['ood', 4585], ['ood', 22262], ['id', 55727], ['ood', 38683]], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.616643092521789, 1.1055202964815178, 1.524751974830417, 1.9212241036163755, 2.2738047021225443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.27460241317749})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.926788806915283})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.329781532287598})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.924374580383301})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.691711902618408})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.916713714599609})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.21300706822372464, 'crossentropy': 5.0429957600261215}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 46081], ['id', 51442], ['id', 14133], ['ood', 34270], ['id', 34027]], 'labels': [2, 1, 9, -1, 1], 'scores': [0.537174406372849, 1.015166703484867, 1.4606592738314568, 1.8802369032986128, 2.268425582116495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.70440673828125})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.004432678222656})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.7739763259887695})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.242420196533203})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.895574569702148})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.533002853393555})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.646176338195801})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.775146007537842})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.24489090350338044, 'crossentropy': 4.909285626824677}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 29611], ['ood', 34283], ['id', 5270], ['id', 57876], ['ood', 9418]], 'labels': [8, -1, 9, 2, -1], 'scores': [0.5445283188327608, 1.0682509660799577, 1.5525733591869044, 1.979285910775248, 2.351912158843543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.156651496887207})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.824840545654297})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.980319976806641})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.4213175773620605})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.035486221313477})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.404637336730957})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.312694549560547})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.2392440073755378, 'crossentropy': 5.1993225885448675}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 11191], ['id', 43328], ['id', 68772], ['id', 59827], ['ood', 35911]], 'labels': [1, 5, 4, 6, -1], 'scores': [0.7486112181276443, 1.276681334789198, 1.7752534079475724, 2.2150449663861025, 2.5955441124784535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.245074272155762})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.179237365722656})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.621981620788574})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.215721130371094})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.814892768859863})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.031981468200684})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.124833106994629})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.220541000366211})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.008878707885742})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.100438117980957})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.515138149261475})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.713309288024902})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.909329891204834})
store['active_learning_steps'][51]['training']['best_epoch']=10
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.2465043023970498, 'crossentropy': 5.18327863302858}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 58882], ['id', 9909], ['id', 56679], ['ood', 25731], ['id', 61489]], 'labels': [1, 3, 7, -1, 1], 'scores': [0.7684355608159241, 1.4744036715796955, 2.050839488181925, 2.5612412017432726, 2.9435509869875567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.1140055656433105})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.2936882972717285})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.384824752807617})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.175146579742432})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.370489120483398})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.158784866333008})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.406132221221924})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.8346452713012695})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.361878871917725})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.970037937164307})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.2502304855562385, 'crossentropy': 5.118551806430547}
