store = {}
store['timestamp']=1621613310
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=13']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=13
store['worker_id']=13
store['num_workers']=24
store['config']={'seed': 1248, 'uniform_ood': True, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 9.389338493347168})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 10.176534652709961})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.09765625, 'crossentropy': 9.66977310180664})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 10.025503158569336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 10.236312866210938})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.13640903503380455, 'crossentropy': 10.21772481945298}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 43996], ['id', 36738], ['ood', 26708], ['id', 55505], ['id', 10953]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1735283254986935, 1.7811885520366433, 2.3521343968061803, 2.799035021465217, 3.1841744736971247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 6.926791667938232})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 6.342566013336182})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 6.43179178237915})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1064453125, 'crossentropy': 6.587456226348877})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.11885371850030732, 'crossentropy': 6.6292951943761524}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 16958], ['id', 33817], ['id', 67272], ['id', 1591], ['id', 21166]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7581313844190452, 1.446859954630602, 2.026716048988172, 2.541605811009765, 2.9576203550483413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 6.427145004272461})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 8.440488815307617})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 11.46053409576416})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 7.466291427612305})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 7.017657279968262})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.313750743865967})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 7.213029861450195})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.86721134185791})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.982763290405273})
store['active_learning_steps'][2]['training']['best_epoch']=6
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.12622925629993853, 'crossentropy': 7.874892560118316}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 4608], ['ood', 22098], ['id', 628], ['id', 19741], ['id', 61166]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7059082514320405, 1.3478586861074975, 1.9345526308972936, 2.459274058727356, 2.889391155597119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 8.111013412475586})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 5.966897010803223})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 7.097372055053711})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 7.5031208992004395})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.6275129318237305})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 9.790180206298828})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 9.366656303405762})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 7.2886061668396})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.14201751690227413, 'crossentropy': 8.091146833704672}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 34839], ['id', 17160], ['id', 62722], ['id', 52177], ['id', 36058]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7016150053246499, 1.3541757634737799, 1.9499762783053884, 2.467218310826377, 2.874602733839547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 7.604780197143555})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 6.6117472648620605})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.429258823394775})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 7.319240570068359})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 7.404516696929932})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 8.162406921386719})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 31.451831817626953})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.13560233558696988, 'crossentropy': 7.968337046711739}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 11895], ['id', 23244], ['id', 26946], ['id', 70617], ['id', 1148]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8853966396022317, 1.4657988304621652, 1.9987726495839215, 2.433643080916605, 2.801297625715347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.509481430053711})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 7.955167770385742})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 11.916448593139648})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 7.8471574783325195})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.476727485656738})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.14005838967424708, 'crossentropy': 6.6464399585126}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 16872], ['id', 27617], ['id', 67081], ['id', 7946], ['id', 34317]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7304176542187824, 1.3768584375690827, 1.9365168942234083, 2.3911672800816746, 2.7860427420150042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.0986328125, 'crossentropy': 8.41157341003418})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.338798522949219})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 5.440627574920654})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 5.553006649017334})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.094488143920898})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.003949165344238})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 6.663184642791748})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 6.334290504455566})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.15215888137676706, 'crossentropy': 5.546565885256607}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 25022], ['id', 40615], ['id', 15972], ['id', 18550], ['id', 67512]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7330685359227278, 1.385195696629987, 1.9003496148371877, 2.3839427187085915, 2.763914653431593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 7.084466934204102})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 5.575296401977539})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 5.954746246337891})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.141653060913086})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 6.322174072265625})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.3657732009887695})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.14751075599262448, 'crossentropy': 5.555327337507683}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 62714], ['id', 56716], ['id', 69706], ['id', 6800], ['id', 9316]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5762027561147345, 1.1064018837254106, 1.6057724672448939, 1.992443734779565, 2.351461729747525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 6.075703144073486})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 4.773277282714844})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 7.706923484802246})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 5.638492584228516})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.15865089121081746, 'crossentropy': 5.875771886524277}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 1387], ['id', 35324], ['id', 31414], ['id', 22320], ['id', 35193]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5995857030115568, 1.161605811577251, 1.6315298658769803, 2.046624438396271, 2.4257355235454963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.584558486938477})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 6.806429862976074})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.823179721832275})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.985020160675049})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 7.071721076965332})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.983677864074707})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.916882514953613})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.6504387855529785})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.1548478795328826, 'crossentropy': 6.29986891133989}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 33489], ['id', 65301], ['id', 9292], ['id', 67798], ['id', 38585]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6532928984983928, 1.212616041661477, 1.7223385476536475, 2.1930386621582336, 2.6051673983497663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.098336219787598})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.229808330535889})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.09570837020874})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.05494499206543})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 4.886958122253418})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.521740913391113})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 8.420942306518555})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.243290901184082})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.385957717895508})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.0954909324646})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 6.295868873596191})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.16349108789182545, 'crossentropy': 6.5896072622157345}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 63453], ['id', 15604], ['id', 6304], ['ood', 36438], ['id', 23678]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7627066858375855, 1.4291965981217838, 2.0114244945437547, 2.5087028446191653, 2.952856056731224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 6.57625675201416})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 4.896778106689453})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 4.465311527252197})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.392844200134277})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 4.685894966125488})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.868019104003906})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.843230247497559})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.8267059326171875})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.014670372009277})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.01308012008667})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.769068717956543})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.15872771972956362, 'crossentropy': 4.8480451943761524}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 30982], ['id', 51621], ['id', 26075], ['id', 62630], ['id', 39267]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5764664914633781, 1.104139616823018, 1.604662872702462, 2.0420701837988506, 2.4360892352951353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 6.070087432861328})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.804393768310547})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.11081600189209})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.095918655395508})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.423041820526123})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.622305870056152})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.436340808868408})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.842554092407227})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.16157037492317147, 'crossentropy': 4.925812461585741}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 64405], ['id', 63236], ['id', 17555], ['id', 39040], ['id', 26919]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5863822320375003, 1.1463583964013293, 1.6780924209490817, 2.1320469349566515, 2.5264667196440342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 4.459470748901367})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.005496978759766})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.317313194274902})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.157975196838379})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 5.378113746643066})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 4.995471000671387})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.16629532882606024, 'crossentropy': 4.792897023375077}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 48468], ['id', 13054], ['id', 69755], ['id', 25806], ['id', 71403]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6846991631576309, 1.2094646917941283, 1.7120866774622518, 2.1528284344683684, 2.533419797662333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 6.010997295379639})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.231503486633301})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 8.211346626281738})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.957091331481934})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.935007572174072})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.370460510253906})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.8569746017456055})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.435335159301758})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.727802276611328})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.1919176398279041, 'crossentropy': 5.497147741241549}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 38923], ['id', 45040], ['id', 29245], ['id', 69675], ['id', 38979]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.708165314127825, 1.3314788886274913, 1.8625290651746287, 2.3131935995971222, 2.7169523003562306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 4.622347831726074})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.431436538696289})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.463386535644531})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.341078281402588})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.941220760345459})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.727865219116211})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.035065174102783})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.1863859864781807, 'crossentropy': 5.4256257922941}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 45357], ['id', 63686], ['id', 53181], ['id', 17188], ['id', 54463]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7101332811537509, 1.3445857917735133, 1.854706147696854, 2.312633023653838, 2.717851689761349]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 5.655384063720703})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.314949035644531})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.72428035736084})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.704809188842773})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.76717472076416})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.147187232971191})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.322477340698242})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.18135371850030732, 'crossentropy': 5.234243551206208}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 37642], ['id', 28887], ['id', 24617], ['id', 60903], ['id', 59565]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6974801037367087, 1.3385445800666895, 1.906508014175111, 2.4524589384676503, 2.901876055547228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.4498701095581055})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 5.460509777069092})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 4.835494041442871})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.043466091156006})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.1461662569145667, 'crossentropy': 4.40797233933236}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 24923], ['id', 48524], ['id', 39317], ['id', 25565], ['id', 65021]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.814605749589647, 1.4351928795770559, 1.9398257045526446, 2.356740811001977, 2.699366773347938]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.891969680786133})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.1436076164245605})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.490838050842285})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.805554389953613})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.897403717041016})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.2743659019470215})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.284208297729492})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.098613739013672})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.630578994750977})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.18484941610325753, 'crossentropy': 6.359079090158267}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 6904], ['id', 64145], ['id', 26105], ['id', 7733], ['id', 59992]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7285043861052323, 1.398330912620898, 1.9576165193235187, 2.4315770813283404, 2.8242602093175027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 4.932613372802734})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.417294025421143})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.592471122741699})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.759725570678711})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 4.296600341796875})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.728318214416504})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.645554065704346})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.30919075012207})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.789748191833496})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.16794714197910265, 'crossentropy': 4.408568060464044}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 14481], ['id', 179], ['id', 71414], ['id', 13306], ['id', 70172]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7131510726122507, 1.335125206213775, 1.910126238922425, 2.429077674460605, 2.884463639739014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 4.725211143493652})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.75811767578125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.430792808532715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.6263532638549805})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.377957820892334})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.369419574737549})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.18335125998770743, 'crossentropy': 3.8662055354947755}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 13223], ['id', 29617], ['id', 28308], ['id', 22386], ['id', 25223]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6349347647539574, 1.1573794098358121, 1.6294123197841888, 2.042004241830602, 2.38148380927656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.4361572265625})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.860875129699707})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.665685653686523})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.188605785369873})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.776876926422119})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.001844882965088})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.915557861328125})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.8906354904174805})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.052776336669922})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 6.011789321899414})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 4.401132583618164})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.18404271665642286, 'crossentropy': 4.289204152581438}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 27475], ['id', 35037], ['id', 70505], ['id', 4899], ['id', 55518]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6693341961685411, 1.3045567782082736, 1.801758481170043, 2.253006110862363, 2.654421893429812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.623138904571533})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.829345703125})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.37982177734375})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.28548526763916})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.19905424118042})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.598209381103516})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.899758338928223})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.939648151397705})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.19660417947141978, 'crossentropy': 4.126966329901659}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 30985], ['id', 32753], ['id', 41292], ['id', 59017], ['id', 15907]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6182982319044523, 1.113497871748982, 1.5966191420197378, 2.0354456629211803, 2.4379234746403107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 5.280965805053711})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.6415300369262695})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.003907203674316})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 4.7304887771606445})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.116460800170898})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 4.818853378295898})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.205329895019531})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.705101490020752})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.18277504609711126, 'crossentropy': 4.3553586091157035}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 29930], ['id', 17641], ['id', 19940], ['id', 7920], ['id', 40482]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6973836822777972, 1.3041208296481699, 1.854615103735532, 2.3143405168711, 2.740332557690981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.178323745727539})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.53173303604126})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.604436874389648})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.233920097351074})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.818079948425293})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.367611885070801})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.18204517516902274, 'crossentropy': 4.276946102393208}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 69041], ['id', 26363], ['id', 17265], ['id', 68545], ['id', 45568]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.564695528484024, 1.1012571378216673, 1.6041952368787684, 2.051523566028287, 2.4618797729943385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.80226993560791})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.0038862228393555})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.480707168579102})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.349430084228516})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.692373275756836})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.4725847244262695})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.496016502380371})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.5187458992004395})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.287713527679443})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.869224548339844})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.751766204833984})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.034381866455078})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.920632362365723})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.1432600021362305})
store['active_learning_steps'][25]['training']['best_epoch']=11
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.19998463429625077, 'crossentropy': 4.527020530020744}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 6391], ['id', 30238], ['id', 7339], ['id', 5033], ['id', 26098]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5921918916315736, 1.140452975995057, 1.6241660111508018, 2.0623482397711665, 2.442694533254774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 4.571780204772949})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.106522560119629})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.231133460998535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.322813034057617})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.19821757836508913, 'crossentropy': 4.4045651745928085}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 61336], ['id', 16400], ['id', 17605], ['id', 34276], ['id', 9051]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6176748678075024, 1.0952937156748503, 1.524613013744733, 1.925128096996457, 2.280417212689195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.272199630737305})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.106241703033447})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.615015983581543})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.856823921203613})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.692781448364258})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.9155378341674805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.533048629760742})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.773570537567139})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.712331771850586})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.19372311001843884, 'crossentropy': 4.499779418120006}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 47603], ['id', 479], ['id', 35711], ['ood', 20696], ['id', 35536]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5848187978434134, 1.1488086960789148, 1.68259164424674, 2.1638903065200044, 2.594605474017057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.763669013977051})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.003905296325684})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.732321262359619})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.36682653427124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.678668975830078})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.9738450050354004})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.235730171203613})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.366823673248291})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.153434753417969})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.666180610656738})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.9916508197784424})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.642562389373779})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.511608123779297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.548850059509277})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.412925720214844})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.663300037384033})
store['active_learning_steps'][28]['training']['best_epoch']=13
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.23824523663183775, 'crossentropy': 3.9561258139021205}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42704], ['id', 65346], ['id', 69974], ['id', 42473], ['id', 23195]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6745693270034883, 1.2734686088126104, 1.8227522556337639, 2.2996307656479917, 2.7158082131979935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.991172790527344})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 4.191032409667969})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.185303688049316})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.100513458251953})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.856471061706543})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.198999404907227})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.00136137008667})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.184649467468262})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.449343681335449})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.795557498931885})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.474490642547607})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.561361312866211})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.709933280944824})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.502053260803223})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.630867004394531})
store['active_learning_steps'][29]['training']['best_epoch']=12
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.23378918254456055, 'crossentropy': 4.7085014957552245}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 49688], ['id', 42294], ['id', 60322], ['id', 30631], ['id', 44618]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6848345142578436, 1.32321868122018, 1.8805553335459009, 2.380895669235601, 2.8069875505684116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.4733290672302246})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.7882230281829834})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.203536033630371})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.936506748199463})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.57232666015625})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.238180160522461})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.250920295715332})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.23793792255685312, 'crossentropy': 3.675521953749232}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 50388], ['id', 2855], ['id', 15264], ['id', 31522], ['id', 49521]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6122993779584314, 1.189396147032391, 1.6866332335332013, 2.08837266523663, 2.452875844429313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.030955791473389})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.522974967956543})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.260953903198242})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.439813613891602})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.533016204833984})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.793664455413818})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.1458024978637695})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.23346471786499})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.617171287536621})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.702096462249756})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.835144996643066})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 8.00100326538086})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.581939697265625})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.19913952059004303, 'crossentropy': 4.563242775718346}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 54148], ['id', 58350], ['id', 16819], ['id', 57631], ['id', 18313]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.640020368152731, 1.245197609444685, 1.802249450308937, 2.2887279556797333, 2.6808743288545784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.748298645019531})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.433680534362793})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.430798530578613})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.365053653717041})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.661527633666992})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.652170181274414})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.954100608825684})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.088367462158203})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.24193300553165334, 'crossentropy': 4.397311482022126}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 31009], ['id', 66286], ['id', 60626], ['id', 71916], ['id', 20573]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5597131849940791, 1.0799826272180768, 1.5746668784882365, 1.990075971250631, 2.349339120879013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.644048690795898})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.31736159324646})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.019433498382568})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.844886064529419})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.473629951477051})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.329334259033203})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.22948678549477566, 'crossentropy': 3.955720663510295}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 36211], ['id', 18240], ['id', 59166], ['id', 49156], ['id', 39254]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5863596355211897, 1.0854889205371054, 1.551873817674566, 1.9918238581774492, 2.359491180134915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.7912824153900146})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.576699733734131})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.218360900878906})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.456011772155762})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.112342357635498})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 3.9884238243103027})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 3.9462337493896484})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.595623970031738})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2344038106945298, 'crossentropy': 3.790777936770129}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 19171], ['id', 19795], ['id', 46036], ['id', 32023], ['id', 17312]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6111905197700538, 1.1925054715650374, 1.7176360400028114, 2.209151460620806, 2.61347210075158]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.8678622245788574})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.128875255584717})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.427889823913574})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.006041049957275})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.119288921356201})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.203014850616455})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.300631046295166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.4720916748046875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.6735172271728516})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2346342962507683, 'crossentropy': 4.252439605581592}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 64455], ['id', 61872], ['id', 66545], ['id', 35208], ['id', 29298]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6356066816623973, 1.2467328878147175, 1.7301252435239047, 2.1600814773608796, 2.5456343008175537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.8887887001037598})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.155362606048584})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.8049793243408203})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.543694019317627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.509443759918213})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2219575906576521, 'crossentropy': 4.2686597264904735}
