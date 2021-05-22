store = {}
store['timestamp']=1621615452
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=15']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=15
store['worker_id']=15
store['num_workers']=24
store['config']={'seed': 1250, 'uniform_ood': False, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 11.267128944396973})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 9.20585823059082})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 9.595970153808594})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 9.590951919555664})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.10053011677934849, 'crossentropy': 11.182034371158574}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 17418], ['id', 8783], ['id', 21759], ['id', 3509], ['id', 54380]], 'labels': [0, 4, 1, 2, 0], 'scores': [0.7976893297116616, 1.4737199897960456, 2.042999355412931, 2.559262493945514, 2.993478476978032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 9.703450202941895})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 9.094712257385254})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 9.544870376586914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 9.705005645751953})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 9.659245491027832})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 20.053871154785156})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 8.845512390136719})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 12.752906799316406})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 9.577720642089844})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 9.248250961303711})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 9.602668762207031})
store['active_learning_steps'][1]['training']['best_epoch']=8
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.11793177627535341, 'crossentropy': 13.39874601452059}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 60748], ['id', 25213], ['id', 18622], ['id', 3905], ['id', 17979]], 'labels': [0, 5, 3, 3, 0], 'scores': [0.8319104262999253, 1.5885662397171645, 2.261478414016242, 2.7795164966447325, 3.1960819225404506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 8.638093948364258})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 8.499658584594727})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.09375, 'crossentropy': 8.880837440490723})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 7.2918806076049805})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 7.63401985168457})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.11359096496619545, 'crossentropy': 8.325913178972034}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 29850], ['id', 14902], ['id', 28271], ['id', 60977], ['id', 27882]], 'labels': [0, 8, 8, 0, 1], 'scores': [0.7410878482551972, 1.3481524949121493, 1.8651606616411862, 2.314977435781854, 2.7169887315705354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 9.636289596557617})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.037225723266602})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 7.2118096351623535})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 7.839437484741211})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 7.785910606384277})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.09987707437000615, 'crossentropy': 7.410449758950523}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 21994], ['id', 60188], ['id', 11911], ['id', 30491], ['id', 5097]], 'labels': [1, 5, 1, 3, 1], 'scores': [0.6183232086800872, 1.194442059087116, 1.741551904071673, 2.251392176804737, 2.695204207239028]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 7.378290176391602})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.824535369873047})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 7.226398468017578})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 7.488796234130859})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 7.21824836730957})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 7.5291900634765625})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 7.242015838623047})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 7.790173530578613})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.11593423478795328, 'crossentropy': 7.735026241740934}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 38116], ['id', 18538], ['id', 36466], ['id', 64768], ['id', 40774]], 'labels': [-1, 1, 8, 7, 5], 'scores': [0.5978620413373192, 1.099290811428336, 1.5512386620593364, 1.9648769619501198, 2.3382056879229545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 19.8460693359375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 6.304608345031738})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 6.612370491027832})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 6.63580322265625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 8.57319450378418})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 8.284093856811523})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 6.835936546325684})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 7.29563570022583})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 15.21003246307373})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 7.974320888519287})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 7.2225661277771})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 7.310351371765137})
store['active_learning_steps'][5]['training']['best_epoch']=9
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.1746696373693915, 'crossentropy': 15.46027605447142}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 35772], ['id', 67229], ['id', 47070], ['id', 32399], ['ood', 42583]], 'labels': [-1, 1, 9, 2, -1], 'scores': [0.6678050780999598, 1.2046340125974089, 1.71053145332416, 2.1609954991719844, 2.536765037258302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.776951789855957})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 6.664402961730957})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 7.488520622253418})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 8.450525283813477})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1259219422249539, 'crossentropy': 7.13168288068531}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 28374], ['id', 54610], ['id', 9674], ['id', 56503], ['id', 746]], 'labels': [8, 5, 5, 2, 3], 'scores': [0.5539529508312153, 1.0291450419605725, 1.4818420232691212, 1.909330138733992, 2.268612594549282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 8.71070671081543})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.466182708740234})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 6.946053504943848})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.021320343017578})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.045136451721191})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 7.034761428833008})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 7.451327800750732})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 7.25332498550415})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.675015449523926})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 9.61948013305664})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.12496158574062692, 'crossentropy': 7.536974324869392}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 53260], ['ood', 21924], ['id', 49252], ['id', 14787], ['id', 7505]], 'labels': [5, -1, 8, 5, 0], 'scores': [0.6094424601666062, 1.121215842342524, 1.608706281578228, 2.06399651421071, 2.4436236050013687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 9.58635139465332})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 9.428895950317383})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.847468376159668})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 6.6488356590271})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 8.756747245788574})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 7.595996379852295})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 7.611794471740723})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 8.153097152709961})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 9.899931907653809})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.13122311001843884, 'crossentropy': 7.409107060540872}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 47513], ['ood', 11731], ['id', 67251], ['ood', 41753], ['id', 2509]], 'labels': [6, -1, 1, -1, 1], 'scores': [0.8178243256480044, 1.418433113721687, 1.961053478036523, 2.418678684676319, 2.8057823162224675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 7.110249042510986})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 7.997371673583984})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.329176902770996})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.129397392272949})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 5.875345230102539})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 9.130313873291016})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.171182155609131})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.14174861708666256, 'crossentropy': 7.625503586931469}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 34743], ['ood', 36053], ['id', 26132], ['id', 13073], ['id', 41665]], 'labels': [9, -1, 3, 1, 0], 'scores': [0.7958489975824474, 1.4980266754382918, 2.0040495706795456, 2.4669830020838157, 2.872952267088543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.1249895095825195})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.656044006347656})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.3866729736328125})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.665405750274658})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.553250312805176})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.337100505828857})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.818918704986572})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.16402888752304856, 'crossentropy': 5.588002266441303}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 70771], ['id', 37345], ['id', 44165], ['id', 29428], ['ood', 37453]], 'labels': [5, 5, 1, 6, -1], 'scores': [0.7193970360094746, 1.317828076146212, 1.8394183573135923, 2.3143937890744537, 2.6910468943091583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 7.304403305053711})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.665113925933838})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 7.176737308502197})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 7.859653472900391})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 8.027767181396484})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.14712661339889366, 'crossentropy': 7.102760544714198}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 49079], ['id', 55531], ['id', 2783], ['id', 62141], ['ood', 46683]], 'labels': [-1, 0, 1, 7, -1], 'scores': [0.5808026517307643, 1.1022406016145925, 1.5391034613022598, 1.9505465767039816, 2.3154573821551416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.321579456329346})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 7.4604644775390625})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 8.565814971923828})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 7.153431415557861})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 7.037796974182129})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 7.562223434448242})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.14551321450522434, 'crossentropy': 9.503863033958206}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 13126], ['id', 1593], ['id', 40492], ['id', 21977], ['id', 52181]], 'labels': [1, 8, 9, 6, 2], 'scores': [0.5832698602608127, 1.1304891832065689, 1.6420156022151944, 2.1026430980200264, 2.5132311215750676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.828291416168213})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.374973297119141})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.473036766052246})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.987995624542236})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.15139059618930548, 'crossentropy': 7.3892474886677935}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 21], ['id', 37773], ['id', 29006], ['id', 69790], ['id', 58229]], 'labels': [-1, 6, 4, 1, 1], 'scores': [0.9479996580206631, 1.5374737903495626, 2.0195474151590145, 2.435915761646106, 2.815683019092692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.724671363830566})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.5356340408325195})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.559979438781738})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 7.414194107055664})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.695713043212891})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 8.119524002075195})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 8.199752807617188})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.261415004730225})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.16253073140749846, 'crossentropy': 6.862796269975415}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 20898], ['ood', 47585], ['id', 59025], ['id', 43627], ['id', 34242]], 'labels': [-1, -1, 5, 8, 8], 'scores': [0.7581314893732678, 1.3506817055633507, 1.9142863576038573, 2.3975792580336366, 2.797062896808683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.504267692565918})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 11.407472610473633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 7.928276062011719})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 8.663959503173828})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.786514759063721})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 7.856711387634277})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 9.661896705627441})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.13517977873386602, 'crossentropy': 9.09349250441764}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 15365], ['ood', 27417], ['id', 37370], ['id', 26358], ['ood', 271]], 'labels': [1, -1, 2, 9, -1], 'scores': [0.6780614032357777, 1.2629384027170918, 1.7677465251508542, 2.216923394744576, 2.6193925342446143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.908172607421875})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.374956130981445})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 8.29859447479248})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.865634918212891})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.17405500921942224, 'crossentropy': 5.579890255262754}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 49079], ['id', 14971], ['id', 7426], ['id', 14147], ['id', 49966]], 'labels': [-1, 5, 6, 6, 1], 'scores': [0.6587999431350016, 1.2428057207416439, 1.7236991919576923, 2.1648177992976123, 2.5127787076578274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 7.897043228149414})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.369696617126465})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.643239974975586})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.059818267822266})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 7.127350807189941})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.160778045654297})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.1496235402581438, 'crossentropy': 7.7559199975030735}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 40113], ['id', 14931], ['id', 65766], ['id', 57299], ['ood', 10655]], 'labels': [-1, 3, 8, 2, -1], 'scores': [0.5410464136885242, 1.0354209694980696, 1.4778476796860671, 1.86284758527027, 2.214379989793027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.581413269042969})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.449681758880615})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.820793151855469})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.196030139923096})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.538166046142578})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.54226016998291})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.338173866271973})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.343907833099365})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.214271545410156})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.19441456668715426, 'crossentropy': 5.572388670674554}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 16985], ['ood', 44101], ['ood', 22009], ['ood', 17135], ['id', 29032]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.649098619829372, 1.2064641844375545, 1.717429972356772, 2.170156903979044, 2.552159044432825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 7.176060676574707})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 7.6193132400512695})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.442446708679199})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 7.534450531005859})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 6.497283458709717})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 6.470300197601318})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 7.046189308166504})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 7.887714385986328})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 8.01203441619873})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 7.804806709289551})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 7.792316436767578})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 8.013261795043945})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 8.040913581848145})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 8.035140037536621})
store['active_learning_steps'][19]['training']['best_epoch']=11
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.15584665027658268, 'crossentropy': 8.826745687999386}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 9320], ['id', 38349], ['id', 29864], ['id', 14362], ['id', 48429]], 'labels': [4, 5, 5, 0, 8], 'scores': [0.6626771880219298, 1.2578101769275154, 1.7577482563872575, 2.2131566503132047, 2.6362413659514097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 7.3524980545043945})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.656818866729736})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 6.466848850250244})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.895414352416992})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.023093223571777})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.137271881103516})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.197194576263428})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 6.356294631958008})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 6.346958637237549})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.14685771358328212, 'crossentropy': 5.850665767132759}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 40742], ['id', 34577], ['ood', 2330], ['id', 6609], ['ood', 47759]], 'labels': [0, 2, -1, 8, -1], 'scores': [0.6255996303915687, 1.2285451738502133, 1.7717315858250862, 2.2498035189552557, 2.646607054199876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 6.847079753875732})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 7.365446090698242})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 7.1796040534973145})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.602952003479004})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 7.064014434814453})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.725914001464844})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 7.350546836853027})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 7.69118595123291})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 7.637491226196289})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.4015302658081055})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 7.397732734680176})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 7.772197723388672})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.378952980041504})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 7.459374904632568})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 8.012234687805176})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 6.7798542976379395})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 7.242107391357422})
store['active_learning_steps'][21]['training']['best_epoch']=14
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.16948371235402582, 'crossentropy': 7.962740569299324}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 16668], ['id', 8757], ['ood', 44590], ['id', 53839], ['id', 4383]], 'labels': [1, 1, -1, 1, 9], 'scores': [0.6475962315031436, 1.2178507220482735, 1.7458301197287174, 2.2382934053495473, 2.6752055177016354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 7.07234001159668})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.198246002197266})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.929194450378418})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 7.45994234085083})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 7.901132583618164})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 9.862344741821289})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 7.500609874725342})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.627809524536133})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.226942539215088})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.59266471862793})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.756502151489258})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.1732483097725876, 'crossentropy': 7.423714082667487}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 62835], ['id', 2576], ['id', 6020], ['id', 70085], ['id', 65886]], 'labels': [2, 6, 6, 1, 1], 'scores': [0.6845434948425067, 1.264143447187811, 1.7702154721024788, 2.2313545184163424, 2.6416367462785146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.306774616241455})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.409135818481445})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.3137335777282715})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.85944938659668})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.15530885064535957, 'crossentropy': 6.332777927166564}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 359], ['id', 26363], ['ood', 21165], ['id', 52239], ['id', 9432]], 'labels': [5, 0, -1, 1, 5], 'scores': [0.5835151321261158, 1.133645492572266, 1.61704066407723, 2.0739351006755733, 2.4498826860678387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.66426420211792})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.170328140258789})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.067320346832275})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.114642143249512})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.616401672363281})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.224770545959473})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.939249038696289})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.545032501220703})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.104863166809082})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.948997497558594})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.000739097595215})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.6247878074646})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.21704056545789796, 'crossentropy': 4.938531182775046}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 54219], ['id', 32468], ['id', 67686], ['id', 32027], ['id', 59694]], 'labels': [2, 6, 1, 1, 6], 'scores': [0.7151015223433344, 1.3310432130141256, 1.873329268809429, 2.345245569454807, 2.731488452168062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.686584949493408})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.679802894592285})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.324014186859131})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.742705345153809})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.414600372314453})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.19426090964966194, 'crossentropy': 4.821034868143054}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 46327], ['ood', 16942], ['ood', 41267], ['ood', 16567], ['ood', 24876]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7909066748216391, 1.3871803618734555, 1.9275036179925924, 2.3811070287577074, 2.7356703851778157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 8.644583702087402})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.707889556884766})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.874492645263672})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 9.581239700317383})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.433810234069824})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.5209832191467285})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.771933555603027})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.126733779907227})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.3114118576049805})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.340806007385254})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.880520820617676})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.211572170257568})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.169042110443115})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.426150321960449})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.755441188812256})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.344599723815918})
store['active_learning_steps'][26]['training']['best_epoch']=13
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.19410725261216963, 'crossentropy': 6.712723162838046}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 23788], ['id', 2293], ['id', 23823], ['ood', 34667], ['id', 7175]], 'labels': [-1, 0, 5, -1, 9], 'scores': [0.6885721233786053, 1.3211021594796097, 1.8834340373631644, 2.3872486794218934, 2.8215224896358784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.596060752868652})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.168008804321289})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.680451393127441})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.851894378662109})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.844291687011719})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 5.906830787658691})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.340028762817383})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.104467391967773})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.18319760295021512, 'crossentropy': 6.500973561385987}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 4953], ['id', 41474], ['id', 23055], ['id', 56032], ['id', 18503]], 'labels': [-1, 5, 6, 9, 5], 'scores': [0.7111632116097697, 1.3601072336695386, 1.9049783837674252, 2.3972298950330497, 2.8099985362800908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.441056251525879})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.009711265563965})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.348794937133789})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.212474822998047})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.160305023193359})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.292926788330078})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.645865440368652})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.336348533630371})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.852468490600586})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.784312725067139})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.897933006286621})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.978055953979492})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.325437545776367})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 6.446924209594727})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.349340915679932})
store['active_learning_steps'][28]['training']['best_epoch']=12
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.19260909649661956, 'crossentropy': 6.006664874001229}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 55364], ['ood', 192], ['id', 63327], ['id', 17848], ['id', 1943]], 'labels': [1, -1, 1, 3, 1], 'scores': [0.6519353304405298, 1.2434169111844682, 1.7925798341437424, 2.2702842282305795, 2.6903895086044933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.948398590087891})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.75221586227417})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 8.339088439941406})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.545950412750244})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.027148246765137})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.512355804443359})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.880729675292969})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.1889981561155501, 'crossentropy': 5.683687984980025}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 25611], ['id', 33465], ['id', 22506], ['id', 62481], ['ood', 35911]], 'labels': [3, 1, 6, 5, -1], 'scores': [0.5440279531900685, 1.0524159871638985, 1.5062716680875239, 1.923724227793608, 2.3048701942781795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.050243377685547})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.230876445770264})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.268621444702148})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 7.106849670410156})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.197824954986572})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.16111421585083})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.876392841339111})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.354519844055176})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.516901969909668})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.24934695759065764, 'crossentropy': 5.8825117883758455}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 29873], ['ood', 34577], ['ood', 23422], ['id', 43966], ['id', 7196]], 'labels': [-1, -1, -1, 1, 2], 'scores': [0.6203515542338172, 1.1827707357050223, 1.68274560731814, 2.1215023679912273, 2.5184989577041383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.138064384460449})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.912820339202881})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.849250793457031})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.921014308929443})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.996807098388672})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.934678554534912})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.60230827331543})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.21907652120467117, 'crossentropy': 6.063155443300553}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 155], ['id', 10533], ['id', 42278], ['ood', 37146], ['id', 15913]], 'labels': [-1, 5, 1, -1, 1], 'scores': [0.6117086953651083, 1.1394631387324408, 1.6372635886712263, 2.097348957107087, 2.487390191607277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.017110824584961})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.416788101196289})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.951327323913574})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.169144630432129})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.809704780578613})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.72882080078125})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.2233020897357099, 'crossentropy': 4.742956085298863}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 16942], ['id', 4602], ['ood', 24336], ['id', 18161], ['ood', 36569]], 'labels': [-1, 5, -1, 1, -1], 'scores': [0.5917336120255134, 1.157659082897914, 1.6742281335694047, 2.1159331758918505, 2.5129145555783614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.61474609375})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.698307991027832})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.7967987060546875})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.82144021987915})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.067383766174316})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.0520172119140625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.786449432373047})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.708819389343262})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.52569580078125})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.252919483712354, 'crossentropy': 4.903390238456515}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 15823], ['ood', 9242], ['id', 59514], ['id', 22897], ['ood', 10503]], 'labels': [3, -1, 4, 0, -1], 'scores': [0.6576669124590673, 1.2535405265224844, 1.770980862530089, 2.237438654658746, 2.6548936769439875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 5.69512939453125})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.916978359222412})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.795587539672852})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.117188930511475})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.203043460845947})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.016141891479492})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.585901260375977})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.065716743469238})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.382766246795654})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.245513916015625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.841388702392578})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.875962257385254})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.016518592834473})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.241559028625488})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.707347869873047})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.429424285888672})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.655913352966309})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.631925106048584})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.73307991027832})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.182952404022217})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.317999839782715})
store['active_learning_steps'][34]['training']['best_epoch']=18
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.23244468346650277, 'crossentropy': 5.622139338122311}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 46641], ['ood', 21463], ['ood', 37665], ['id', 53749], ['id', 45915]], 'labels': [-1, -1, -1, 3, 6], 'scores': [0.7872641295965472, 1.4034107800002875, 1.974502566474298, 2.474066763959831, 2.8975441318593216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.659088134765625})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.484531879425049})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.292797088623047})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 4.871509552001953})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.492890357971191})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.156634330749512})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.995553970336914})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.920015335083008})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.93653678894043})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.728912353515625})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.20555470190534728, 'crossentropy': 5.469722360940381}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 47968], ['ood', 1272], ['id', 64554], ['ood', 6875], ['id', 25250]], 'labels': [-1, -1, 3, -1, 1], 'scores': [0.8133527136205654, 1.4324709121950008, 1.955556638153023, 2.4010815967391537, 2.774692319763604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.793466567993164})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.0057220458984375})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.025601387023926})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.612981796264648})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.727436542510986})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.948151588439941})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.160467147827148})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.993606090545654})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.932365417480469})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.19683466502765826, 'crossentropy': 4.99796254369622}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 44320], ['id', 18487], ['id', 4456], ['ood', 38047], ['id', 9828]], 'labels': [-1, 5, 4, -1, 1], 'scores': [0.6982293520014777, 1.2796623078923375, 1.8167626711385605, 2.2825104701190053, 2.69556139594678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.180171966552734})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.244174003601074})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.184366703033447})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.532808303833008})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.727859020233154})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.678038597106934})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.2275660725261217, 'crossentropy': 4.913516597360941}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 25910], ['id', 40882], ['ood', 22349], ['id', 47395], ['id', 40874]], 'labels': [0, 0, -1, 7, 9], 'scores': [0.6409531994368513, 1.2265520310215878, 1.7759212929756707, 2.205484052654951, 2.57297319020281]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.56575870513916})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.512894630432129})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 7.330910682678223})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.039313316345215})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.570460319519043})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.506452560424805})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.402327537536621})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.697010040283203})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.547784328460693})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.22011370620774431, 'crossentropy': 6.5351064315073755}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 42513], ['id', 23202], ['ood', 38484], ['id', 38630], ['id', 48267]], 'labels': [-1, 4, -1, 7, 1], 'scores': [0.6436730334620502, 1.2463195980525237, 1.8061940896281161, 2.2466183825991948, 2.6371903184588366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.3653669357299805})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.547938823699951})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.714846611022949})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.625494480133057})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.20794153213501})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.959383010864258})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.75124979019165})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.479662895202637})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.2210740626920713, 'crossentropy': 5.365313004187154}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 36311], ['id', 57550], ['id', 554], ['id', 37018], ['ood', 13988]], 'labels': [-1, 6, 9, 8, -1], 'scores': [0.6636811251237358, 1.2345203234039497, 1.7374792957456586, 2.1965227341366775, 2.580356373698516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.902219295501709})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.628937721252441})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.899786949157715})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.500461578369141})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.79859733581543})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.70658016204834})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 6.225522518157959})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.058751106262207})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2212661339889367, 'crossentropy': 5.006176892862631}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 12012], ['ood', 5904], ['ood', 223], ['id', 35633], ['id', 30339]], 'labels': [8, -1, -1, 5, 5], 'scores': [0.6470358263286613, 1.2634406236753044, 1.7975543904844526, 2.2775541230726395, 2.6786140304069574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.83507776260376})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.377801895141602})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.736448287963867})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.466067790985107})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.0722198486328125})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.873918056488037})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.05167293548584})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.719299793243408})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.608780860900879})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.098352432250977})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.156660079956055})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.2476183159188691, 'crossentropy': 5.108528085625384}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 47243], ['id', 66068], ['ood', 28193], ['id', 58815], ['id', 13236]], 'labels': [-1, 3, -1, 6, 8], 'scores': [0.6785090784599896, 1.3244714808761362, 1.9085484644950141, 2.432559549015152, 2.857151428714202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.1008195877075195})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.276722431182861})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.4944610595703125})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.557724952697754})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.993606090545654})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.4242401123046875})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.629477500915527})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.917590618133545})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.689009666442871})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.924418926239014})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.765637397766113})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 5.478139400482178})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.801247596740723})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.8472089767456055})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.83179235458374})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 4.762557029724121})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.902027130126953})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.062562942504883})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.131728172302246})
store['active_learning_steps'][42]['training']['best_epoch']=16
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.2585279655808236, 'crossentropy': 4.885222394552858}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 29480], ['ood', 31945], ['ood', 46572], ['id', 7179], ['id', 39680]], 'labels': [-1, -1, -1, 6, 9], 'scores': [0.8418898061642912, 1.526287139690825, 2.0933798095409513, 2.5909409563023793, 3.025815315129396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.313093185424805})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.086198806762695})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.8313093185424805})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.33242130279541})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.080134868621826})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.0124969482421875})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.1571197509765625})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 5.165909767150879})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.92413854598999})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 5.037543296813965})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 5.7781476974487305})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 7.074037551879883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.01607608795166})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.2609096496619545, 'crossentropy': 5.390704829632759}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 62947], ['ood', 7183], ['ood', 24987], ['id', 22058], ['id', 30973]], 'labels': [3, -1, -1, 9, 1], 'scores': [0.7203762332647607, 1.4221256123421822, 1.9609297674312685, 2.4604646833526473, 2.8898784788898997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.105688095092773})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.13587760925293})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.858633518218994})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.128952980041504})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.797033309936523})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.8583526611328125})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.882280349731445})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.441680431365967})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.22368623232944068, 'crossentropy': 5.6369432333282115}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 22079], ['id', 64469], ['id', 13891], ['id', 30556], ['id', 60243]], 'labels': [8, 6, 8, 1, 2], 'scores': [0.6610321316629235, 1.2430776825444525, 1.7766807350019818, 2.275391659723601, 2.7067995543250927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.749571800231934})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.101436614990234})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.081181526184082})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.21580696105957})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.99585485458374})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.7301459312438965})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.497567176818848})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.23509526736324524, 'crossentropy': 5.163090139059619}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 70061], ['ood', 27774], ['ood', 40990], ['ood', 20554], ['id', 54232]], 'labels': [2, -1, -1, -1, 0], 'scores': [0.6434913500955557, 1.1948246526368882, 1.700663044292559, 2.138744163023084, 2.532710284669922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.819056987762451})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.600226402282715})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.907416343688965})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.892070770263672})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.966897010803223})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.268119812011719})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.93322229385376})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.841813087463379})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.119798183441162})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.933984756469727})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.563727378845215})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.131680488586426})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.2534956976029502, 'crossentropy': 5.219779982329441}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 18134], ['id', 41699], ['ood', 15775], ['id', 44997], ['id', 1017]], 'labels': [-1, 5, -1, 9, 6], 'scores': [0.705763447169709, 1.305565002121459, 1.8724564093342169, 2.357602047428548, 2.775125787551083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.639683723449707})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.659962177276611})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.098323822021484})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.6427154541015625})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.618676662445068})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.7245025634765625})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.176651954650879})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.2520359557467732, 'crossentropy': 4.4984358193761524}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 57757], ['id', 8025], ['id', 9028], ['id', 45225], ['id', 58890]], 'labels': [1, 6, 1, 6, 2], 'scores': [0.6097272676386114, 1.1014588142188417, 1.5620254516190837, 1.9874022169947363, 2.3778859028849544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.911005735397339})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.228428840637207})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.19418478012085})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.170280456542969})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.644530296325684})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.14933967590332})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.24884757221880763, 'crossentropy': 4.122463458435772}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 34193], ['id', 24414], ['ood', 5844], ['ood', 15805], ['id', 50354]], 'labels': [-1, 1, -1, -1, 0], 'scores': [0.6066367881323345, 1.0778344203556611, 1.5191033350135061, 1.897215849995888, 2.2408885006288557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.5248494148254395})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.23673152923584})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.19929313659668})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.157639503479004})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.837854385375977})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.611074447631836})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.91245174407959})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.019028186798096})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.08050012588501})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.282921020282729, 'crossentropy': 4.61185632106638}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 15235], ['ood', 44520], ['ood', 6831], ['ood', 9591], ['ood', 14277]], 'labels': [5, -1, -1, -1, -1], 'scores': [0.6879758669006961, 1.2977486894752097, 1.844860547722349, 2.308799979148601, 2.721133344021574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.849034309387207})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.484481334686279})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.3814697265625})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.68528413772583})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.206087589263916})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.425083160400391})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.557146072387695})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 4.6612138748168945})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.855145454406738})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.256275653839111})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.707875728607178})
store['active_learning_steps'][50]['training']['best_epoch']=8
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.30020743700061464, 'crossentropy': 4.699668917102028}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 26576], ['id', 11607], ['id', 42476], ['id', 47095], ['ood', 29055]], 'labels': [2, 5, 6, 0, -1], 'scores': [0.6497335313954633, 1.205324736895104, 1.7203254362301594, 2.191846594321026, 2.577035007485321]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.375650405883789})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.84766960144043})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.4097580909729})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.736856460571289})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.05152702331543})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.0751237869262695})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.24177934849416102, 'crossentropy': 4.302679754724954}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 33793], ['ood', 30088], ['id', 42521], ['ood', 19168], ['id', 41647]], 'labels': [8, -1, 1, -1, 1], 'scores': [0.6301806015578055, 1.2502179566973401, 1.7404389322536327, 2.167618614311648, 2.5426330453675305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.8109493255615234})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.622447967529297})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.830262660980225})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.617969989776611})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.697832107543945})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.641984462738037})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.479577541351318})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.25311155500921945, 'crossentropy': 4.637055474992317}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 9335], ['id', 35796], ['id', 13702], ['id', 11804], ['id', 54907]], 'labels': [-1, 7, 2, 9, 8], 'scores': [0.6553371218184645, 1.191302978495889, 1.6903477939476117, 2.124784553869782, 2.508549395606286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.5212628841400146})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.155269145965576})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.463461399078369})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.1228742599487305})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.565634250640869})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.470287322998047})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.987814903259277})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.801494121551514})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.854733467102051})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.962735652923584})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.442106246948242})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.282286167144775})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.362269401550293})
store['active_learning_steps'][53]['training']['best_epoch']=10
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.2609096496619545, 'crossentropy': 5.37347303318992}
