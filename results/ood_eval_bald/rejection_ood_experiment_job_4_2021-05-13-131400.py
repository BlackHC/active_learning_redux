store = {}
store['timestamp']=1620908041
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=4']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=4
store['worker_id']=4
store['num_workers']=20
store['config']={'seed': 1240, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.504276990890503})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3698782920837402})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.887885570526123})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.925203800201416})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9974164962768555})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6982, 'crossentropy': 2.15694375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.176171898841858})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1046385765075684})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0906438827514648})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0906240940093994})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [41556, 10475, 9154, 41108, 37238, 23101, 31995, 11219, 39483, 18171], 'labels': [0, 6, 8, 0, 6, 3, 0, -1, 0, 0], 'scores': [1.0104324221611023, 0.902738094329834, 0.9603103399276733, 0.8383510112762451, 0.6826158165931702, 0.5652449429035187, 0.9649966359138489, 0.5965112447738647, 0.8915862441062927, 0.7423405647277832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.483182430267334})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7948484420776367})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.9467825889587402})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.164149761199951})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6469, 'crossentropy': 2.3496169921875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3987367153167725})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3175363540649414})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.298714280128479})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [56951, 10987, 42633, 18619, 5401, 56083, 14073, 9327, 48165, 47571], 'labels': [4, 5, 2, -1, 4, 2, 7, 7, 7, 4], 'scores': [0.6712634563446045, 0.6616414189338684, 0.6936387419700623, 0.6472415328025818, 0.8053240776062012, 0.6163039803504944, 0.8232454657554626, 0.7751207947731018, 0.6581179201602936, 0.6741970777511597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.7670676708221436})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.982267141342163})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.025838613510132})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.317124843597412})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7607, 'crossentropy': 1.56332255859375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.046541452407837})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9460577964782715})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.928002119064331})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [53162, 42417, 12069, 56776, 6075, 37270, 35766, 41092, 46012, 2748], 'labels': [-1, 8, -1, 3, 1, 5, 5, 8, -1, 2], 'scores': [0.5142532587051392, 0.4939860701560974, 0.4472007751464844, 0.49568426609039307, 0.6343846321105957, 0.6507093906402588, 0.6719167232513428, 0.5684501528739929, 0.3577558994293213, 0.6985860466957092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4133083820343018})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.5440351963043213})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.7700798511505127})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5901685953140259})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8064, 'crossentropy': 1.21712890625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9237685203552246})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8322540521621704})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.8613007068634033})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [51038, 19557, 28301, 28693, 27972, 40177, 19315, 32747, 10361, 10083], 'labels': [3, 8, 8, 3, 8, 9, 9, 8, 9, -1], 'scores': [0.54888916015625, 0.6583471894264221, 0.7186834216117859, 0.6701476573944092, 0.5487069487571716, 0.4362720847129822, 0.6418786644935608, 0.4781992435455322, 0.7718362212181091, 0.5175893306732178]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9879787564277649})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1740314960479736})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3571538925170898})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4340777397155762})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8426, 'crossentropy': 0.9015208984375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8052375912666321})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7221415042877197})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7150366306304932})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [8586, 22249, 19972, 56829, 53193, 52392, 23838, 48818, 27960, 36024], 'labels': [9, 2, 9, 9, 5, 1, 9, 9, 3, -1], 'scores': [0.7257593870162964, 0.5860742926597595, 0.7396532297134399, 0.5536937713623047, 0.4560997486114502, 0.47111833095550537, 0.5854806303977966, 0.44113367795944214, 0.3391638994216919, 0.4906240701675415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0238690376281738})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2882812023162842})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3906807899475098})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.3842999935150146})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8365, 'crossentropy': 0.91667607421875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8477615118026733})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7728790640830994})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7538496255874634})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [57331, 32774, 13533, 36339, 48384, 26779, 24245, 15188, 14728, 55968], 'labels': [2, 8, 5, 4, 9, 2, 0, 6, 8, 8], 'scores': [0.6553221940994263, 0.5920918583869934, 0.45679789781570435, 0.6069375872612, 0.7424155473709106, 0.5140784978866577, 0.5669196844100952, 0.41768574714660645, 0.5550875663757324, 0.5028743743896484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9558786749839783})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0224511623382568})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0698950290679932})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.031280279159546})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8363, 'crossentropy': 0.8830666015625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9181802868843079})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.754935085773468})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.7519466876983643})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [51561, 52891, 6725, 13622, 878, 20513, 47415, 31014, 19959, 25499], 'labels': [3, 3, 2, 6, -1, 9, -1, 8, 5, 6], 'scores': [0.305370569229126, 0.4897671937942505, 0.5207599401473999, 0.5176947116851807, 0.1847820281982422, 0.3273913860321045, 0.29277753829956055, 0.4179380536079407, 0.518510639667511, 0.3359661102294922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9364228248596191})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9154325127601624})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1040472984313965})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.236328125})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.072311282157898})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8794, 'crossentropy': 0.7820001953125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7365005016326904})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6077334880828857})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5850309133529663})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5736543536186218})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [1559, 42426, 33344, 30041, 1324, 29694, 13831, 34142, 6618, 11076], 'labels': [3, 9, 3, 3, 5, 7, 3, 7, -1, 7], 'scores': [0.4449889063835144, 0.3741641044616699, 0.39135539531707764, 0.4299706220626831, 0.5349408984184265, 0.5699762105941772, 0.5040396451950073, 0.6472736597061157, 0.3592582941055298, 0.39881396293640137]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7925517559051514})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7579115629196167})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7829123735427856})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8406699895858765})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.867504358291626})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8846, 'crossentropy': 0.69757392578125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6956826448440552})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6004558801651001})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5671809911727905})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5370954275131226})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [8283, 5000, 4420, 7819, 40259, 41585, 14645, 44281, 18998, 2765], 'labels': [7, 7, 1, 1, 8, 1, 8, 1, 2, 0], 'scores': [0.4777677655220032, 0.4439900517463684, 0.5094571113586426, 0.6206912994384766, 0.538806676864624, 0.560877799987793, 0.5578271150588989, 0.6136672496795654, 0.5178689360618591, 0.6133681535720825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8280466198921204})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7644317150115967})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8682520389556885})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8242117166519165})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.856452465057373})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8768, 'crossentropy': 0.732864501953125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8184854388237})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6103699803352356})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.5834496021270752})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5324400663375854})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [53114, 24944, 31847, 11999, 53316, 3692, 14715, 40905, 9533, 22549], 'labels': [5, 6, -1, 3, 5, 7, 4, -1, 6, 9], 'scores': [0.35683494806289673, 0.3788660764694214, 0.4477119445800781, 0.4282454252243042, 0.6364132761955261, 0.5644429922103882, 0.3976781368255615, 0.39690232276916504, 0.5270980000495911, 0.4073020815849304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7483021020889282})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7518863677978516})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6983497142791748})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8064923286437988})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8065742254257202})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9246888756752014})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.613468310546875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6367276906967163})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.49252933263778687})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4753536581993103})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4704931080341339})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4375377297401428})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [24740, 56048, 27066, 12666, 5574, 42746, 28313, 47280, 45917, 20672], 'labels': [8, -1, -1, -1, 8, 2, 9, -1, 9, -1], 'scores': [0.6052390336990356, 0.512670636177063, 0.43164145946502686, 0.38894903659820557, 0.3569561243057251, 0.9775802493095398, 0.609107494354248, 0.24911713600158691, 0.5952719449996948, 0.4908686876296997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9310839176177979})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7918649911880493})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8957605361938477})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8944871425628662})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9090707302093506})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8884, 'crossentropy': 0.69551689453125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7726438045501709})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5886817574501038})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5400948524475098})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.5685297846794128})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [45801, 12919, 26079, 51261, 4877, 12744, 21491, 35688, 18896, 43978], 'labels': [3, 6, 8, 4, -1, 6, 4, 3, 0, 3], 'scores': [0.3921382427215576, 0.4426596164703369, 0.39138728380203247, 0.4736397862434387, 0.2878401279449463, 0.647681713104248, 0.43047958612442017, 0.47435301542282104, 0.2813968360424042, 0.3607640564441681]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8078759908676147})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6943913698196411})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6858059167861938})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7513858675956726})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7891829013824463})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8120956420898438})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.6128197265625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8088464736938477})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5088903903961182})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.507734477519989})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4841187596321106})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4594193696975708})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [15399, 36421, 53324, 45626, 28956, 12607, 20944, 14749, 31404, 19101], 'labels': [0, 3, 9, 7, -1, -1, 2, 0, 3, 3], 'scores': [0.5565161108970642, 0.33573710918426514, 0.5922986268997192, 0.45972585678100586, 0.38413143157958984, 0.2766040563583374, 0.4426826238632202, 0.6349819302558899, 0.60934978723526, 0.5419915318489075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8129948377609253})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.623815655708313})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6900033354759216})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7429189682006836})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7414731979370117})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9027, 'crossentropy': 0.60199248046875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7263843417167664})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5896590352058411})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5716243386268616})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5262166261672974})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [5968, 29180, 32880, 43537, 15386, 53376, 19842, 59753, 45788, 8867], 'labels': [7, 9, 0, 3, 6, 3, 7, 4, -1, 8], 'scores': [0.5120444297790527, 0.3910354971885681, 0.5009649991989136, 0.5051102638244629, 0.4891011118888855, 0.267633855342865, 0.5461632013320923, 0.40740567445755005, 0.2747352123260498, 0.2845960259437561]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7923917770385742})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6099963188171387})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6368302702903748})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5907204151153564})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6376782655715942})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6405972242355347})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.682878851890564})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.5499185546875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6912168264389038})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5165532827377319})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4540427029132843})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42303138971328735})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4489578902721405})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.42970699071884155})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [80, 40380, 48330, 35425, 5336, 13436, 16022, 31637, 30585, 13038], 'labels': [9, -1, 9, 4, -1, -1, 8, 5, -1, -1], 'scores': [0.5565624833106995, 0.439214825630188, 0.5914632081985474, 0.6116633117198944, 0.43337756395339966, 0.518541157245636, 0.6318500638008118, 0.5801746845245361, 0.38101285696029663, 0.41098880767822266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7153704166412354})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5472761392593384})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6068823933601379})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6704795360565186})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5796349048614502})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9206, 'crossentropy': 0.513861669921875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6872291564941406})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5440973043441772})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5364459753036499})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4918432831764221})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [23964, 22049, 49751, 14964, 32231, 28194, 38315, 18239, 45622, 50841], 'labels': [8, -1, 8, -1, -1, -1, 0, -1, 6, 4], 'scores': [0.3822190761566162, 0.40541279315948486, 0.32408416271209717, 0.3827873468399048, 0.33930110931396484, 0.33100366592407227, 0.26590496301651, 0.35219311714172363, 0.472774863243103, 0.4308912754058838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8194218277931213})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5706811547279358})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5829440355300903})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6310198307037354})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6266881227493286})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.5576576171875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6955541372299194})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5412139892578125})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.47282809019088745})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5434532165527344})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [56712, 44875, 49470, 42322, 57770, 21315, 38503, 5740, 17679, 16986], 'labels': [5, 8, 5, 5, 6, 8, -1, 9, 8, 7], 'scores': [0.4624179005622864, 0.29474592208862305, 0.35983961820602417, 0.5385069847106934, 0.2662675380706787, 0.4021680951118469, 0.22560477256774902, 0.4857027530670166, 0.4698265790939331, 0.2754707336425781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9036778211593628})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5597022175788879})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5293790102005005})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5560126304626465})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5583045482635498})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5563077330589294})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.52092802734375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7411488890647888})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5280137062072754})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.45843684673309326})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5117302536964417})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4585464894771576})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [12268, 57972, 1248, 19368, 35066, 57982, 51432, 3360, 20830, 17603], 'labels': [8, 4, 4, 3, 3, 5, 1, -1, 9, 0], 'scores': [0.3943920135498047, 0.6058915853500366, 0.4823581576347351, 0.363090455532074, 0.3894166350364685, 0.4141739010810852, 0.3219771981239319, 0.2413017749786377, 0.3257725238800049, 0.4182794690132141]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8271315693855286})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5849751830101013})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5407946109771729})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5647906064987183})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.538111686706543})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6313685178756714})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5623422861099243})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6291314363479614})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.51161796875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6979759931564331})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4921315312385559})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40421611070632935})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3810271620750427})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3892304599285126})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.35590803623199463})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34640389680862427})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [44883, 13259, 5370, 21445, 12525, 26389, 31786, 6011, 6930, 47870], 'labels': [-1, 1, 3, 9, 4, 0, 9, -1, 6, 9], 'scores': [0.2868584394454956, 0.5541642308235168, 0.6347693204879761, 0.6141754388809204, 0.5355939865112305, 0.5342499017715454, 0.48480886220932007, 0.4343007206916809, 0.5249638557434082, 0.4881889820098877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8213886022567749})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5533332228660583})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5474977493286133})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5082887411117554})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5276159048080444})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5471396446228027})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.575653076171875})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.468738232421875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7320946455001831})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5131615400314331})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4550398290157318})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.39920711517333984})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.37588417530059814})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3854425549507141})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [31335, 44286, 20037, 56466, 58653, 40158, 20853, 33150, 7967, 55639], 'labels': [5, 8, 8, 9, 5, 8, 5, 8, 5, 5], 'scores': [0.803520143032074, 0.5759907364845276, 0.5777292847633362, 0.2816014587879181, 0.6234759092330933, 0.5741705298423767, 0.5972651839256287, 0.5868870615959167, 0.6200329065322876, 0.4944005012512207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8873127698898315})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5592639446258545})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5212023258209229})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49248021841049194})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44695109128952026})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5205711126327515})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5362385511398315})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5003652572631836})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9438, 'crossentropy': 0.413457421875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7336993217468262})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4785187542438507})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.39213037490844727})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3513241410255432})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3629879057407379})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.35925325751304626})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34120553731918335})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [20964, 3318, 47211, 56084, 5013, 11411, 34697, 8978, 30806, 35372], 'labels': [-1, -1, -1, -1, 2, -1, -1, 2, -1, -1], 'scores': [0.394084095954895, 0.3894752860069275, 0.2870149612426758, 0.4022955894470215, 0.5694889426231384, 0.3229907751083374, 0.3729345202445984, 0.4307768940925598, 0.4852246046066284, 0.44538748264312744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9254512786865234})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5569890737533569})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5809043645858765})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5087639093399048})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5768669843673706})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5770050883293152})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5763366222381592})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9392, 'crossentropy': 0.4497685546875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8289103507995605})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4654451310634613})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4131300151348114})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.39653480052948})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3782801032066345})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3930165767669678})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [491, 23094, 9380, 19998, 5157, 28371, 39963, 32521, 4590, 602], 'labels': [-1, 7, 3, -1, 5, 3, 4, -1, 5, 8], 'scores': [0.40434348583221436, 0.4717504382133484, 0.8660438656806946, 0.40783190727233887, 0.38370704650878906, 0.5945518016815186, 0.5853886008262634, 0.29968923330307007, 0.5360627174377441, 0.5368661284446716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0372282266616821})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5154255628585815})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48069053888320923})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4897432327270508})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49806368350982666})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4753763675689697})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5070565342903137})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5287212133407593})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5157302021980286})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.457421630859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6837005615234375})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4862961769104004})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4594082236289978})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.41358131170272827})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.40306156873703003})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.38804057240486145})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.388746440410614})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.35246944427490234})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [26358, 10520, 52886, 13085, 42384, 527, 46860, 943, 45797, 59339], 'labels': [3, -1, 7, 6, 8, 0, 0, 0, 5, 1], 'scores': [0.5384483337402344, 0.4645443558692932, 0.5289469957351685, 0.6694735884666443, 0.5652741193771362, 0.6732596755027771, 0.44771474599838257, 0.5617528557777405, 0.4611355662345886, 0.40426039695739746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9159245491027832})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5134179592132568})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5032527446746826})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46542680263519287})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43801599740982056})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5825154185295105})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45292389392852783})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5164526700973511})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.44140693359375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6886441707611084})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.46707746386528015})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.43163007497787476})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4116259813308716})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36303040385246277})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36272138357162476})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.33535802364349365})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [17494, 9136, 10544, 11734, 27912, 59447, 45121, 56586, 27998, 54195], 'labels': [5, -1, 7, 8, -1, 8, 4, 5, -1, 8], 'scores': [0.5011295080184937, 0.380004346370697, 0.43613290786743164, 0.5758700966835022, 0.3522965908050537, 0.4087773561477661, 0.51307213306427, 0.5594877004623413, 0.5048115253448486, 0.546555757522583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0253212451934814})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5412269830703735})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5234098434448242})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4499359428882599})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5341669321060181})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.478307843208313})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5086629390716553})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.945, 'crossentropy': 0.424440380859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7555720806121826})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4894977807998657})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3910982012748718})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3515456020832062})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3582117557525635})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3786482512950897})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [21161, 34570, 46627, 28844, 33693, 15062, 28784, 4004, 3374, 26405], 'labels': [-1, -1, 0, 2, -1, -1, -1, 5, 9, 9], 'scores': [0.3667330741882324, 0.2513623833656311, 0.4935356378555298, 0.5522329211235046, 0.407204270362854, 0.2812156677246094, 0.41670238971710205, 0.4647040367126465, 0.48291683197021484, 0.3596974015235901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9394450187683105})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5419002771377563})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43871697783470154})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43842649459838867})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45415154099464417})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42476338148117065})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44505006074905396})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43669384717941284})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4703316390514374})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.411721728515625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7622320055961609})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.478655606508255})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38087552785873413})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3520752191543579})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3560720682144165})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3567824363708496})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3261439800262451})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3070215880870819})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [6286, 3034, 31375, 2284, 9407, 32271, 42866, 23384, 14309, 1091], 'labels': [-1, -1, -1, -1, -1, -1, 2, 5, -1, -1], 'scores': [0.46433985233306885, 0.30349206924438477, 0.4291940927505493, 0.3388916850090027, 0.5992932915687561, 0.2522777318954468, 0.3389877378940582, 0.479275107383728, 0.48657774925231934, 0.4434744119644165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8787615895271301})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5190515518188477})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42636919021606445})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4424886703491211})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4389864504337311})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4958290755748749})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.4025359375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7829992771148682})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5253056883811951})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41292738914489746})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37813133001327515})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42586439847946167})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [8443, 36784, 44296, 24171, 48401, 22313, 50908, 368, 611, 29958], 'labels': [2, -1, 1, -1, -1, -1, -1, 8, 7, -1], 'scores': [0.39807575941085815, 0.4070773124694824, 0.2561647295951843, 0.3029855489730835, 0.3288707733154297, 0.3622843027114868, 0.371753454208374, 0.3149205446243286, 0.31790024042129517, 0.45905327796936035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8646676540374756})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5115818977355957})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4441910982131958})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4363356828689575})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4529396593570709})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38721638917922974})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4379209280014038})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4446566104888916})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4650869369506836})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.39565615234375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.715729296207428})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4346897006034851})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4020737409591675})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35871005058288574})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3356594443321228})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.30968910455703735})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2988089323043823})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3200206756591797})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [7638, 56104, 50297, 47609, 228, 10979, 45439, 5679, 28779, 31919], 'labels': [8, -1, 3, -1, 3, -1, 2, 3, -1, 9], 'scores': [0.4963579773902893, 0.4360496997833252, 0.3620593845844269, 0.3887038230895996, 0.5985926389694214, 0.41358137130737305, 0.47173458337783813, 0.4760373830795288, 0.3757575750350952, 0.6063523292541504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.915680468082428})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47302407026290894})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4090462923049927})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4053995609283447})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4839114546775818})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4214010238647461})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44045114517211914})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9462, 'crossentropy': 0.3951427978515625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7473917007446289})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5007444024085999})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41357165575027466})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3978671431541443})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34605926275253296})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.354370653629303})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [39714, 262, 37574, 1136, 56348, 31771, 12196, 44363, 53854, 22717], 'labels': [-1, 2, 5, 6, -1, -1, 2, 0, 8, 3], 'scores': [0.22258466482162476, 0.594576358795166, 0.48396384716033936, 0.4118943214416504, 0.3019665479660034, 0.22956335544586182, 0.5643936395645142, 0.35474300384521484, 0.6259351968765259, 0.38800978660583496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.067772388458252})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5184204578399658})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4499402642250061})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3964884579181671})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41362082958221436})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40897202491760254})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4145169258117676})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9429, 'crossentropy': 0.3926324462890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8181928396224976})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5185632705688477})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42679792642593384})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3675915002822876})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3868453800678253})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3338850736618042})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [34542, 23370, 25546, 37782, 17231, 50562, 17895, 39363, 50505, 46689], 'labels': [1, 2, 8, -1, 4, 9, 2, -1, -1, 3], 'scores': [0.4634819030761719, 0.26658618450164795, 0.4899476170539856, 0.26095426082611084, 0.34176117181777954, 0.3561829924583435, 0.42842862010002136, 0.23786211013793945, 0.21588176488876343, 0.25607556104660034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1663641929626465})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5600097179412842})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4006482660770416})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48479604721069336})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4596288800239563})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4215041697025299})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.948, 'crossentropy': 0.4090434326171875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7310361862182617})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.489287793636322})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4502103328704834})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.438182532787323})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38860565423965454})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [23452, 25910, 15737, 33630, 46017, 30130, 32173, 43040, 42638, 10260], 'labels': [5, 1, 7, 4, 0, 3, 7, 2, 4, 3], 'scores': [0.3271239995956421, 0.49285078048706055, 0.5243488550186157, 0.3274196684360504, 0.4961373805999756, 0.4460750222206116, 0.646675705909729, 0.37909215688705444, 0.49663060903549194, 0.31086933612823486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0177682638168335})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4602354168891907})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35242339968681335})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3875510096549988})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3872056007385254})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3617922067642212})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9503, 'crossentropy': 0.36053916015625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7341510057449341})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4919624328613281})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41861119866371155})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4024975299835205})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3619680404663086})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [19132, 18423, 12440, 29705, 55488, 37048, 35864, 39300, 52808, 5828], 'labels': [2, 2, 9, 5, 3, 9, 5, -1, 8, 5], 'scores': [0.3582058548927307, 0.41961050033569336, 0.2658578157424927, 0.5061287879943848, 0.37604397535324097, 0.4051967263221741, 0.39274072647094727, 0.23312973976135254, 0.33706414699554443, 0.3281099796295166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.878791093826294})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45720210671424866})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3742385506629944})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38791030645370483})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36390429735183716})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41075050830841064})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38298213481903076})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40480631589889526})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9542, 'crossentropy': 0.3612923828125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7385789155960083})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4430615305900574})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3728911280632019})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3052157759666443})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33017510175704956})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3167332410812378})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.313862681388855})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [45491, 12977, 9748, 15900, 17503, 9133, 43760, 55392, 7386, 5888], 'labels': [5, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5419816374778748, 0.4324827194213867, 0.471423864364624, 0.34219563007354736, 0.4188944101333618, 0.4567760229110718, 0.4701259136199951, 0.43327152729034424, 0.48223376274108887, 0.3387850522994995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8862506151199341})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45761555433273315})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36340099573135376})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34412717819213867})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34680676460266113})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3704352378845215})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3719087243080139})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.31631123046875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.786853551864624})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42916691303253174})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34593889117240906})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33811724185943604})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.35327786207199097})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3136812746524811})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [27988, 1832, 56004, 21378, 7621, 23418, 49849, 47814, 19597, 16301], 'labels': [-1, -1, -1, -1, 7, -1, -1, 4, 9, 8], 'scores': [0.3910667896270752, 0.47414517402648926, 0.29078805446624756, 0.3530430793762207, 0.4295656681060791, 0.35863006114959717, 0.29797667264938354, 0.19201645255088806, 0.33564698696136475, 0.45291662216186523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8785255551338196})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46902626752853394})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4019126296043396})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3492845892906189})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37160706520080566})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3834151029586792})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4093117117881775})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9512, 'crossentropy': 0.3457072509765625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7656788229942322})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45616576075553894})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3640972375869751})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35183340311050415})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3413695693016052})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.323873907327652})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [50767, 51984, 24943, 38408, 18572, 5079, 21130, 55739, 46369, 31184], 'labels': [-1, -1, 3, 5, 0, -1, -1, 5, 5, 9], 'scores': [0.46352386474609375, 0.4149223566055298, 0.41596484184265137, 0.28368079662323, 0.4612038731575012, 0.508457362651825, 0.44905877113342285, 0.43793195486068726, 0.33563733100891113, 0.5177282691001892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.065791368484497})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5331979990005493})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40335020422935486})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.44622498750686646})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3543708920478821})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3730824589729309})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3621038794517517})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38424545526504517})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9546, 'crossentropy': 0.3563981689453125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8173778057098389})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5326113700866699})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36362648010253906})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3301185667514801})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3279566764831543})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34485793113708496})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28914928436279297})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [34090, 3386, 16989, 40378, 48340, 29667, 9736, 30893, 20623, 36744], 'labels': [9, -1, 2, 7, -1, 2, 2, -1, 9, 1], 'scores': [0.4136534333229065, 0.3975931406021118, 0.44967812299728394, 0.6337295770645142, 0.5818449258804321, 0.5848888158798218, 0.3890736997127533, 0.4228363037109375, 0.48394280672073364, 0.665696382522583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9478552937507629})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4967406392097473})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3882882297039032})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33807405829429626})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37180519104003906})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3492271304130554})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3616917133331299})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.33494755859375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7490309476852417})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46266013383865356})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39489108324050903})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.380760133266449})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3670005202293396})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3321853280067444})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [54771, 32657, 59701, 27509, 11193, 44985, 28362, 47626, 47729, 49651], 'labels': [-1, -1, 5, 1, -1, -1, 7, -1, 1, -1], 'scores': [0.3839048147201538, 0.28608453273773193, 0.4215511679649353, 0.48213064670562744, 0.41349709033966064, 0.39562398195266724, 0.5615154504776001, 0.4836881160736084, 0.34489673376083374, 0.39253830909729004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0803635120391846})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49399110674858093})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38417237997055054})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3485395312309265})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3116811513900757})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36990562081336975})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39508479833602905})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4005918502807617})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.31103193359375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8202526569366455})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4941715896129608})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38590866327285767})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35417479276657104})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34369993209838867})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32693004608154297})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2734666168689728})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [8300, 43444, 44570, 6292, 36614, 22884, 50939, 33612, 22491, 31114], 'labels': [8, -1, 7, -1, -1, 2, -1, 7, 2, 4], 'scores': [0.46554845571517944, 0.4028257131576538, 0.4792172908782959, 0.36931174993515015, 0.3895695209503174, 0.4605008363723755, 0.32746362686157227, 0.2873232364654541, 0.45361971855163574, 0.4736194610595703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.1380436420440674})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5875797271728516})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.436480313539505})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4008229374885559})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3578028082847595})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3541055917739868})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3482096493244171})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34544920921325684})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35444366931915283})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3265179395675659})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37557560205459595})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38125601410865784})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3821994662284851})
store['active_learning_steps'][38]['training']['best_epoch']=10
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.3039353271484375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7025389671325684})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44566231966018677})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37289494276046753})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31063467264175415})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3052945137023926})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28550446033477783})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27749764919281006})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2610098123550415})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2555263638496399})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29345449805259705})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24267913401126862})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.24609971046447754})
store['active_learning_steps'][38]['eval_training']['best_epoch']=11
store['active_learning_steps'][38]['acquisition']={'indices': [9899, 27248, 51527, 30974, 33215, 20587, 24866, 9179, 5361, 13343], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4534912109375, 0.3504422903060913, 0.4402930736541748, 0.33825623989105225, 0.3979761600494385, 0.5286303758621216, 0.5506199598312378, 0.36008816957473755, 0.36810970306396484, 0.3996843099594116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1193264722824097})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5188708305358887})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4084474444389343})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3288005590438843})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34587353467941284})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35657772421836853})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35520967841148376})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9603, 'crossentropy': 0.302673681640625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8606323003768921})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4610939025878906})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41757652163505554})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3801485300064087})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3496418595314026})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3093773424625397})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [23190, 17157, 23081, 44109, 34464, 25897, 37403, 998, 24479, 42774], 'labels': [-1, -1, -1, 1, -1, -1, 2, 3, 8, 4], 'scores': [0.369784951210022, 0.4419670104980469, 0.3213372230529785, 0.4618889093399048, 0.39442265033721924, 0.42325568199157715, 0.3199424147605896, 0.4494725465774536, 0.6938483715057373, 0.509299635887146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1407358646392822})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.525713324546814})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3813004195690155})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3703528642654419})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3441551625728607})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3471607565879822})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38716262578964233})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33068788051605225})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3477165102958679})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36545711755752563})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3565511703491211})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9609, 'crossentropy': 0.3193837890625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8106688261032104})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42947864532470703})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3540894389152527})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34032803773880005})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.309603750705719})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2737486660480499})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2964922785758972})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27743178606033325})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26575803756713867})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28206998109817505})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [34946, 6176, 28674, 54629, 11708, 6846, 25883, 42914, 51054, 8202], 'labels': [8, -1, 9, -1, 3, 2, -1, 3, 3, 2], 'scores': [0.7055664658546448, 0.3057897090911865, 0.3495241105556488, 0.523361086845398, 0.4779197573661804, 0.4939796030521393, 0.22846496105194092, 0.4330952763557434, 0.6617560386657715, 0.5763558745384216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0433017015457153})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47560396790504456})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3639777898788452})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35821568965911865})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33614811301231384})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33657190203666687})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33877620100975037})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36610856652259827})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.294685888671875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8629266023635864})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4509199261665344})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41453585028648376})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3459942936897278})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3135940432548523})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31324368715286255})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32036423683166504})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [706, 43367, 11175, 57802, 2245, 5298, 37004, 17091, 15728, 34362], 'labels': [-1, -1, -1, -1, -1, 0, 5, 4, 9, -1], 'scores': [0.44091010093688965, 0.46685314178466797, 0.3952435255050659, 0.417047381401062, 0.3781569004058838, 0.4653235673904419, 0.4406888484954834, 0.3169482350349426, 0.40330731868743896, 0.35288095474243164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9891953468322754})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49558815360069275})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4243479073047638})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35942429304122925})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3681398630142212})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40197694301605225})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35609132051467896})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3670206367969513})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4041047990322113})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38149797916412354})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.96, 'crossentropy': 0.3153068115234375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9089378118515015})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4576995074748993})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3728829324245453})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34593039751052856})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28537067770957947})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2786475718021393})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29055702686309814})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31047481298446655})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.26292383670806885})
store['active_learning_steps'][42]['eval_training']['best_epoch']=9
store['active_learning_steps'][42]['acquisition']={'indices': [20088, 42078, 29828, 10350, 17869, 2512, 33824, 5440, 4542, 27603], 'labels': [0, 4, -1, -1, 5, -1, 4, 5, -1, -1], 'scores': [0.23720282316207886, 0.7362145781517029, 0.4621286392211914, 0.5033882856369019, 0.3857190012931824, 0.37776780128479004, 0.42702072858810425, 0.440889835357666, 0.42500102519989014, 0.2893129587173462]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.012317180633545})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4880841076374054})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41313695907592773})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32845762372016907})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3250414729118347})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3117738664150238})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3358696699142456})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36174511909484863})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3591713309288025})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.2844272216796875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8489401936531067})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47764652967453003})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42916643619537354})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3139744997024536})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34159332513809204})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3114432692527771})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30545568466186523})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29159465432167053})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [19702, 4050, 29185, 29108, 991, 34846, 54038, 57334, 18202, 2412], 'labels': [5, -1, 3, -1, 4, 3, 9, 7, 4, 5], 'scores': [0.45768213272094727, 0.4390662908554077, 0.46226850152015686, 0.3897619843482971, 0.40881359577178955, 0.3756713271141052, 0.5483198761940002, 0.4821735620498657, 0.5884740352630615, 0.43786388635635376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2744276523590088})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5979577302932739})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4080837368965149})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3687256872653961})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33956360816955566})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3152114748954773})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35214632749557495})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3733746111392975})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35539600253105164})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.288521826171875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7991026639938354})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5354331135749817})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4100878834724426})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3482920527458191})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3323814868927002})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33384793996810913})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29981228709220886})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32618916034698486})
store['active_learning_steps'][44]['eval_training']['best_epoch']=7
store['active_learning_steps'][44]['acquisition']={'indices': [45642, 2525, 2118, 16011, 17576, 50736, 48807, 14423, 44583, 3891], 'labels': [-1, -1, 7, 5, -1, -1, -1, 6, -1, -1], 'scores': [0.2865089178085327, 0.43270862102508545, 0.3714905083179474, 0.5705605149269104, 0.39938485622406006, 0.46657222509384155, 0.45697927474975586, 0.5555897355079651, 0.40069055557250977, 0.30333685874938965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.089066743850708})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5109341740608215})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3659057021141052})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3441716134548187})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28755128383636475})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34270069003105164})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3077581524848938})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30145663022994995})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2747660888671875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8171439170837402})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4852473735809326})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41844114661216736})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.372283399105072})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32778558135032654})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2927180230617523})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2779906988143921})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [14654, 42504, 25801, 46187, 24947, 23350, 53491, 24575, 54568, 38308], 'labels': [-1, 8, -1, 3, -1, 8, -1, -1, -1, -1], 'scores': [0.4537290334701538, 0.4224834442138672, 0.45414984226226807, 0.5065793395042419, 0.4884706735610962, 0.5194590091705322, 0.4378080368041992, 0.3753093481063843, 0.40513235330581665, 0.3714998960494995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9625489711761475})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5443089008331299})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35476309061050415})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3256908655166626})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3315567970275879})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3388689160346985})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3428044319152832})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.291869873046875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8980117440223694})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48782965540885925})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4070362448692322})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38337647914886475})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35494112968444824})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3151448369026184})
store['active_learning_steps'][46]['eval_training']['best_epoch']=6
store['active_learning_steps'][46]['acquisition']={'indices': [30897, 32018, 31177, 37183, 22188, 38764, 40707, 6208, 37759, 55190], 'labels': [3, 8, -1, -1, -1, 1, -1, -1, -1, 3], 'scores': [0.38751888275146484, 0.39094769954681396, 0.45847487449645996, 0.470991849899292, 0.38407498598098755, 0.2788257598876953, 0.43722331523895264, 0.3091568946838379, 0.3600045442581177, 0.48395752906799316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0567244291305542})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.549168586730957})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3965029716491699})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3500674068927765})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30928656458854675})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3596058785915375})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32275712490081787})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3314993381500244})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2849452392578125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8309771418571472})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47091370820999146})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4252254366874695})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3116929531097412})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33679327368736267})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2781967520713806})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3115430176258087})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [47078, 13827, 25716, 59854, 36281, 13276, 4507, 27067, 11068, 42511], 'labels': [-1, 3, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.3944913148880005, 0.4439639449119568, 0.5546538829803467, 0.37742769718170166, 0.4287372827529907, 0.472123920917511, 0.3551473617553711, 0.34875500202178955, 0.37722277641296387, 0.4011063575744629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.9461158514022827})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5333819389343262})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3705081343650818})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35639697313308716})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34965330362319946})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3293263912200928})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3327036499977112})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3210115432739258})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33830490708351135})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3726448714733124})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3517129123210907})
store['active_learning_steps'][48]['training']['best_epoch']=8
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2783359375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7744048833847046})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4993373453617096})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3442109227180481})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32922083139419556})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2920635938644409})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27176010608673096})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30455148220062256})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2721557021141052})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2517034113407135})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24231648445129395})
store['active_learning_steps'][48]['eval_training']['best_epoch']=10
store['active_learning_steps'][48]['acquisition']={'indices': [3933, 49250, 31847, 28512, 37280, 31549, 34314, 46730, 22731, 9474], 'labels': [-1, 8, -1, 5, -1, -1, 7, -1, -1, -1], 'scores': [0.4436483383178711, 0.3979051113128662, 0.49067455530166626, 0.681085854768753, 0.4463016390800476, 0.4270194172859192, 0.4486026167869568, 0.48194873332977295, 0.44755685329437256, 0.4366244077682495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.048804521560669})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49649566411972046})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3818596303462982})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3204047679901123})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29693013429641724})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2966097593307495})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2730500400066376})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3215073347091675})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3244202136993408})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31100887060165405})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.268669140625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8793962001800537})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4272945523262024})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36617016792297363})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32861995697021484})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2838285565376282})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29231148958206177})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2766307592391968})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27519696950912476})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2822189927101135})
store['active_learning_steps'][49]['eval_training']['best_epoch']=8
store['active_learning_steps'][49]['acquisition']={'indices': [43948, 4226, 17036, 5694, 52899, 42554, 34438, 35453, 21481, 56027], 'labels': [-1, 7, -1, -1, 7, -1, -1, -1, -1, -1], 'scores': [0.46721434593200684, 0.44879835844039917, 0.3913148045539856, 0.660174548625946, 0.5409422516822815, 0.4457913637161255, 0.6168737411499023, 0.49464356899261475, 0.6049548983573914, 0.48036396503448486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2148795127868652})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6336836814880371})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3940437436103821})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3401442766189575})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3538140654563904})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2832260727882385})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35338690876960754})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3599244952201843})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3153608441352844})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2933977783203125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8472835421562195})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4726462960243225})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3954094648361206})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.359255313873291})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32351887226104736})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2936880588531494})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2697722911834717})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3220224976539612})
store['active_learning_steps'][50]['eval_training']['best_epoch']=7
store['active_learning_steps'][50]['acquisition']={'indices': [19937, 37582, 31705, 4692, 22470, 26174, 37742, 36206, 44910, 48611], 'labels': [-1, -1, -1, 8, -1, -1, -1, -1, -1, -1], 'scores': [0.5407475233078003, 0.47796088457107544, 0.3316843509674072, 0.4797380566596985, 0.4257180690765381, 0.5972313284873962, 0.5357769727706909, 0.3849952220916748, 0.4999849796295166, 0.34541428089141846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9943743944168091})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5030272006988525})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35916024446487427})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.316180020570755})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30900439620018005})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31703317165374756})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32132208347320557})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31788527965545654})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.279633544921875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9320926666259766})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4383704662322998})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41550928354263306})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3250836730003357})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3097107410430908})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2897223234176636})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2841160297393799})
store['active_learning_steps'][51]['eval_training']['best_epoch']=7
store['active_learning_steps'][51]['acquisition']={'indices': [40752, 55219, 32583, 9996, 32229, 2670, 26852, 38316, 47321, 42703], 'labels': [3, -1, -1, -1, -1, -1, 8, 4, 2, 0], 'scores': [0.4964367151260376, 0.2837313413619995, 0.42781561613082886, 0.17055046558380127, 0.3738691806793213, 0.33350861072540283, 0.4866485595703125, 0.6527942419052124, 0.4219893217086792, 0.6034446358680725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0865507125854492})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.518339991569519})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.395101398229599})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3463953137397766})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34281453490257263})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30456051230430603})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3314785957336426})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3060556650161743})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3208596706390381})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2916850830078125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1027703285217285})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.530055046081543})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.411344051361084})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3733159005641937})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28609490394592285})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3078262209892273})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.292620986700058})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28274470567703247})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [39238, 9962, 38381, 34800, 43458, 14619, 54950, 55902, 17786, 14801], 'labels': [-1, 2, 2, 5, -1, 3, 8, -1, -1, -1], 'scores': [0.4033339023590088, 0.45054569840431213, 0.5116042196750641, 0.4656608998775482, 0.4567021131515503, 0.69746333360672, 0.5829588174819946, 0.43812763690948486, 0.3832836151123047, 0.4377291202545166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1097257137298584})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.468265175819397})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3668874204158783})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33750051259994507})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.308521568775177})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31381845474243164})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29834455251693726})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32499730587005615})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2848985195159912})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32210227847099304})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3056771159172058})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31722480058670044})
store['active_learning_steps'][53]['training']['best_epoch']=9
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.24738349609375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8538389205932617})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.50447678565979})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35903677344322205})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3082137107849121})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2626979649066925})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30730772018432617})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.247043639421463})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.22857290506362915})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26882100105285645})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2574174404144287})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24284771084785461})
store['active_learning_steps'][53]['eval_training']['best_epoch']=8
store['active_learning_steps'][53]['acquisition']={'indices': [54592, 9050, 4039, 27458, 51850, 54718, 14305, 43815, 10137, 27542], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.3984144926071167, 0.24387431144714355, 0.4763883352279663, 0.4336380362510681, 0.38782799243927, 0.3336557149887085, 0.36378371715545654, 0.41476598381996155, 0.14446979761123657, 0.22635316848754883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0282528400421143})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4761608839035034})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37149274349212646})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3157634735107422})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29152604937553406})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2890709340572357})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30124813318252563})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2909592092037201})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3089786767959595})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.265254638671875}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8937122821807861})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47742366790771484})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35254815220832825})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3381801247596741})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3295102119445801})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3062663674354553})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2843279242515564})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2673143744468689})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [5600, 8267, 30726, 31155, 53693, 45461, 44875, 2202, 52205, 27296], 'labels': [6, -1, -1, -1, 4, -1, -1, 1, -1, -1], 'scores': [0.5576289892196655, 0.34955692291259766, 0.303308367729187, 0.3844391703605652, 0.4320879578590393, 0.34623968601226807, 0.21880507469177246, 0.4058070778846741, 0.4226353168487549, 0.268485426902771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0876703262329102})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5289849042892456})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35610949993133545})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3341286778450012})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3036128878593445})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3174911141395569})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.330671489238739})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2897997796535492})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3427586257457733})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34471994638442993})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3067312240600586})
store['active_learning_steps'][55]['training']['best_epoch']=8
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2669447021484375}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7244563102722168})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46698176860809326})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35941094160079956})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29145753383636475})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29798078536987305})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28337037563323975})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25288790464401245})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28450527787208557})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2530447244644165})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26628196239471436})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [49299, 11390, 23101, 26676, 12218, 2735, 54019, 56796, 54907, 3231], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5257291793823242, 0.5269842147827148, 0.564325213432312, 0.6138550043106079, 0.4448169469833374, 0.503652811050415, 0.5236281156539917, 0.5567938685417175, 0.3885749578475952, 0.2974724769592285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1129062175750732})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.594028115272522})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3881087899208069})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3699321150779724})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3342839181423187})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33744561672210693})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.324054479598999})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3082941174507141})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3212381601333618})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3216949701309204})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34761932492256165})
store['active_learning_steps'][56]['training']['best_epoch']=8
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.27429462890625}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7843073606491089})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48455971479415894})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3766443133354187})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3620207905769348})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2898310422897339})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2912844717502594})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28276318311691284})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2725129723548889})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2886878252029419})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27348583936691284})
store['active_learning_steps'][56]['eval_training']['best_epoch']=8
store['active_learning_steps'][56]['acquisition']={'indices': [50342, 52744, 57722, 32275, 48664, 32572, 34071, 48102, 551, 4043], 'labels': [8, -1, -1, -1, -1, -1, 6, 7, -1, -1], 'scores': [0.6275546550750732, 0.41046690940856934, 0.37741565704345703, 0.37808775901794434, 0.3410797119140625, 0.45451831817626953, 0.3848961591720581, 0.6115957498550415, 0.3858884572982788, 0.44200706481933594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1546517610549927})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.532318115234375})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3931272029876709})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3544572591781616})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3202189803123474})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.355567067861557})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30652034282684326})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3162762224674225})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3339923620223999})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3129723370075226})
store['active_learning_steps'][57]['training']['best_epoch']=7
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2820152587890625}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8526422381401062})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4775906205177307})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3931131064891815})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3000786602497101})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29364073276519775})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30154138803482056})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3020581007003784})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25044959783554077})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.252442330121994})
store['active_learning_steps'][57]['eval_training']['best_epoch']=8
store['active_learning_steps'][57]['acquisition']={'indices': [19778, 36653, 20080, 51231, 59383, 19658, 7949, 44384, 37160, 20578], 'labels': [9, 6, -1, -1, -1, -1, -1, -1, 5, 8], 'scores': [0.4685790538787842, 0.5040156841278076, 0.37598931789398193, 0.4575881361961365, 0.323511004447937, 0.3273611068725586, 0.48612749576568604, 0.3938225507736206, 0.4124850034713745, 0.5910669565200806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0333034992218018})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48128587007522583})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3662645220756531})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3071689307689667})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3264932334423065})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2949025630950928})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27579379081726074})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2851657271385193})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3334193825721741})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29993587732315063})
store['active_learning_steps'][58]['training']['best_epoch']=7
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.2525861328125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9167890548706055})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44634222984313965})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35803651809692383})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32685020565986633})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2913495600223541})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2678099572658539})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2880747318267822})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2640155851840973})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25796419382095337})
store['active_learning_steps'][58]['eval_training']['best_epoch']=9
store['active_learning_steps'][58]['acquisition']={'indices': [29515, 956, 6178, 12651, 58437, 45348, 26376, 45764, 19100, 13752], 'labels': [-1, -1, -1, 9, -1, 2, 1, -1, -1, 9], 'scores': [0.26189136505126953, 0.43488991260528564, 0.5239944458007812, 0.5777896642684937, 0.5404326915740967, 0.5125279426574707, 0.36300235986709595, 0.315186083316803, 0.2357109785079956, 0.5573177933692932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1145447492599487})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5980392694473267})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39584171772003174})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37114861607551575})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33010557293891907})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30540043115615845})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.288293719291687})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30789637565612793})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30437690019607544})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2853361666202545})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26750242710113525})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32544463872909546})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3199741840362549})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2961358428001404})
store['active_learning_steps'][59]['training']['best_epoch']=11
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.252956494140625}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.8718395829200745})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4560513496398926})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3619067072868347})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31098562479019165})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26494812965393066})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28798311948776245})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24951711297035217})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26180851459503174})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25441277027130127})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24623757600784302})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2706158757209778})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21966707706451416})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22269338369369507})
store['active_learning_steps'][59]['eval_training']['best_epoch']=12
store['active_learning_steps'][59]['acquisition']={'indices': [25322, 42386, 50907, 58411, 51917, 17382, 30115, 47440, 4457, 31646], 'labels': [-1, -1, -1, -1, -1, 6, -1, -1, -1, -1], 'scores': [0.5752576589584351, 0.594444990158081, 0.514385461807251, 0.41317594051361084, 0.4240380525588989, 0.4860873818397522, 0.6142470836639404, 0.5078157186508179, 0.5750942230224609, 0.617339015007019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 1.0189094543457031})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47629043459892273})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3845600485801697})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30628281831741333})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31822943687438965})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3030102849006653})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32267022132873535})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30739766359329224})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2895815968513489})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3424775004386902})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2990376055240631})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3207084834575653})
store['active_learning_steps'][60]['training']['best_epoch']=9
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2548674072265625}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9807083606719971})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5253756642341614})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35889142751693726})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3286265432834625})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32097142934799194})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31177884340286255})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2622697353363037})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24614956974983215})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27925407886505127})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26117607951164246})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24720941483974457})
store['active_learning_steps'][60]['eval_training']['best_epoch']=8
store['active_learning_steps'][60]['acquisition']={'indices': [21793, 2268, 4160, 9038, 18554, 9290, 6210, 15369, 21567, 26733], 'labels': [-1, -1, -1, -1, -1, 9, -1, -1, -1, 2], 'scores': [0.4588714838027954, 0.38644301891326904, 0.36975574493408203, 0.38208627700805664, 0.3342653512954712, 0.3520559072494507, 0.34422624111175537, 0.27758216857910156, 0.32635730504989624, 0.6222956776618958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9774308204650879})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48059219121932983})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40799838304519653})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31728315353393555})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33594149351119995})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32231491804122925})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31169384717941284})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32782113552093506})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30501118302345276})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30837610363960266})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30743470788002014})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33605265617370605})
store['active_learning_steps'][61]['training']['best_epoch']=9
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2644128662109375}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8714259266853333})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5095854997634888})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39006948471069336})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34419554471969604})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32043230533599854})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27995526790618896})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2686733901500702})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2527269124984741})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24734823405742645})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24668990075588226})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2582045793533325})
store['active_learning_steps'][61]['eval_training']['best_epoch']=10
store['active_learning_steps'][61]['acquisition']={'indices': [14405, 52834, 41601, 30658, 47234, 52151, 41185, 11767, 56703, 8434], 'labels': [6, 2, -1, 4, 1, 9, -1, 4, -1, -1], 'scores': [0.6200837194919586, 0.7637121677398682, 0.38556838035583496, 0.3538447320461273, 0.45732665061950684, 0.45708972215652466, 0.3317587375640869, 0.5942865014076233, 0.22809338569641113, 0.36183905601501465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.168761968612671})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5899783372879028})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4195981025695801})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32599353790283203})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.321108341217041})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28907525539398193})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29362547397613525})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32613474130630493})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28754371404647827})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30856460332870483})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3445529043674469})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3044840097427368})
store['active_learning_steps'][62]['training']['best_epoch']=9
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.254338330078125}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9459347724914551})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5461178421974182})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3709193170070648})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33830398321151733})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27790993452072144})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3135012090206146})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.284074604511261})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24471846222877502})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25313031673431396})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27366435527801514})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23629599809646606})
store['active_learning_steps'][62]['eval_training']['best_epoch']=11
store['active_learning_steps'][62]['acquisition']={'indices': [35382, 33029, 37838, 50091, 54212, 22675, 21387, 57929, 18757, 31161], 'labels': [7, -1, -1, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.3081209659576416, 0.475752055644989, 0.328727126121521, 0.6202282309532166, 0.4047963619232178, 0.3417477607727051, 0.4903854727745056, 0.32402241230010986, 0.5625569820404053, 0.4342995285987854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0621399879455566})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5587059259414673})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37105754017829895})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33164292573928833})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2876138389110565})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3125835657119751})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31797295808792114})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2798475921154022})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26779550313949585})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30455970764160156})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3000314235687256})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30479711294174194})
store['active_learning_steps'][63]['training']['best_epoch']=9
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.251488330078125}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8473799228668213})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4962334632873535})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3504461348056793})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29867708683013916})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28443825244903564})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28008171916007996})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2484390288591385})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23392362892627716})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24678222835063934})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2456447333097458})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2558217942714691})
store['active_learning_steps'][63]['eval_training']['best_epoch']=8
store['active_learning_steps'][63]['acquisition']={'indices': [8114, 49087, 11857, 18238, 22162, 38290, 51234, 17714, 14151, 8267], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, -1], 'scores': [0.4055819511413574, 0.3189157247543335, 0.500732421875, 0.38380563259124756, 0.5360379219055176, 0.3504161834716797, 0.4133695363998413, 0.41476690769195557, 0.510212779045105, 0.5891202688217163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.1342644691467285})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5467537641525269})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42229989171028137})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3439216613769531})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32212796807289124})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32240092754364014})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2925679087638855})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3148117661476135})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30115604400634766})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2973504066467285})
store['active_learning_steps'][64]['training']['best_epoch']=7
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2744677734375}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8958255052566528})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4478956460952759})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37517648935317993})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33681702613830566})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32746201753616333})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2997889220714569})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2790946364402771})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26749229431152344})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28246009349823})
store['active_learning_steps'][64]['eval_training']['best_epoch']=8
store['active_learning_steps'][64]['acquisition']={'indices': [4379, 55323, 54629, 58309, 12318, 47597, 20287, 18486, 39457, 36195], 'labels': [-1, -1, -1, -1, 1, 8, 4, -1, 0, -1], 'scores': [0.6204042434692383, 0.45301687717437744, 0.35642242431640625, 0.5337026715278625, 0.31801852583885193, 0.6346107721328735, 0.4231739044189453, 0.5278159379959106, 0.6131250858306885, 0.27545690536499023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.017091989517212})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4874624013900757})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34542566537857056})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32184484601020813})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2679293751716614})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2699875831604004})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2561018466949463})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2901074290275574})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2849150002002716})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2820613980293274})
store['active_learning_steps'][65]['training']['best_epoch']=7
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9745, 'crossentropy': 0.2559261474609375}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 1.0191209316253662})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5234200954437256})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4622904360294342})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31848931312561035})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32393282651901245})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31429237127304077})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27970507740974426})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2633667588233948})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28541678190231323})
store['active_learning_steps'][65]['eval_training']['best_epoch']=8
store['active_learning_steps'][65]['acquisition']={'indices': [33973, 394, 23411, 38733, 17478, 24656, 34080, 31329, 58628, 34865], 'labels': [-1, -1, 4, -1, 4, -1, -1, -1, -1, -1], 'scores': [0.32183241844177246, 0.2785353660583496, 0.4715960621833801, 0.5186530947685242, 0.5436156988143921, 0.4882155656814575, 0.4237159490585327, 0.4686460494995117, 0.4625917077064514, 0.3735833168029785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1926517486572266})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5582067966461182})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4309040606021881})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34522417187690735})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33382928371429443})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3055492043495178})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27719646692276})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2798526883125305})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32807618379592896})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28962960839271545})
store['active_learning_steps'][66]['training']['best_epoch']=7
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2540846923828125}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9350226521492004})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.46561023592948914})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35979700088500977})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3447585105895996})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26902031898498535})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2555086016654968})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28240543603897095})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2519087791442871})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2750697731971741})
store['active_learning_steps'][66]['eval_training']['best_epoch']=8
store['active_learning_steps'][66]['acquisition']={'indices': [47867, 55245, 27564, 6329, 57159, 7429, 31861, 45422, 19428, 32172], 'labels': [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1], 'scores': [0.35627281665802, 0.48968374729156494, 0.3667459487915039, 0.5565587878227234, 0.464432954788208, 0.6149858236312866, 0.6125897169113159, 0.4653061032295227, 0.42737877368927, 0.3163912296295166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.1761265993118286})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5981892347335815})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3282927870750427})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32097941637039185})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30017179250717163})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.322313129901886})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2808866798877716})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2853727638721466})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28708577156066895})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2893596291542053})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.2456309814453125}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.898745596408844})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.426159143447876})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35542529821395874})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3285266160964966})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2591839134693146})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2967451810836792})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24963736534118652})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28114455938339233})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25384676456451416})
store['active_learning_steps'][67]['eval_training']['best_epoch']=7
store['active_learning_steps'][67]['acquisition']={'indices': [17862, 42847, 43209, 48637, 14973, 20257, 48149, 48781, 59776, 22064], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4847567081451416, 0.3712731599807739, 0.5484672784805298, 0.49293386936187744, 0.35170412063598633, 0.5118529796600342, 0.31858938932418823, 0.4573867917060852, 0.40776526927948, 0.3289763927459717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2358031272888184})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5996538400650024})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3963192403316498})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35364705324172974})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2857474088668823})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2798537611961365})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2765653729438782})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2784324884414673})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27347469329833984})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27869391441345215})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3170790672302246})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28448277711868286})
store['active_learning_steps'][68]['training']['best_epoch']=9
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2499895263671875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8718084096908569})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4923909604549408})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37458574771881104})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30803364515304565})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2843489944934845})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2991599142551422})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26773783564567566})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25309038162231445})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26269611716270447})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2385692298412323})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26563742756843567})
store['active_learning_steps'][68]['eval_training']['best_epoch']=10
store['active_learning_steps'][68]['acquisition']={'indices': [30075, 42817, 51896, 5905, 23514, 27200, 27162, 49956, 42681, 3282], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5036380290985107, 0.3794121742248535, 0.444000244140625, 0.4080909490585327, 0.3236100673675537, 0.5768855214118958, 0.2868220806121826, 0.19086503982543945, 0.38921165466308594, 0.5617186427116394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.21934175491333})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5491667985916138})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37439149618148804})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2972620725631714})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29831042885780334})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2667131721973419})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2807481288909912})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29207780957221985})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2958090007305145})
store['active_learning_steps'][69]['training']['best_epoch']=6
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2631557373046875}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8435325622558594})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5092476606369019})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36836451292037964})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33278733491897583})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3338415324687958})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31194737553596497})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30015069246292114})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31174445152282715})
store['active_learning_steps'][69]['eval_training']['best_epoch']=7
store['active_learning_steps'][69]['acquisition']={'indices': [4379, 57523, 16574, 53398, 47170, 57028, 10441, 9079, 16110, 4457], 'labels': [-1, 3, -1, 6, -1, -1, -1, -1, -1, -1], 'scores': [0.605840802192688, 0.490165114402771, 0.6240570545196533, 0.38175737857818604, 0.6079245805740356, 0.4934709072113037, 0.5163110494613647, 0.3221867084503174, 0.6153563261032104, 0.526678204536438]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1290881633758545})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.45412203669548035})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.37345090508461})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30224499106407166})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2736261785030365})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2720147371292114})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23722991347312927})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27807337045669556})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2858598232269287})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27755022048950195})
store['active_learning_steps'][70]['training']['best_epoch']=7
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9752, 'crossentropy': 0.223757080078125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8725391626358032})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4504650831222534})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3387368321418762})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29551923274993896})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2715452313423157})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26209643483161926})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2787685990333557})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23952408134937286})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2360556423664093})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [59133, 31821, 45339, 7252, 3319, 55297, 22226, 57851, 25420, 31795], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3280826807022095, 0.4720918536186218, 0.5742464065551758, 0.45904505252838135, 0.3471332788467407, 0.37627077102661133, 0.33087921142578125, 0.3938688039779663, 0.5851571559906006, 0.2912214994430542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1179790496826172})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5851937532424927})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41587918996810913})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35366934537887573})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31951743364334106})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3176228404045105})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.303525447845459})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3096824586391449})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28977566957473755})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3106219172477722})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2905694246292114})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3086642026901245})
store['active_learning_steps'][71]['training']['best_epoch']=9
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2649939697265625}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9210591912269592})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5153899788856506})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3681703209877014})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36446115374565125})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2861587703227997})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2679213285446167})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2566852867603302})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24974875152111053})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2380332499742508})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2489863634109497})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22972050309181213})
store['active_learning_steps'][71]['eval_training']['best_epoch']=11
store['active_learning_steps'][71]['acquisition']={'indices': [24645, 42807, 52054, 59344, 20686, 33222, 47674, 36809, 24249, 6633], 'labels': [-1, -1, -1, 9, -1, 5, -1, -1, -1, -1], 'scores': [0.3020057678222656, 0.5057297945022583, 0.29226285219192505, 0.4798763394355774, 0.4459182024002075, 0.6895629465579987, 0.5154658555984497, 0.42851436138153076, 0.3891618251800537, 0.4454331398010254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0828676223754883})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.483387291431427})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36770468950271606})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32574260234832764})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3027387857437134})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26985305547714233})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28662025928497314})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23919536173343658})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29356849193573})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26656538248062134})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31611913442611694})
store['active_learning_steps'][72]['training']['best_epoch']=8
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.976, 'crossentropy': 0.2315681640625}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9432189464569092})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4823645353317261})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3237266540527344})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3018207848072052})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23702818155288696})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25930410623550415})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23782551288604736})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23334752023220062})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23221148550510406})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2436690777540207})
store['active_learning_steps'][72]['eval_training']['best_epoch']=9
store['active_learning_steps'][72]['acquisition']={'indices': [57579, 53169, 57841, 59662, 31103, 4055, 32276, 25654, 32374, 25499], 'labels': [-1, -1, -1, -1, 8, -1, 3, -1, -1, -1], 'scores': [0.43818557262420654, 0.538286566734314, 0.34875428676605225, 0.43714582920074463, 0.5566722750663757, 0.5710853338241577, 0.5547723174095154, 0.600212812423706, 0.5053939819335938, 0.5038691759109497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 1.09696626663208})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49761128425598145})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.38314294815063477})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30605000257492065})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28760144114494324})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2874063551425934})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2528154253959656})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27042338252067566})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.279645174741745})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2711409330368042})
store['active_learning_steps'][73]['training']['best_epoch']=7
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.2436655029296875}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0042755603790283})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.550511360168457})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4095957577228546})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3516954779624939})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3135366439819336})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30493372678756714})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28592342138290405})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2882830500602722})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2893971800804138})
store['active_learning_steps'][73]['eval_training']['best_epoch']=7
store['active_learning_steps'][73]['acquisition']={'indices': [41474, 5637, 51500, 23988, 36042, 53440, 25138, 24484, 38037, 23008], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 8], 'scores': [0.27062737941741943, 0.3687819242477417, 0.4692455530166626, 0.41690880060195923, 0.31395792961120605, 0.37138044834136963, 0.5663636922836304, 0.5180634260177612, 0.46102774143218994, 0.42102694511413574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.424096941947937})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6453158855438232})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4491337239742279})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3098948001861572})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3210713863372803})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2938685417175293})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2792706787586212})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27236154675483704})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31715676188468933})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2789652943611145})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29530084133148193})
store['active_learning_steps'][74]['training']['best_epoch']=8
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9733, 'crossentropy': 0.251941357421875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8917042016983032})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5338493585586548})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3858600854873657})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.316089928150177})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2837330102920532})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32238829135894775})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2697504460811615})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2661842703819275})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2821311354637146})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2757270336151123})
store['active_learning_steps'][74]['eval_training']['best_epoch']=8
store['active_learning_steps'][74]['acquisition']={'indices': [59211, 39967, 46766, 12420, 42005, 10532, 54087, 53263, 38164, 10591], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4849089980125427, 0.6535810232162476, 0.6208251714706421, 0.47224128246307373, 0.6471827626228333, 0.6019196510314941, 0.6694353818893433, 0.5200446844100952, 0.48189985752105713, 0.7143720984458923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1966350078582764})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5676630735397339})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.40632301568984985})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3046351671218872})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2954264283180237})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2756011486053467})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25995901226997375})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3060768246650696})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2744387984275818})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29711854457855225})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2535726318359375}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9111710786819458})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5184284448623657})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34727901220321655})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3562643527984619})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.302325963973999})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28204917907714844})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2729496657848358})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26882249116897583})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2753939628601074})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [11759, 56203, 4369, 8819, 34866, 57495, 10854, 19998, 37934, 23760], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 9, -1], 'scores': [0.2874739170074463, 0.5585610270500183, 0.6339267492294312, 0.37091028690338135, 0.36042559146881104, 0.4323444366455078, 0.49080318212509155, 0.588411808013916, 0.494312047958374, 0.29487383365631104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.196892261505127})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.6079196333885193})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.41781485080718994})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3682563900947571})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29877138137817383})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3109619915485382})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29837316274642944})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3220941126346588})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32659244537353516})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3308107256889343})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9749, 'crossentropy': 0.2567190673828125}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.793790340423584})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4710119962692261})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35929232835769653})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3300549387931824})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2836708426475525})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2688428461551666})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.300070583820343})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2746817469596863})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24567605555057526})
store['active_learning_steps'][76]['eval_training']['best_epoch']=9
store['active_learning_steps'][76]['acquisition']={'indices': [30745, 13945, 41999, 53489, 2659, 20471, 43163, 39827, 33636, 7840], 'labels': [-1, -1, 0, -1, -1, -1, -1, -1, -1, 5], 'scores': [0.45528215169906616, 0.4386667013168335, 0.5904001593589783, 0.31227433681488037, 0.39461827278137207, 0.4185807704925537, 0.44477128982543945, 0.3178708553314209, 0.36578822135925293, 0.45557886362075806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1207680702209473})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.569602370262146})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37839949131011963})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34692203998565674})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3383452892303467})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3376652002334595})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30614525079727173})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3050501346588135})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.330863893032074})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3231995105743408})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31011199951171875})
store['active_learning_steps'][77]['training']['best_epoch']=8
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2651704833984375}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8670763373374939})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4929347038269043})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3554697036743164})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3329886198043823})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29296985268592834})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31687310338020325})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.291879266500473})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25640547275543213})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25136297941207886})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25624215602874756})
store['active_learning_steps'][77]['eval_training']['best_epoch']=9
store['active_learning_steps'][77]['acquisition']={'indices': [9628, 48973, 33505, 50373, 27624, 33801, 40534, 8772, 23216, 32773], 'labels': [-1, 8, 2, -1, 6, -1, -1, 1, -1, -1], 'scores': [0.37504470348358154, 0.43063366413116455, 0.5140289068222046, 0.3097192049026489, 0.4594523012638092, 0.5509892702102661, 0.2599707841873169, 0.4280726909637451, 0.33936798572540283, 0.2752048969268799]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1122188568115234})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5145226716995239})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39664915204048157})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3324151337146759})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2949942350387573})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30876320600509644})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3408774733543396})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29865115880966187})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.2757634521484375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8351848125457764})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4849548935890198})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4284856915473938})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3142768144607544})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3515252470970154})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3288757801055908})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3112134635448456})
store['active_learning_steps'][78]['eval_training']['best_epoch']=7
store['active_learning_steps'][78]['acquisition']={'indices': [11056, 2908, 14693, 37630, 50499, 48587, 18130, 3825, 24776, 14040], 'labels': [-1, -1, -1, -1, -1, 3, 8, -1, -1, -1], 'scores': [0.38846325874328613, 0.4637743830680847, 0.43044590950012207, 0.4628399610519409, 0.5331337451934814, 0.5178698897361755, 0.5855840444564819, 0.4420914649963379, 0.5081835389137268, 0.25942349433898926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1469933986663818})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5287699103355408})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3425823748111725})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3081531226634979})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28063932061195374})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25279584527015686})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2757248282432556})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2881361246109009})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2573860287666321})
store['active_learning_steps'][79]['training']['best_epoch']=6
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9738, 'crossentropy': 0.2492367431640625}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0395805835723877})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6345703601837158})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3972327411174774})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35925665497779846})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3262287378311157})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29866093397140503})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29584869742393494})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28303879499435425})
store['active_learning_steps'][79]['eval_training']['best_epoch']=8
store['active_learning_steps'][79]['acquisition']={'indices': [20703, 10591, 28216, 38252, 52581, 46368, 5195, 27179, 46366, 33930], 'labels': [-1, -1, -1, 5, -1, 8, 4, 5, -1, -1], 'scores': [0.31179189682006836, 0.3333011865615845, 0.4020124673843384, 0.4111635088920593, 0.4567009210586548, 0.40254443883895874, 0.38567477464675903, 0.28171175718307495, 0.384326696395874, 0.3648955821990967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.283083200454712})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.587570071220398})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3852889835834503})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33993518352508545})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29018986225128174})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3379128873348236})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2978290915489197})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2943603992462158})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.276437744140625}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8795639872550964})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5025462508201599})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.44367727637290955})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3561049699783325})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32995671033859253})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3130412697792053})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3045806288719177})
store['active_learning_steps'][80]['eval_training']['best_epoch']=7
store['active_learning_steps'][80]['acquisition']={'indices': [18398, 8267, 11374, 31646, 34771, 42793, 56195, 7720, 51351, 41424], 'labels': [4, -1, -1, -1, 0, 4, -1, -1, -1, 1], 'scores': [0.43848419189453125, 0.33678770065307617, 0.45006537437438965, 0.4475672245025635, 0.36789876222610474, 0.2167833149433136, 0.30432188510894775, 0.40777385234832764, 0.5888451337814331, 0.4166024923324585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0807201862335205})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5194486379623413})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3948419690132141})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36280691623687744})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31531429290771484})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3023229241371155})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3030150532722473})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3085956573486328})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3098394274711609})
store['active_learning_steps'][81]['training']['best_epoch']=6
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2820103271484375}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0057560205459595})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4929336905479431})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4175536632537842})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.4191974997520447})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3559180796146393})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33824700117111206})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3224887251853943})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3032741844654083})
store['active_learning_steps'][81]['eval_training']['best_epoch']=8
store['active_learning_steps'][81]['acquisition']={'indices': [41385, 47292, 28262, 2148, 9576, 20746, 57663, 29099, 24038, 13126], 'labels': [3, 9, 9, 6, -1, 1, 7, -1, 1, -1], 'scores': [0.274630069732666, 0.45272815227508545, 0.3663157820701599, 0.48546159267425537, 0.35371291637420654, 0.3602633476257324, 0.3487071990966797, 0.3638871908187866, 0.5435945391654968, 0.4285632371902466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.005753517150879})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5338870286941528})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3639085292816162})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2930493950843811})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2873818278312683})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25775855779647827})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2873741686344147})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2667883634567261})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2501949369907379})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3101612329483032})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.268054723739624})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.270987331867218})
store['active_learning_steps'][82]['training']['best_epoch']=9
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9748, 'crossentropy': 0.235229931640625}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8898433446884155})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.48943838477134705})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36035382747650146})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2847261130809784})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24819067120552063})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26021140813827515})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2467791736125946})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23381584882736206})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22879192233085632})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2148435413837433})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2608242630958557})
store['active_learning_steps'][82]['eval_training']['best_epoch']=10
store['active_learning_steps'][82]['acquisition']={'indices': [53979, 27753, 31509, 18672, 40088, 7793, 44753, 30851, 20110, 57701], 'labels': [8, -1, -1, -1, -1, 8, 5, -1, 4, -1], 'scores': [0.693381667137146, 0.36912965774536133, 0.3693767786026001, 0.4067319631576538, 0.45620226860046387, 0.6011008024215698, 0.6286378502845764, 0.6120864152908325, 0.474393755197525, 0.2988419532775879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2032008171081543})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.6138992309570312})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36777448654174805})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3346512019634247})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27787625789642334})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2815127372741699})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27461981773376465})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29464030265808105})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28493732213974})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2849029004573822})
store['active_learning_steps'][83]['training']['best_epoch']=7
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.250576708984375}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9824604988098145})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49301424622535706})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37111371755599976})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3233186602592468})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31497910618782043})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2909843325614929})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2866988778114319})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28571754693984985})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28499025106430054})
store['active_learning_steps'][83]['eval_training']['best_epoch']=9
store['active_learning_steps'][83]['acquisition']={'indices': [23843, 10409, 16872, 5443, 23027, 35012, 28172, 45373, 30477, 28434], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.43931710720062256, 0.3532679080963135, 0.48384857177734375, 0.5596197843551636, 0.5204373002052307, 0.45320582389831543, 0.27217280864715576, 0.4223228693008423, 0.5000412464141846, 0.3993033170700073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1629464626312256})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5171616077423096})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3947485685348511})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30957669019699097})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.267658531665802})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27223843336105347})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28751569986343384})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2618589401245117})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30203405022621155})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27265089750289917})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2828478217124939})
store['active_learning_steps'][84]['training']['best_epoch']=8
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.2406861328125}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.027282953262329})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5033207535743713})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33547261357307434})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30645427107810974})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28760600090026855})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2757466435432434})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28186696767807007})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2669542729854584})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24103453755378723})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27252858877182007})
store['active_learning_steps'][84]['eval_training']['best_epoch']=9
store['active_learning_steps'][84]['acquisition']={'indices': [5557, 16162, 18826, 2089, 6273, 31520, 50153, 36896, 53328, 29322], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.40585649013519287, 0.5744764804840088, 0.46602946519851685, 0.3369353413581848, 0.48859429359436035, 0.4325813055038452, 0.4196743965148926, 0.3272089958190918, 0.4721350073814392, 0.3581007719039917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.2056496143341064})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.535059928894043})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3782777786254883})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34509819746017456})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26053470373153687})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.312421977519989})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2707168757915497})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28754541277885437})
store['active_learning_steps'][85]['training']['best_epoch']=5
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.26288955078125}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 1.0552808046340942})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5752830505371094})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4489032030105591})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3881211578845978})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3448023200035095})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3455989360809326})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32491591572761536})
store['active_learning_steps'][85]['eval_training']['best_epoch']=7
store['active_learning_steps'][85]['acquisition']={'indices': [17265, 31343, 32374, 21636, 34938, 8451, 9227, 55106, 46096, 37725], 'labels': [2, -1, -1, 2, -1, 1, -1, -1, -1, 1], 'scores': [0.4017442464828491, 0.3770085573196411, 0.26097571849823, 0.5202916860580444, 0.3173975944519043, 0.3139455318450928, 0.5295335054397583, 0.27470874786376953, 0.28353744745254517, 0.3173176646232605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9979144334793091})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5106409192085266})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38790786266326904})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32691699266433716})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26345008611679077})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.287563681602478})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27045369148254395})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26564592123031616})
store['active_learning_steps'][86]['training']['best_epoch']=5
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.2623746337890625}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9506513476371765})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.601495623588562})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4189826548099518})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32913944125175476})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3251359760761261})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3702293038368225})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2772423028945923})
store['active_learning_steps'][86]['eval_training']['best_epoch']=7
store['active_learning_steps'][86]['acquisition']={'indices': [5129, 12461, 41330, 41772, 27242, 25307, 8243, 41894, 16947, 20952], 'labels': [2, -1, 2, 5, -1, 1, -1, 1, 4, -1], 'scores': [0.44657015800476074, 0.3522433042526245, 0.414652556180954, 0.48774999380111694, 0.38235175609588623, 0.21464025974273682, 0.3318225145339966, 0.33140838146209717, 0.4543169140815735, 0.2818509340286255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 1.01771879196167})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48319172859191895})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32114726305007935})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2662380337715149})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25594159960746765})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26726704835891724})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26037439703941345})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25618991255760193})
store['active_learning_steps'][87]['training']['best_epoch']=5
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.973, 'crossentropy': 0.2434516357421875}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8773837089538574})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.530476450920105})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3844437599182129})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36977171897888184})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30898308753967285})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3138294816017151})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28957802057266235})
store['active_learning_steps'][87]['eval_training']['best_epoch']=7
store['active_learning_steps'][87]['acquisition']={'indices': [17741, 24767, 14616, 34315, 6618, 54237, 43702, 56457, 28562, 15012], 'labels': [0, 4, -1, -1, -1, -1, 3, 3, -1, -1], 'scores': [0.35728514194488525, 0.3653097152709961, 0.38004928827285767, 0.2271512746810913, 0.2873128056526184, 0.3417699337005615, 0.48100852966308594, 0.43359142541885376, 0.20127761363983154, 0.2647104859352112]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.3048372268676758})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5639991760253906})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37867650389671326})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31043165922164917})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26321178674697876})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27980688214302063})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2940264344215393})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2499818354845047})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2799708843231201})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24873259663581848})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2758084833621979})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2781613767147064})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2629910111427307})
store['active_learning_steps'][88]['training']['best_epoch']=10
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.241014599609375}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0211460590362549})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5573622584342957})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3563135266304016})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3087773323059082})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3099886178970337})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23901638388633728})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25531384348869324})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26696574687957764})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24932825565338135})
store['active_learning_steps'][88]['eval_training']['best_epoch']=6
store['active_learning_steps'][88]['acquisition']={'indices': [42531, 22970, 49541, 33481, 45942, 11622, 45364, 46624, 56329, 52889], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.41937780380249023, 0.5747016668319702, 0.40743041038513184, 0.37577617168426514, 0.4750131368637085, 0.3855891227722168, 0.43886876106262207, 0.39923202991485596, 0.3161407709121704, 0.5170759558677673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0488853454589844})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.528740406036377})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3982059061527252})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3665271997451782})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29885774850845337})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28881165385246277})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2878981828689575})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28846174478530884})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28275734186172485})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28338849544525146})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3109667897224426})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3192784786224365})
store['active_learning_steps'][89]['training']['best_epoch']=9
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.23355849609375}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9334075450897217})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4885907769203186})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3768928050994873})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3155970275402069})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2915031611919403})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2442161738872528})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.249669149518013})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2564312219619751})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2347164750099182})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2576405107975006})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24121223390102386})
store['active_learning_steps'][89]['eval_training']['best_epoch']=9
store['active_learning_steps'][89]['acquisition']={'indices': [34906, 19362, 46013, 34122, 4904, 32776, 24061, 50595, 40372, 56414], 'labels': [3, 8, 6, 5, 7, 4, -1, -1, -1, 9], 'scores': [0.5606032907962799, 0.5225229859352112, 0.3343765139579773, 0.5218148231506348, 0.44134676456451416, 0.6289594173431396, 0.5585677623748779, 0.361106276512146, 0.5302108526229858, 0.46901631355285645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1546533107757568})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6110734939575195})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4146987199783325})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3250505328178406})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29549115896224976})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2951355278491974})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29084473848342896})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.293375700712204})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28655606508255005})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29794174432754517})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.323400616645813})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2829367220401764})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2844449281692505})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30402547121047974})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3017677366733551})
store['active_learning_steps'][90]['training']['best_epoch']=12
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9764, 'crossentropy': 0.2458253662109375}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9324779510498047})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5205458402633667})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32471394538879395})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30674442648887634})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2801300287246704})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25902438163757324})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2708161473274231})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24574729800224304})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24513563513755798})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2512337565422058})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23806224763393402})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24243909120559692})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2549286484718323})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2257116734981537})
store['active_learning_steps'][90]['eval_training']['best_epoch']=14
store['active_learning_steps'][90]['acquisition']={'indices': [16690, 14645, 22145, 84, 52717, 4564, 37441, 56978, 17978, 55179], 'labels': [-1, -1, -1, -1, -1, -1, 1, 8, -1, -1], 'scores': [0.5977243185043335, 0.4384589195251465, 0.3954726457595825, 0.4267048239707947, 0.41350626945495605, 0.6174862384796143, 0.6409981846809387, 0.4089754819869995, 0.39917880296707153, 0.30476856231689453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2035300731658936})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.560553252696991})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3647806644439697})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32918089628219604})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3147600293159485})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26358848810195923})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2936158776283264})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2828751802444458})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2827739715576172})
store['active_learning_steps'][91]['training']['best_epoch']=6
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.23809208984375}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9905999302864075})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5245910882949829})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4104282259941101})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35373249650001526})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3075001537799835})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3303750157356262})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27947530150413513})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26067814230918884})
store['active_learning_steps'][91]['eval_training']['best_epoch']=8
store['active_learning_steps'][91]['acquisition']={'indices': [31687, 37322, 25774, 50548, 38932, 9628, 48448, 11330, 32583, 35643], 'labels': [-1, -1, -1, -1, 5, -1, 4, -1, -1, 3], 'scores': [0.2360990047454834, 0.33700406551361084, 0.29712945222854614, 0.23320996761322021, 0.5044719576835632, 0.31455278396606445, 0.2802606225013733, 0.28144359588623047, 0.43764686584472656, 0.40154850482940674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.105781078338623})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5212520360946655})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3514043688774109})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29192012548446655})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2742433249950409})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2742927074432373})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31044191122055054})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27004045248031616})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2643808126449585})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2648012638092041})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27029815316200256})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24245473742485046})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2951377034187317})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.267661452293396})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2745761275291443})
store['active_learning_steps'][92]['training']['best_epoch']=12
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9754, 'crossentropy': 0.2227994873046875}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9021269083023071})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45752307772636414})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3509494960308075})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2919148802757263})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2847515344619751})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27681076526641846})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24623242020606995})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23025798797607422})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2296013981103897})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2041553258895874})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22047829627990723})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22722896933555603})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.20576950907707214})
store['active_learning_steps'][92]['eval_training']['best_epoch']=10
store['active_learning_steps'][92]['acquisition']={'indices': [25016, 22830, 17392, 11992, 30425, 20072, 29273, 43025, 38875, 11482], 'labels': [-1, 6, 0, 9, -1, -1, -1, -1, -1, 8], 'scores': [0.4075136184692383, 0.42311346530914307, 0.6224349737167358, 0.38154006004333496, 0.5213104486465454, 0.35146939754486084, 0.3971993923187256, 0.28585028648376465, 0.43973004817962646, 0.7351190447807312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2927521467208862})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.590674102306366})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.43191373348236084})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34806686639785767})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.282204806804657})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25930601358413696})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29426562786102295})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.265832781791687})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2895978093147278})
store['active_learning_steps'][93]['training']['best_epoch']=6
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.238755078125}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8801389932632446})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4665359556674957})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4111352264881134})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30917057394981384})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3175976276397705})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32214534282684326})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2716270089149475})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.290412962436676})
store['active_learning_steps'][93]['eval_training']['best_epoch']=7
store['active_learning_steps'][93]['acquisition']={'indices': [11539, 17825, 6178, 4650, 22320, 31047, 35971, 18657, 10744, 49517], 'labels': [-1, -1, -1, -1, 8, -1, 0, -1, 7, 6], 'scores': [0.33508098125457764, 0.38355040550231934, 0.34557676315307617, 0.30850470066070557, 0.32254093885421753, 0.39672374725341797, 0.595479428768158, 0.3199242353439331, 0.3285753130912781, 0.539901614189148]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1143510341644287})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.518363356590271})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35760772228240967})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3405182659626007})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28527140617370605})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26832807064056396})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2645804286003113})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2437869757413864})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2719956636428833})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26294177770614624})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25261813402175903})
store['active_learning_steps'][94]['training']['best_epoch']=8
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9765, 'crossentropy': 0.2286337158203125}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9759999513626099})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5174221992492676})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34840211272239685})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3584063649177551})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3165830373764038})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2659887969493866})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2832113802433014})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2649606466293335})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.28708207607269287})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2424027919769287})
store['active_learning_steps'][94]['eval_training']['best_epoch']=10
store['active_learning_steps'][94]['acquisition']={'indices': [48340, 5752, 55134, 9057, 52140, 26134, 24555, 29511, 43474, 2429], 'labels': [-1, 5, -1, -1, 4, -1, -1, -1, 3, -1], 'scores': [0.49434995651245117, 0.3773488998413086, 0.31593549251556396, 0.4783053994178772, 0.515249490737915, 0.24837350845336914, 0.4722033739089966, 0.5372914671897888, 0.4990187883377075, 0.3752247095108032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2148492336273193})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5046029090881348})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33138585090637207})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2690105438232422})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25424033403396606})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2695278525352478})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.257975697517395})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2660352885723114})
store['active_learning_steps'][95]['training']['best_epoch']=5
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.2466064697265625}
