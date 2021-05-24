store = {}
store['timestamp']=1621618145
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=21']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=21
store['worker_id']=21
store['num_workers']=24
store['config']={'seed': 1257, 'uniform_ood': True, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.0966796875, 'crossentropy': 13.03884220123291})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 12.18336296081543})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 13.304105758666992})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 9.966493606567383})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 10.476825714111328})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 10.192296981811523})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 10.635955810546875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 10.50048828125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 10.840204238891602})
store['active_learning_steps'][0]['training']['best_epoch']=6
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1149738783036263, 'crossentropy': 10.92201065035341}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 18339], ['ood', 42966], ['id', 60191], ['ood', 3286], ['id', 64941]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8241466200497944, 1.5109486459161863, 2.1246891135767587, 2.6709420964106485, 3.110726862716252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 8.206356048583984})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 8.111560821533203})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.474827766418457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 5.678104400634766})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.09765625, 'crossentropy': 9.511999130249023})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 9.045957565307617})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.14793331284572833, 'crossentropy': 6.9305710279655806}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 48733], ['id', 61069], ['id', 63057], ['id', 1591], ['id', 20098]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9745230421184639, 1.6622846236027269, 2.235242182715173, 2.7205729730376387, 3.1004358308048534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.0966796875, 'crossentropy': 7.258698463439941})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.09765625, 'crossentropy': 7.4192352294921875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 6.587742805480957})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 6.567954063415527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 7.219841003417969})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 6.959529876708984})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 7.150912284851074})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.11747080516287646, 'crossentropy': 6.639652038836816}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 39213], ['id', 56221], ['id', 23779], ['id', 4951], ['id', 62412]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5268624467855432, 0.9981693753074081, 1.4516066019194875, 1.8347897187148536, 2.1936180151807907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 10.600692749023438})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 6.940005302429199})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 7.0638298988342285})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 6.346435546875})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.13383527965580824, 'crossentropy': 9.704251618200676}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 67347], ['id', 52904], ['id', 22401], ['id', 15359], ['id', 11434]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1756442120405728, 2.030807366429112, 2.6726258402570626, 3.11923130799223, 3.4749776280555693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.6788434982299805})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 8.333456039428711})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 7.911303520202637})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 7.691871643066406})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.14351567301782422, 'crossentropy': 6.651999222111248}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 57242], ['id', 47718], ['id', 71861], ['id', 57915], ['id', 19200]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8196626660651762, 1.4304741194955217, 1.9606668016594115, 2.4447417588246676, 2.824008013199217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 7.074952125549316})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.952883720397949})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 9.05271053314209})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 7.74184513092041})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.13640903503380455, 'crossentropy': 7.520395570835895}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 53750], ['id', 66194], ['id', 72204], ['id', 16064], ['id', 19465]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8197403870179225, 1.431158139973809, 2.0031536455939203, 2.493316439521343, 2.877508792758036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 7.7130560874938965})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.746315956115723})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 7.10722541809082})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 4.575838088989258})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1283420405654579, 'crossentropy': 7.754878610940381}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 47134], ['id', 56579], ['id', 28422], ['id', 4924], ['id', 49400]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6527623683105701, 1.1826688888697627, 1.6636543750485124, 2.0829615404031188, 2.4495915087407933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 6.176934242248535})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 5.8121538162231445})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 7.273486614227295})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 7.029720306396484})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 6.653192043304443})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 6.790858268737793})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.630118370056152})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1642977873386601, 'crossentropy': 6.295224387292563}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 43020], ['id', 42148], ['id', 60800], ['ood', 20530], ['id', 62671]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6165841778355763, 1.1511161150744371, 1.6595381087060588, 2.096425927621958, 2.4726969467056943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.686606407165527})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 6.734708786010742})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 6.964014530181885})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.32436990737915})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.15196681007990165, 'crossentropy': 6.807213837776582}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 13706], ['id', 70620], ['id', 50976], ['ood', 46553], ['id', 13362]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5975369555136052, 1.1512001243314511, 1.6375943654029057, 2.0645957581864405, 2.4444659510622495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.837523460388184})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.308637619018555})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.675117492675781})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.9054951667785645})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.574923515319824})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.2419281005859375})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 7.226985454559326})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.15830516287645974, 'crossentropy': 4.654562473590197}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 57465], ['id', 16934], ['id', 59781], ['id', 15274], ['id', 42886]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6503436292491194, 1.2137797170629678, 1.740188519939335, 2.1984765118296767, 2.5824602824261262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.745304107666016})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.42198371887207})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 7.261659145355225})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.7160258293151855})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.797981262207031})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.021740913391113})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 6.535765171051025})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.11116886138916})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.83354377746582})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.15623079287031347, 'crossentropy': 5.852683115972649}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 8256], ['id', 32585], ['id', 44064], ['id', 10668], ['id', 47824]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6805982980901435, 1.2602734976809193, 1.8009982465491703, 2.292528900232913, 2.6857877131937142]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.421912670135498})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.738260746002197})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.699406623840332})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.7447638511657715})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.037933349609375})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.1077470779418945})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.029269218444824})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.16798555623847572, 'crossentropy': 5.316415853564843}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 61685], ['id', 63213], ['id', 12491], ['id', 45415], ['id', 36332]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5373217046168426, 0.9977737465633689, 1.4126283964580466, 1.811787214927616, 2.177710365689302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 6.671447277069092})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.870699405670166})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.112557411193848})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.301853179931641})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.590068340301514})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.25837516784668})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 7.319845199584961})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.8788743019104})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.15238936693300553, 'crossentropy': 6.286647203441918}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 26879], ['id', 64366], ['id', 45436], ['ood', 26544], ['id', 33662]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5890207978376281, 1.1525844811689465, 1.65455327934726, 2.104084793393918, 2.519041433411889]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.725980758666992})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.972015380859375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.537167549133301})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.972115993499756})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.141864776611328})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 5.78117036819458})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.417515754699707})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.606703758239746})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.439017295837402})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.551486015319824})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.18826828518746158, 'crossentropy': 5.931779876690228}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 7944], ['id', 51582], ['id', 45802], ['id', 4545], ['id', 47857]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6986153397058912, 1.3382976627617968, 1.93271204613876, 2.4366112196473884, 2.8230634740095706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.496294975280762})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.839859485626221})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.1775641441345215})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.831579208374023})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.581233978271484})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.489709854125977})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.566401481628418})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.426264762878418})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.685930252075195})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.19391518131530425, 'crossentropy': 5.078643592501536}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 50059], ['id', 46263], ['id', 28982], ['id', 36937], ['id', 68545]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6778518851782303, 1.2739764452463125, 1.7913767400913523, 2.2133125562677236, 2.591042320319957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 4.948939323425293})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.158550262451172})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.941739082336426})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.47395658493042})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 5.868682861328125})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.900727272033691})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.18177627535341118, 'crossentropy': 5.488467919291641}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 70505], ['id', 43541], ['id', 21064], ['id', 40413], ['id', 33497]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.769257845451131, 1.406196868798122, 1.9729334350698515, 2.4224500467345944, 2.796283340307756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 4.423182010650635})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.952750205993652})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.445859909057617})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.804172992706299})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.176456451416016})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.181200061462815, 'crossentropy': 5.499674679240934}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 53747], ['id', 59694], ['id', 71779], ['id', 15382], ['id', 71196]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6194530121586888, 1.1404031509418315, 1.6227778710248737, 2.0444464414922567, 2.4261948162903018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.6057448387146})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.024752616882324})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.421106338500977})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 4.843935966491699})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.1756684081130916, 'crossentropy': 4.282755358789182}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 13223], ['id', 66127], ['id', 10636], ['id', 47605], ['id', 38370]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5345129924861471, 0.9744677621792093, 1.3819635339178338, 1.7683257324978872, 2.104722356576511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 8.984809875488281})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.470717430114746})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.631386756896973})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.174068450927734})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.54361629486084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.099205017089844})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.18542562999385373, 'crossentropy': 5.949637705516287}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 32220], ['ood', 24791], ['id', 69956], ['id', 43353], ['id', 32576]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6770919082583453, 1.333718092876227, 1.962913642754855, 2.386690961567523, 2.7434462589738535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.7326765060424805})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.581554889678955})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.102093696594238})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.252074718475342})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.659584999084473})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.1909956976029502, 'crossentropy': 4.201887940803626}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 39905], ['id', 56992], ['id', 25735], ['id', 70773], ['id', 66644]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5996893005945718, 1.0953421456030017, 1.5607820567015729, 1.9786232623972948, 2.3640870826591867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 4.449271202087402})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 5.491325855255127})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.706539630889893})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.422919273376465})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.527061939239502})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.426279067993164})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.718982696533203})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.63893985748291})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.758234024047852})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.419424057006836})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.17881837738168407, 'crossentropy': 4.322863747022895}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 12114], ['id', 27297], ['id', 68869], ['id', 34353], ['id', 60215]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5859675637946962, 1.1365037034220613, 1.6426334486360963, 2.0872078489073846, 2.4860324249219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 4.617772579193115})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.320591449737549})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.032212734222412})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.614673614501953})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.324666976928711})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.1750921942224954, 'crossentropy': 4.306189557563767}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 26034], ['id', 69539], ['id', 9490], ['id', 21965], ['id', 24101]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6164810612608804, 1.167419820140621, 1.6662067835279082, 2.118170270937041, 2.526015026768718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.886040687561035})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.5066237449646})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.764396667480469})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.440258026123047})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 4.601126670837402})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.840052127838135})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.276035308837891})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.19218653964351567, 'crossentropy': 4.333589428395821}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 10301], ['id', 44534], ['id', 67833], ['id', 61609], ['id', 41511]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7776479983534617, 1.3499590421344934, 1.8873650450375683, 2.339897569153539, 2.752584801984627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 4.383327484130859})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 4.3961029052734375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.894501686096191})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.234655380249023})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.470859527587891})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.410026550292969})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.09642219543457})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.425107002258301})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.729338645935059})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.01422119140625})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.395665645599365})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 5.458225250244141})
store['active_learning_steps'][23]['training']['best_epoch']=9
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.1848878303626306, 'crossentropy': 5.252986708666257}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 29098], ['id', 69155], ['id', 36183], ['id', 17732], ['id', 3588]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6567183635095304, 1.2928345137123864, 1.8653664444992293, 2.3576854189051986, 2.785094274245214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.969231605529785})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.297032356262207})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.787012577056885})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.250480651855469})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.722198963165283})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 6.153955459594727})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.489377021789551})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.296705722808838})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.042224884033203})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.134846210479736})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.20021511985248924, 'crossentropy': 4.271467268650123}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 63488], ['id', 64986], ['id', 43277], ['id', 40045], ['ood', 21664]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6264070097133829, 1.1715253940736652, 1.6961558144341553, 2.141851123534096, 2.5386886153880663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.632719993591309})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.322721481323242})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.170177936553955})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.01176643371582})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.015804290771484})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.505987167358398})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.947638988494873})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.21389059618930548, 'crossentropy': 4.8897816869622}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 54146], ['id', 36742], ['id', 44952], ['id', 43328], ['id', 32789]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6223043190603956, 1.2268748144930743, 1.773612750035869, 2.2502353327641877, 2.676980562786941]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.656802654266357})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.911655426025391})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.028850078582764})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.139967441558838})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.074800968170166})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.439716339111328})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.993895530700684})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.621992111206055})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.66908073425293})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.808366298675537})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.646382808685303})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.639286994934082})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.566097736358643})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.722752571105957})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.7848944664001465})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.7421793937683105})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.604182720184326})
store['active_learning_steps'][26]['training']['best_epoch']=14
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.23540258143822987, 'crossentropy': 4.573394343980485}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 60188], ['id', 29440], ['id', 25236], ['id', 20331], ['id', 16079]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6494991267175234, 1.2404143764393858, 1.7980955649089139, 2.300723012849594, 2.741295608211418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.238279819488525})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.094964981079102})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.611006736755371})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.632256984710693})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.054642677307129})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.743116855621338})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.4273271560668945})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.373043537139893})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.424129486083984})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.575442314147949})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.650453090667725})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.528144359588623})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.653006076812744})
store['active_learning_steps'][27]['training']['best_epoch']=10
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.22022894898586357, 'crossentropy': 4.178248465830516}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 53735], ['id', 16030], ['id', 22847], ['id', 50684], ['id', 9381]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5777530446752683, 1.140568388995784, 1.6130784251229495, 2.0473063646215994, 2.4358385711826624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.9913551807403564})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.498602867126465})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.90489387512207})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.759357452392578})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.152580261230469})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.19656576521204672, 'crossentropy': 4.229258400718346}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 31157], ['id', 68347], ['id', 61316], ['id', 52518], ['id', 53695]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5428164468743661, 0.9808953210913613, 1.389375540970983, 1.7732499262367902, 2.1234732637014933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.872272491455078})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.324988842010498})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.444820404052734})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.775052547454834})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 4.6180925369262695})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.482809066772461})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.129994869232178})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.20298094652735096, 'crossentropy': 4.475551424688844}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 39215], ['id', 53641], ['id', 66546], ['id', 23318], ['id', 5464]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6426813452346298, 1.171607473801985, 1.6332773413364645, 2.070237378594241, 2.459300071970584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.665472984313965})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.737149238586426})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 7.4984636306762695})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.879005432128906})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.777700424194336})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.8789472579956055})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.167961120605469})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.1421074867248535})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.908703804016113})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.913773536682129})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.628118515014648})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2405500921942225, 'crossentropy': 4.2156942657114325}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 29985], ['id', 30362], ['id', 15537], ['id', 13546], ['id', 18400]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6682002888148175, 1.2339548305650894, 1.7637987672510267, 2.24220580292123, 2.6677889032808055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.8812575340270996})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.442133903503418})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.846817493438721})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.21491003036499})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.172490119934082})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.649347305297852})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.929098606109619})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.21504302397049785, 'crossentropy': 4.037862054394592}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 33541], ['id', 46399], ['id', 54660], ['id', 1807], ['id', 32662]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5760255822005531, 1.0828850541029333, 1.5588131017266473, 1.9759207307085056, 2.345206212295384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.81009578704834})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.621085166931152})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.979300498962402})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.730186939239502})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.8812754154205322})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.217954635620117})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.076743125915527})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.829331874847412})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.459717273712158})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.835176467895508})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.022109031677246})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.204980850219727})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.127716064453125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.83235502243042})
store['active_learning_steps'][32]['training']['best_epoch']=11
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.2534188690842041, 'crossentropy': 4.28678975635756}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 41231], ['id', 15146], ['id', 36882], ['id', 52719], ['id', 15746]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7064083119598346, 1.2863649888134905, 1.802070630323286, 2.260821445973523, 2.6624600756433603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.684077262878418})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.589443206787109})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.328433990478516})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.19683837890625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.8681912422180176})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.6005377769470215})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.500438690185547})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.789898872375488})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.75334358215332})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.822429656982422})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.194016933441162})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.22725875845113705, 'crossentropy': 4.63898699197142}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 35420], ['id', 10454], ['id', 72056], ['id', 32394], ['id', 66874]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6277898116710119, 1.1899249079656404, 1.6883105625507318, 2.13703651675959, 2.5327051180431717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.748171806335449})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.450679779052734})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.792087554931641})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.4226298332214355})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.934100151062012})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.986215591430664})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.838249206542969})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.558750152587891})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.255833625793457})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.016532897949219})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.912439346313477})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.805351734161377})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.047283172607422})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.940986633300781})
store['active_learning_steps'][34]['training']['best_epoch']=11
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.22787338660110634, 'crossentropy': 4.746322734999231}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 60639], ['id', 69201], ['id', 19811], ['id', 39991], ['id', 23292]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6604471415273032, 1.2509383774865768, 1.8056147447485085, 2.2859592591698457, 2.7030703219227323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.692169666290283})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.294637680053711})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.770906448364258})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.410586357116699})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.318078994750977})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.833398818969727})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.443863391876221})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.891274452209473})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.490604400634766})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.917048454284668})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.25161339889366935, 'crossentropy': 4.121166076847726}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 13613], ['id', 4123], ['id', 44344], ['id', 51669], ['id', 61252]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6445672981429169, 1.260633279171754, 1.8274038183014927, 2.319936172083901, 2.7426862636488503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.505131721496582})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.28218936920166})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.384463310241699})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.565035820007324})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.428770065307617})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.090900421142578})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.870432376861572})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 4.052860260009766})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 4.378964424133301})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 5.172835350036621})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.435932636260986})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.3036647203441918, 'crossentropy': 4.107295528100031}
