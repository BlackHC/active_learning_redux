store = {}
store['timestamp']=1621608547
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=9']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=9
store['worker_id']=9
store['num_workers']=24
store['config']={'seed': 1244, 'uniform_ood': True, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.09765625, 'crossentropy': 8.610559463500977})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 13.730630874633789})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.0986328125, 'crossentropy': 11.626321792602539})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 11.578289031982422})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 12.841144561767578})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 8.723876953125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 8.873817443847656})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 8.903985977172852})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 10.925127029418945})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 10.025177955627441})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 16.598697662353516})
store['active_learning_steps'][0]['training']['best_epoch']=8
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.11601106330669944, 'crossentropy': 9.29467098186847}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1064453125, 'crossentropy': 5.046536445617676})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 5.094653129577637})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 4.860754489898682})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 4.5587286949157715})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 6.361807823181152})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 4.735507011413574})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 4.602412223815918})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 41805], ['id', 28149], ['id', 37464], ['id', 20780], ['id', 16946]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5922946082296565, 1.1009919804017718, 1.5667710721885744, 1.9272835724092428, 2.2553408252492595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 7.635201454162598})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 7.717621803283691})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 8.576961517333984})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 9.098379135131836})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 9.064616203308105})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 9.284245491027832})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.12392440073755379, 'crossentropy': 8.733514880723725}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 4.070450782775879})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 4.576564788818359})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 5.325160026550293})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 4.537755966186523})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 4.861058712005615})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 12073], ['id', 19016], ['id', 64946], ['id', 4383], ['id', 44855]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6788448388348555, 1.1953427028108725, 1.6544550868152779, 2.063562207906207, 2.384207370876617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 8.869888305664062})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 9.428191184997559})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 11.764589309692383})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 7.346963882446289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.9292521476745605})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 8.329328536987305})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.83463191986084})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 8.413153648376465})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.13786877688998156, 'crossentropy': 7.325389784688076}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 4.236003398895264})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 3.8663170337677})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 4.4083099365234375})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 4.144094944000244})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 4.737832069396973})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 10229], ['id', 4358], ['id', 65402], ['id', 34743], ['id', 17129]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6517680818314218, 1.2057411585689248, 1.695140980586519, 2.107403700627523, 2.453299515398111]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 10.272153854370117})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 7.762192249298096})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 6.9817399978637695})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 7.659433364868164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.709470748901367})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 7.407036781311035})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 7.139763355255127})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 8.239974021911621})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.13602489244007376, 'crossentropy': 6.180101053511064}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 3.549323797225952})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 4.203405380249023})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 4.098283290863037})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 4.189545631408691})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 3.7348499298095703})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 4.037021160125732})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.742525577545166})
store['active_learning_steps'][3]['eval_training']['best_epoch']=5
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 8474], ['id', 13729], ['id', 33597], ['id', 57805], ['id', 65122]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4747047017965784, 0.9280631183202893, 1.3396483185897037, 1.7150972275006284, 2.0582865433394537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 6.466714382171631})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 6.809016227722168})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.004428863525391})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 5.345303535461426})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.232293128967285})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 5.576402187347412})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 5.5407514572143555})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 5.836683750152588})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.12672864167178857, 'crossentropy': 5.291357151774739}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 4.075418472290039})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 3.751585006713867})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 3.89932918548584})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 3.5913097858428955})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 3.7641103267669678})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 4.057417869567871})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 3.8458681106567383})
store['active_learning_steps'][4]['eval_training']['best_epoch']=6
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 4275], ['id', 4021], ['id', 10771], ['id', 1138], ['id', 15720]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4405307689166752, 0.8686761257563177, 1.2509316533088386, 1.6042785150689465, 1.9142050960612913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 7.908944129943848})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.873648166656494})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.991705894470215})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.7744598388671875})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.6777143478393555})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 9.724838256835938})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 8.198622703552246})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 8.18370246887207})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 9.618907928466797})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.65716552734375})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.14758758451137063, 'crossentropy': 7.561587061117087}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 4.5389404296875})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.808094024658203})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 4.501677513122559})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.566830635070801})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 4.289685249328613})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.198535919189453})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 4.329517364501953})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.395232200622559})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 4.491976737976074})
store['active_learning_steps'][5]['eval_training']['best_epoch']=6
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 32716], ['id', 31619], ['id', 51626], ['id', 44255], ['id', 64776]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8866217268615433, 1.5367531038929128, 2.0949231146134926, 2.5542427249851647, 2.9086364629702155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 8.015874862670898})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.852585792541504})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 6.8217010498046875})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.029438495635986})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.909214019775391})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.768440246582031})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.285606384277344})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.15442532267977874, 'crossentropy': 5.499674679240934}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 3.3726491928100586})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 3.789398670196533})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.3157453536987305})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 4.436138153076172})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.377838134765625})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.205005645751953})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 36888], ['id', 39547], ['id', 23519], ['id', 47204], ['id', 22820]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5821726279701167, 1.0731292585123673, 1.5268650726849478, 1.9178819564919505, 2.271961989574873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.738055229187012})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.155400276184082})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.6645660400390625})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 7.408976078033447})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.921064376831055})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.52114200592041})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.435299873352051})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.351741790771484})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.782488822937012})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.4778547286987305})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1691379840196681, 'crossentropy': 6.463608491472034}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.5162622928619385})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.8307361602783203})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.775485038757324})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.025731086730957})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.911897897720337})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.1068925857543945})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 43328], ['ood', 28193], ['id', 53515], ['id', 15335], ['id', 13587]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5223932417948002, 0.9445577824611848, 1.333155110721031, 1.6723159954604612, 1.977188920915992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 7.518314361572266})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.168707847595215})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.305478096008301})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.074850082397461})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.541981220245361})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 6.579898834228516})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.220893383026123})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.17167332513829134, 'crossentropy': 5.888279929509834}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 3.6002607345581055})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.72104811668396})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.9791479110717773})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 4.303127288818359})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.6588292121887207})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.646200180053711})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 42251], ['id', 61192], ['id', 59727], ['id', 43834], ['id', 63696]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5473854868520792, 1.0649510341426196, 1.4611832173846921, 1.8203777735217272, 2.1564410501035787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 4.6062211990356445})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.802297592163086})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.783939361572266})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.471871376037598})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.995954513549805})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.344243049621582})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.191411972045898})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.1982559926244622, 'crossentropy': 4.859608786781654}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.227421283721924})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.5334391593933105})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.8965935707092285})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.344611883163452})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.705230951309204})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.6160330772399902})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 19062], ['id', 8192], ['id', 71619], ['id', 61257], ['id', 61241]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.520191889725153, 0.9920879084160952, 1.409339770076577, 1.7588818269962712, 2.0794189880634413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 7.268368721008301})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 5.212991237640381})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.49343204498291})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.206049919128418})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.546681880950928})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.081511974334717})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.597583770751953})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 11.743969917297363})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.1878841425937308, 'crossentropy': 5.13357598340504}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 2.7246127128601074})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.3993380069732666})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.2490551471710205})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.6950974464416504})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.7758450508117676})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 59628], ['id', 23929], ['id', 58188], ['id', 45202], ['id', 45075]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5124562999365521, 0.9850542983650592, 1.4087920174185706, 1.7876067245140899, 2.1093487653515393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.561600685119629})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 9.19650650024414})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.049797058105469})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.204422950744629})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.690300941467285})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.985505104064941})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 4.962100505828857})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.18707744314689612, 'crossentropy': 5.637511644322372}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.2392210960388184})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.175101280212402})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.5785117149353027})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.9082751274108887})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 5778], ['id', 58427], ['id', 43489], ['id', 17441], ['id', 72018]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6127867586227977, 1.114924331603846, 1.5800497839606829, 1.9663423000995923, 2.3016377401165578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 7.039677619934082})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.80239200592041})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.964456558227539})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.347151756286621})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.64897346496582})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.467127799987793})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.1848878303626306, 'crossentropy': 5.17696188825292}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.1539597511291504})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.516003131866455})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.8047640323638916})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.510223627090454})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.9394404888153076})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 17236], ['id', 19510], ['id', 3980], ['id', 23732], ['id', 3724]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4552899853171395, 0.8690447730584783, 1.2532372029164707, 1.6153357139167928, 1.932951851200361]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 4.627598762512207})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.332830905914307})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.9537272453308105})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.1471686363220215})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.054754257202148})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.195164680480957})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.18185310387215733, 'crossentropy': 3.9761927627535343}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 2.7800965309143066})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.027578353881836})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.394915819168091})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 2.927807092666626})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 2.977534532546997})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 49966], ['ood', 36747], ['id', 55778], ['id', 40518], ['id', 61326]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5138064824670998, 0.9508819839239755, 1.2700887350110572, 1.5563012456351837, 1.8211615413566644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 6.825945854187012})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 8.097993850708008})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.239592552185059})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.598875045776367})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.688276290893555})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.1726720958819914, 'crossentropy': 7.66327020590043}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.243849277496338})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.223171234130859})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.803412914276123})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.770945072174072})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 4556], ['id', 18717], ['id', 28019], ['id', 2638], ['id', 48287]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6723228434100048, 1.1877075321395116, 1.6423664151680808, 2.0332093668764237, 2.3667337136939643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.358293056488037})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.332837104797363})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.7319536209106445})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.338325500488281})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.302675247192383})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.409798622131348})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.380963325500488})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.5161051750183105})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.555736541748047})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.17255685310387217, 'crossentropy': 4.509325661685618}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 2.8872413635253906})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 2.977802038192749})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.129135847091675})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.223316192626953})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 2.9902243614196777})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 49358], ['id', 70444], ['id', 31844], ['id', 2457], ['id', 29356]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6063458443094649, 1.044159181492705, 1.4480087872592633, 1.8034571787917582, 2.114306254331394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 7.620705604553223})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.388567924499512})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.011474132537842})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.941046714782715})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.17908727719729564, 'crossentropy': 6.654769850568531}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.1437811851501465})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 3.6777915954589844})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 3.691232681274414})
store['active_learning_steps'][16]['eval_training']['best_epoch']=1
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 43582], ['id', 25359], ['id', 11980], ['id', 26017], ['id', 54410]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5620667343154608, 1.0559156175821185, 1.453700987589741, 1.7933304366598133, 2.1043652093686234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.505435943603516})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.368103504180908})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.734118461608887})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.673818111419678})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.627032279968262})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.009140968322754})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.1683696988322065, 'crossentropy': 5.528590412761217}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.208282470703125})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.2547199726104736})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.2882637977600098})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.53090763092041})
store['active_learning_steps'][17]['eval_training']['best_epoch']=1
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 41403], ['id', 27021], ['id', 3592], ['id', 25499], ['id', 29548]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5324834243808477, 1.032715388136737, 1.5050023595685058, 1.922468619045059, 2.278349252923399]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 8.14416217803955})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.44789981842041})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.0087409019470215})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.6778669357299805})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.1903042409342348, 'crossentropy': 7.433548733289797}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 4.260549545288086})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.181597709655762})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.033238410949707})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 5553], ['id', 8284], ['id', 29641], ['id', 38586], ['id', 66630]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6799689200293451, 1.322518713964834, 1.8583591974800395, 2.2774431055059363, 2.5937071419321676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.845314979553223})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.8150129318237305})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.526905059814453})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.317019462585449})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.575267791748047})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.875284194946289})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.216774940490723})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.18135371850030732, 'crossentropy': 5.3850015125614625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 3.0466389656066895})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.186561584472656})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.69063401222229})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.191200256347656})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.7399423122406006})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 31777], ['id', 4899], ['id', 29423], ['id', 70914], ['id', 71555]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6877274559072886, 1.2467538423329345, 1.7614140228636008, 2.1844725478411555, 2.5587091793217303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.278441429138184})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.444896697998047})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.742854595184326})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.053332328796387})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.789690971374512})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 4.803915500640869})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.048792362213135})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.996319770812988})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2004840196681008, 'crossentropy': 4.671763658670098}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 2.6613292694091797})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 2.712996006011963})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 2.9308581352233887})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 2.9212474822998047})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.115004062652588})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 25603], ['id', 56312], ['id', 54116], ['id', 14101], ['id', 10582]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5206130675843155, 0.9808291440516133, 1.3900040952037154, 1.7670934706215906, 2.095049217466162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.294135093688965})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 4.574518203735352})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.834851264953613})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.797536849975586})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.530885696411133})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.970340728759766})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.134614944458008})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.1760141364474493, 'crossentropy': 4.915783638886754}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.3146867752075195})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 2.9460721015930176})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 3.3032078742980957})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.4358432292938232})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.1388421058654785})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.164869785308838})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 32849], ['id', 21767], ['id', 67049], ['id', 69655], ['id', 65516]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4609833738437832, 0.8864181179256645, 1.2896873484126372, 1.6337229667047728, 1.9304629260636972]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 4.435731887817383})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 4.32193660736084})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.351104259490967})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.893472671508789})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.039502143859863})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.29691743850708})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.909821510314941})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.714382171630859})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.19668100799016594, 'crossentropy': 5.192074898202213}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 2.6740918159484863})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.1222174167633057})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.177436113357544})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.239330768585205})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.095839023590088})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.277653932571411})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.043243885040283})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 65189], ['id', 28372], ['id', 59301], ['id', 1534], ['id', 29481]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5408946376685012, 1.045440590939549, 1.499073021419799, 1.9042913928519072, 2.2648893583574985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.322902679443359})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.137661933898926})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.695566177368164})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.86699914932251})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.6910400390625})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.6363725662231445})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.922974586486816})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.183838367462158})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.750737190246582})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2513444990780578, 'crossentropy': 4.461384665988015}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 2.7271108627319336})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.853775978088379})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.205036163330078})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.8608012199401855})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.1146485805511475})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.9781603813171387})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.7559027671813965})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.6695518493652344})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 18161], ['id', 66574], ['id', 12952], ['id', 55972], ['ood', 26981]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5523483627720513, 1.032509806812909, 1.4694233598796167, 1.8659940621613789, 2.2117856191169425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.740362167358398})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.8167009353637695})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.41660213470459})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.051690101623535})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.211587905883789})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.545738220214844})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.796148300170898})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.428213596343994})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.398096561431885})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.231266021728516})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.21965273509526737, 'crossentropy': 4.747888716291487}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 2.647911787033081})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.8736696243286133})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.030876636505127})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.101076602935791})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.015397787094116})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.0131797790527344})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.056485176086426})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.9374003410339355})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.0014634132385254})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 63684], ['id', 66125], ['id', 19982], ['id', 68972], ['id', 63627]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5238340222406898, 1.0040787039434644, 1.407812513506785, 1.7604185507649222, 2.056154868425077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.892910957336426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.801585674285889})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 4.675145149230957})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.699282169342041})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.530561447143555})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.1887359619140625})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.641292095184326})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.781037330627441})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.892290115356445})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.865097761154175})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.4508233070373535})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.658011436462402})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.580938816070557})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.723487377166748})
store['active_learning_steps'][25]['training']['best_epoch']=11
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.24097264904732638, 'crossentropy': 4.3991343586739395}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.6491451263427734})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.5986976623535156})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.9002294540405273})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.5228404998779297})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.6251745223999023})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.8367843627929688})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.6537973880767822})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.679788589477539})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 2.8750481605529785})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.575080156326294})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.659639835357666})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.5546329021453857})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.6709938049316406})
store['active_learning_steps'][25]['eval_training']['best_epoch']=10
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 12341], ['id', 29470], ['id', 4431], ['id', 19837], ['id', 65884]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6166506593579224, 1.1278850958350513, 1.5788244922022194, 1.9835185096933539, 2.309514339321434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.712116241455078})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.600951194763184})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.611904144287109})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.604809761047363})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.500161170959473})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.05775260925293})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.925820827484131})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.21681007990165949, 'crossentropy': 4.7583238898279046}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 2.711785316467285})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.537431716918945})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.780348062515259})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.133072853088379})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.3997840881347656})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.175110340118408})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 13085], ['id', 49365], ['id', 15675], ['id', 17576], ['id', 3939]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5153140740971897, 0.9968775019780356, 1.4046616128880676, 1.7720008572095716, 2.0894454343378976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 4.284128189086914})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.887502670288086})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.063664436340332})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.208460807800293})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.306524276733398})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.9447381496429443})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.21880762138905963, 'crossentropy': 3.9610902567032884}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 2.7911734580993652})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.6135854721069336})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.933960437774658})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.9301555156707764})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.1270945072174072})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 68756], ['id', 29985], ['id', 50700], ['id', 18349], ['id', 40075]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5454949661564122, 0.9748380810470352, 1.3712951884163407, 1.7174955457726049, 2.037554913433238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.264997959136963})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.5864715576171875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.307993412017822})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.9861092567443848})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.018885612487793})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.027078151702881})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.231387615203857})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2329440688383528, 'crossentropy': 3.9175152816725567}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.6200971603393555})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.6607346534729004})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.6652519702911377})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.740095615386963})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.6040005683898926})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.7888355255126953})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 8955], ['id', 70607], ['id', 47857], ['ood', 21165], ['id', 18073]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.45410546810320573, 0.8453649550088427, 1.1882320027507651, 1.5049442176314933, 1.7937949585033728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.8650245666503906})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.708211898803711})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.988046884536743})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.417963981628418})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.310876846313477})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.101958274841309})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.0440778732299805})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.2962141036987305})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.456192970275879})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.592852592468262})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.648995399475098})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2509219422249539, 'crossentropy': 4.131400775968039}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 2.445845127105713})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.567690849304199})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.4956674575805664})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.8069303035736084})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.523834705352783})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.4502556324005127})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 17685], ['id', 59178], ['id', 49049], ['id', 70437], ['id', 27737]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6461577348835443, 1.1227463073799822, 1.5496089970726796, 1.895159644255532, 2.1974781488425537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.098211765289307})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.9435195922851562})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.4514689445495605})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.9128544330596924})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.016532897949219})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.8902344703674316})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2692839582052858, 'crossentropy': 3.161049381530424}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.383906841278076})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.504972457885742})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.393751621246338})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.5620627403259277})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.6259799003601074})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 43348], ['id', 54380], ['id', 50334], ['id', 985], ['id', 26098]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5176446964054469, 0.9207940748170347, 1.2830794056699206, 1.5964806229001294, 1.8638560683755072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.017131805419922})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.811540126800537})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.267827033996582})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.365616798400879})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.107334136962891})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.447226524353027})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.8527963161468506})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 4.149941444396973})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.617188453674316})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 4.054274559020996})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.1054229736328125})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2880685310387216, 'crossentropy': 4.029660910129841}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.983982563018799})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.7981927394866943})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.7249112129211426})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 2.5056891441345215})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.6118950843811035})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.328125, 'crossentropy': 2.5324668884277344})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.4196956157684326})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 2.3598194122314453})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.3232421875, 'crossentropy': 2.4864766597747803})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 18063], ['id', 3991], ['id', 2233], ['id', 20098], ['id', 13604]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6080616025540508, 1.1763835236083238, 1.65785958595777, 2.040927409114469, 2.3722224914985155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.645175933837891})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.1602325439453125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.1119184494018555})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.646049499511719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.590979099273682})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.085066795349121})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.1742377281188965})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.540316581726074})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.121611595153809})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.143105506896973})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.284021377563477})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.447383403778076})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.21990966796875})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.512528419494629})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.6051344871521})
store['active_learning_steps'][32]['training']['best_epoch']=12
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.27642901044867857, 'crossentropy': 4.289831385410264}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 2.645810842514038})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.5016989707946777})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.5500855445861816})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 2.6101109981536865})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.542909860610962})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.5768728256225586})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 2.5613760948181152})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 47441], ['id', 17050], ['id', 42564], ['id', 577], ['id', 13242]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5944244277852391, 1.0979034811956796, 1.5524454613891485, 1.9236259850042554, 2.2584387751321353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.4000959396362305})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.0805158615112305})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.601255416870117})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.246831893920898})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.238731384277344})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.150199890136719})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.269533157348633})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.32407808303833})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 3.754431962966919})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.054889678955078})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.228252410888672})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.420421600341797})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.380481719970703})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 4.176963806152344})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 4.2208123207092285})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 4.305272579193115})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 4.105619430541992})
store['active_learning_steps'][33]['training']['best_epoch']=14
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.30846650276582666, 'crossentropy': 4.0511428842386294}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 2.387692928314209})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.437741756439209})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 2.379363536834717})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 2.6104440689086914})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.6484642028808594})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.365234375, 'crossentropy': 2.309072971343994})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.328125, 'crossentropy': 2.540313482284546})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 2.4749655723571777})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 2.441209316253662})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 29764], ['id', 59825], ['id', 26998], ['id', 16898], ['id', 72224]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.680276013853039, 1.2489226504672846, 1.7521893097246133, 2.17670446615549, 2.5217661069636286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 4.637008190155029})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.617952346801758})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.108545780181885})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.5510735511779785})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.930991172790527})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.407307147979736})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.021296977996826})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.200571537017822})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.331204414367676})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.284464359283447})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 4.194753170013428})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.304459571838379})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.241192817687988})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.694891929626465})
store['active_learning_steps'][34]['training']['best_epoch']=11
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2872618315918869, 'crossentropy': 4.348098614205593}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 2.953244686126709})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.5499868392944336})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 2.4912302494049072})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.891477346420288})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 2.5924324989318848})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.973818302154541})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.3232421875, 'crossentropy': 2.7233052253723145})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.32421875, 'crossentropy': 2.5792720317840576})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 2.6758193969726562})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.3212890625, 'crossentropy': 2.544306516647339})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 2.4745407104492188})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 5324], ['id', 51432], ['id', 8141], ['id', 52058], ['id', 68783]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5929226612119717, 1.106315473778102, 1.5768790012476355, 1.9861546609076859, 2.3465956260894973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.0854434967041016})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.602832794189453})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.455787181854248})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.3698434829711914})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 4.402740478515625})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 4.282543182373047})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.322265625, 'crossentropy': 4.147994041442871})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.132360458374023})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.337890625, 'crossentropy': 3.6318345069885254})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.328125, 'crossentropy': 3.711977243423462})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3603515625, 'crossentropy': 3.77091646194458})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.34765625, 'crossentropy': 3.950810194015503})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.359375, 'crossentropy': 4.43669319152832})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3544921875, 'crossentropy': 4.355820178985596})
store['active_learning_steps'][35]['training']['best_epoch']=11
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.32663644744929315, 'crossentropy': 3.903886022491549}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 2.728111743927002})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.4668493270874023})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.33203125, 'crossentropy': 2.2157459259033203})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.3349609375, 'crossentropy': 2.262220621109009})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 2.6180858612060547})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.333984375, 'crossentropy': 2.3988595008850098})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.33203125, 'crossentropy': 2.4161901473999023})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 57631], ['ood', 26317], ['id', 64154], ['ood', 20700], ['ood', 9958]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7087743787851626, 1.3500475458190422, 1.8561389735802378, 2.2702456938237767, 2.5979371854140103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.7384932041168213})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.157873630523682})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 3.8327112197875977})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.177595138549805})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.571564674377441})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 4.181779861450195})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 4.561686038970947})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.44321346282959})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.27413272857666})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2884910878918254, 'crossentropy': 3.9066857617547632}
