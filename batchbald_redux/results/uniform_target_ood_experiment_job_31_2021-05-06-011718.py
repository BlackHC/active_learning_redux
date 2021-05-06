store = {}
store['timestamp']=1620260238
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=31']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=31
store['worker_id']=31
store['num_workers']=40
store['config']={'seed': 42, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.2003986835479736})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.368544340133667})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.673008441925049})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8074793815612793})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6973, 'crossentropy': 2.01779765625}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 7766], ['id', 29126], ['id', 2909], ['id', 18648], ['id', 51518]], 'labels': [4, 8, 7, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.779317021369934})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.9398478269577026})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.1055972576141357})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.18727445602417})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7031, 'crossentropy': 1.586630859375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 41546], ['ood', 17144], ['ood', 41306], ['id', 23431], ['id', 26941]], 'labels': [5, 2, 1, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6982988119125366})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8791844844818115})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.067756175994873})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.1733555793762207})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6701, 'crossentropy': 1.6131810546875}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 29431], ['ood', 59009], ['ood', 1714], ['id', 12297], ['ood', 10265]], 'labels': [1, 5, 3, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6884856224060059})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.0266823768615723})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.136751651763916})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1670336723327637})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6738, 'crossentropy': 1.57139951171875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 6689], ['ood', 8960], ['ood', 50402], ['id', 59422], ['id', 17898]], 'labels': [4, 8, 2, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.5503146648406982})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.8263239860534668})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.099946975708008})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.0704245567321777})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6842, 'crossentropy': 1.37204619140625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 14310], ['id', 53690], ['id', 132], ['ood', 23335], ['ood', 40057]], 'labels': [1, 5, 5, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.6119763851165771})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.6403496265411377})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.9601491689682007})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.9932894706726074})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6746, 'crossentropy': 1.373022265625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 34942], ['ood', 43554], ['ood', 18430], ['id', 6700], ['id', 56940]], 'labels': [9, 4, 9, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5083234310150146})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7772172689437866})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.927060842514038})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9234979152679443})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6782, 'crossentropy': 1.3216419921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 11733], ['id', 22679], ['id', 46213], ['id', 8702], ['id', 59674]], 'labels': [7, 5, 1, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.334586501121521})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.518341302871704})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8094282150268555})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8368735313415527})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7109, 'crossentropy': 1.23536552734375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 19594], ['ood', 18055], ['ood', 47593], ['ood', 26658], ['id', 53829]], 'labels': [0, 0, 3, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2769906520843506})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.3479626178741455})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.5195083618164062})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3976621627807617})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7295, 'crossentropy': 1.14201318359375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 38964], ['ood', 27207], ['id', 42927], ['id', 50369], ['id', 42457]], 'labels': [7, 7, 1, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3082777261734009})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4435620307922363})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.494192361831665})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.7989952564239502})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7264, 'crossentropy': 1.1532634765625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 46645], ['id', 15560], ['ood', 24206], ['id', 13068], ['ood', 26477]], 'labels': [9, 9, 2, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3667354583740234})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4781718254089355})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5602465867996216})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7624146938323975})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7112, 'crossentropy': 1.212191796875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 28655], ['ood', 44329], ['id', 47742], ['ood', 33291], ['id', 56045]], 'labels': [4, 5, 3, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.1951239109039307})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.3110535144805908})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.3154628276824951})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3874192237854004})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7692, 'crossentropy': 1.0110919921875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 26931], ['id', 36457], ['ood', 55634], ['id', 56655], ['id', 57388]], 'labels': [6, 1, 0, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0258369445800781})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0788013935089111})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1615345478057861})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1648465394973755})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7831, 'crossentropy': 0.94999814453125}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 33206], ['id', 46473], ['ood', 35422], ['id', 37028], ['id', 36704]], 'labels': [9, 7, 7, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0041351318359375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0008256435394287})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.049039602279663})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0178990364074707})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0906833410263062})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8196, 'crossentropy': 0.89434873046875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 18846], ['id', 36477], ['id', 55297], ['ood', 25846], ['id', 5792]], 'labels': [4, 9, 0, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9507109522819519})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.019270896911621})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0584735870361328})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.079137921333313})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8023, 'crossentropy': 0.92132470703125}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 36629], ['ood', 35609], ['id', 4109], ['ood', 5573], ['ood', 44123]], 'labels': [8, 7, 1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9798336029052734})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9233400225639343})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.945659339427948})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0899732112884521})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0660252571105957})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8181, 'crossentropy': 0.85912353515625}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 7261], ['ood', 13026], ['id', 12188], ['id', 23849], ['id', 26242]], 'labels': [0, 6, 7, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0253671407699585})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0597500801086426})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9886689186096191})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0627110004425049})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2142362594604492})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1524205207824707})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8149, 'crossentropy': 0.94297099609375}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 5105], ['ood', 25313], ['id', 17520], ['ood', 13478], ['id', 6988]], 'labels': [3, 3, 2, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.883861780166626})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0068225860595703})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9842658638954163})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0591877698898315})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8073, 'crossentropy': 0.8689375}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 59446], ['ood', 45114], ['ood', 29057], ['ood', 54491], ['ood', 28395]], 'labels': [5, 3, 3, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0470364093780518})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0840215682983398})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1080026626586914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1019413471221924})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7604, 'crossentropy': 1.00493896484375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 32561], ['ood', 12326], ['id', 27785], ['id', 40377], ['ood', 6894]], 'labels': [1, 9, 1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9444657564163208})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9884012937545776})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0070455074310303})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0860183238983154})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8001, 'crossentropy': 0.883854296875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 13658], ['ood', 23391], ['id', 16111], ['id', 50808], ['ood', 13534]], 'labels': [3, 3, 3, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9821069836616516})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8850611448287964})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9914621114730835})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1191531419754028})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0518542528152466})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8223, 'crossentropy': 0.86199453125}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 51711], ['id', 12206], ['ood', 33543], ['id', 1345], ['id', 38105]], 'labels': [8, 7, 4, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9877346754074097})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9497069716453552})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.113158941268921})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0489792823791504})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9420989155769348})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0539746284484863})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1397050619125366})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0879368782043457})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8247, 'crossentropy': 0.97967802734375}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 53836], ['ood', 34979], ['id', 19513], ['id', 10439], ['ood', 2982]], 'labels': [9, 1, 9, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9731050133705139})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9700537323951721})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9285866618156433})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9517209529876709})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1041918992996216})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1001951694488525})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8263, 'crossentropy': 0.84509033203125}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 6903], ['ood', 42580], ['ood', 50407], ['ood', 56264], ['ood', 23184]], 'labels': [9, 0, 1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 0.9845865964889526})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9064339399337769})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9491817951202393})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9523160457611084})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0458645820617676})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8134, 'crossentropy': 0.844622265625}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 28536], ['id', 45500], ['id', 42292], ['id', 24949], ['ood', 19568]], 'labels': [2, 2, 7, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9826054573059082})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8914230465888977})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0792734622955322})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1004419326782227})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1107854843139648})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8174, 'crossentropy': 0.8299869140625}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 46827], ['id', 33071], ['id', 20111], ['id', 42159], ['id', 10986]], 'labels': [8, 5, 9, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8924389481544495})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9116379618644714})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8804168701171875})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9425464868545532})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9680832624435425})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.047778844833374})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.83, 'crossentropy': 0.82054306640625}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 59498], ['ood', 58195], ['ood', 51531], ['id', 21287], ['ood', 28351]], 'labels': [8, 3, 4, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9869013428688049})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9060059189796448})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9271718263626099})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8224407434463501})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0557146072387695})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0214450359344482})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9610286355018616})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8392, 'crossentropy': 0.83634150390625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 46699], ['id', 81], ['ood', 22357], ['id', 28042], ['id', 37707]], 'labels': [7, 0, 6, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9140487909317017})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8309898376464844})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9296954274177551})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9200812578201294})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0095322132110596})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8424, 'crossentropy': 0.736423779296875}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 38242], ['id', 36300], ['ood', 41870], ['id', 11879], ['ood', 51144]], 'labels': [0, 8, 2, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0263042449951172})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9433634877204895})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8781419992446899})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9853756427764893})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9624103307723999})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0377411842346191})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8506, 'crossentropy': 0.73823544921875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 28280], ['id', 13156], ['ood', 44503], ['ood', 153], ['id', 5258]], 'labels': [6, 2, 2, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0152373313903809})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9611498117446899})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9225805997848511})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9434882402420044})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.153339147567749})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9916882514953613})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8427, 'crossentropy': 0.814843408203125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 34569], ['id', 48835], ['ood', 51700], ['ood', 27609], ['ood', 33118]], 'labels': [9, 4, 1, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9202617406845093})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8391045928001404})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.006778359413147})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9147738218307495})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9690029621124268})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8337, 'crossentropy': 0.767168603515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 9886], ['ood', 47506], ['ood', 53664], ['ood', 47571], ['id', 2877]], 'labels': [7, 6, 4, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9129999876022339})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8728777170181274})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8689098358154297})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8858409523963928})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8839246034622192})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9200003147125244})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8437, 'crossentropy': 0.79977041015625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 53436], ['id', 24987], ['ood', 36739], ['id', 29948], ['ood', 33638]], 'labels': [1, 3, 1, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.0765020847320557})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8829660415649414})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9529978632926941})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9573180079460144})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0734646320343018})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8333, 'crossentropy': 0.7929287109375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 116], ['id', 21304], ['ood', 21961], ['id', 42655], ['ood', 47395]], 'labels': [5, 4, 2, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9175127148628235})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8460467457771301})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8428090810775757})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9506943821907043})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9704313278198242})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9577593803405762})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8583, 'crossentropy': 0.705124462890625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 42375], ['id', 27011], ['id', 24007], ['id', 15441], ['id', 9361]], 'labels': [3, 1, 8, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.9973931312561035})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8280973434448242})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7974461317062378})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.923595666885376})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8951436281204224})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8515149354934692})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.861, 'crossentropy': 0.7247013671875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 51718], ['id', 37613], ['id', 2059], ['ood', 31799], ['ood', 33728]], 'labels': [5, 2, 6, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.9117929935455322})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8047959208488464})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8658112287521362})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.820589542388916})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.830206036567688})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8566, 'crossentropy': 0.689592236328125}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 29034], ['ood', 9372], ['id', 40912], ['id', 36972], ['ood', 41804]], 'labels': [7, 1, 4, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9324156641960144})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.702775239944458})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7457501888275146})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7844997644424438})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7392393350601196})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8829, 'crossentropy': 0.61285576171875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 52884], ['ood', 48450], ['ood', 45150], ['id', 22363], ['id', 19778]], 'labels': [8, 0, 7, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8877130746841431})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7088222503662109})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7414329051971436})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7562093734741211})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7265549898147583})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8746, 'crossentropy': 0.642052099609375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 17233], ['id', 9855], ['ood', 36132], ['id', 27276], ['ood', 5165]], 'labels': [3, 2, 7, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9314820766448975})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.737031102180481})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7779275178909302})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8278295993804932})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7647944688796997})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8638, 'crossentropy': 0.663214501953125}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 50491], ['ood', 25300], ['id', 28666], ['ood', 51493], ['ood', 32056]], 'labels': [3, 1, 5, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8091288805007935})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7395579814910889})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6987316012382507})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7259336113929749})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7693882584571838})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7076215744018555})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.61822841796875}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 25195], ['ood', 5674], ['id', 43194], ['ood', 31699], ['ood', 29211]], 'labels': [3, 1, 8, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9288581609725952})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.786013662815094})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8029205203056335})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7883721590042114})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8446016907691956})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8609, 'crossentropy': 0.69979111328125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 3725], ['id', 14520], ['id', 10380], ['ood', 9565], ['ood', 26408]], 'labels': [1, 4, 0, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8173224329948425})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6712173819541931})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7335293292999268})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.709752082824707})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9062305688858032})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8763, 'crossentropy': 0.623496435546875}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 21910], ['ood', 57368], ['id', 4], ['ood', 12167], ['id', 1695]], 'labels': [0, 7, 9, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9202735424041748})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.709321141242981})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.758696436882019})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7362158298492432})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7422524690628052})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8771, 'crossentropy': 0.640543994140625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 17151], ['id', 29198], ['id', 1942], ['id', 53048], ['id', 3005]], 'labels': [1, 8, 1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8406885862350464})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6905492544174194})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7206281423568726})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7961809635162354})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7311978936195374})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8834, 'crossentropy': 0.6364958984375}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 7653], ['ood', 39459], ['ood', 56128], ['id', 24587], ['ood', 20938]], 'labels': [0, 3, 1, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9099980592727661})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7689265012741089})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8444206118583679})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8138177394866943})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7804274559020996})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8736, 'crossentropy': 0.65994375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 37055], ['id', 21474], ['id', 46430], ['ood', 29866], ['id', 15826]], 'labels': [7, 1, 0, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8064467906951904})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6539156436920166})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6856467127799988})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7702768445014954})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.802857518196106})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8741, 'crossentropy': 0.63610361328125}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 11459], ['id', 7254], ['ood', 31403], ['id', 26322], ['id', 3897]], 'labels': [9, 0, 8, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8345720767974854})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6968031525611877})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6897919178009033})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7645525932312012})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7936292886734009})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8428425788879395})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8715, 'crossentropy': 0.66700244140625}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 47358], ['ood', 28222], ['ood', 19786], ['id', 54908], ['ood', 17110]], 'labels': [1, 1, 9, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8611142635345459})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7237096428871155})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7001647353172302})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8431792259216309})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8415714502334595})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8579486608505249})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8781, 'crossentropy': 0.656766748046875}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 44802], ['ood', 41886], ['ood', 55914], ['ood', 37227], ['id', 43742]], 'labels': [5, 4, 4, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9145236015319824})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7889435887336731})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.732781171798706})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7603750228881836})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8569146394729614})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7429611682891846})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8782, 'crossentropy': 0.622856689453125}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 23223], ['id', 46743], ['id', 8651], ['id', 27235], ['id', 20138]], 'labels': [0, 3, 7, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8402377963066101})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7064678072929382})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.738078773021698})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.886581540107727})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7885703444480896})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8684, 'crossentropy': 0.645069140625}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 32246], ['id', 48828], ['ood', 21358], ['ood', 3131], ['ood', 46231]], 'labels': [2, 8, 2, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8142577409744263})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6897875070571899})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7632235288619995})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7164233922958374})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7146368622779846})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8635, 'crossentropy': 0.664310009765625}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 57885], ['ood', 51113], ['ood', 19371], ['ood', 54564], ['ood', 5667]], 'labels': [7, 5, 3, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8843981027603149})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7648221850395203})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7926163673400879})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7301582098007202})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8159825205802917})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.824560284614563})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8439579606056213})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8827, 'crossentropy': 0.660266943359375}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 7301], ['ood', 9119], ['id', 16193], ['id', 38895], ['id', 59596]], 'labels': [7, 2, 3, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7715277671813965})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.672626256942749})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7501895427703857})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6686750650405884})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7010936737060547})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.781111478805542})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8245612382888794})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.892, 'crossentropy': 0.5859513671875}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 28817], ['id', 6190], ['ood', 19135], ['id', 20041], ['id', 33389]], 'labels': [6, 2, 6, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8882083296775818})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6890439391136169})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.673149824142456})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7015631198883057})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7404876351356506})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7343736886978149})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8788, 'crossentropy': 0.604792919921875}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 14666], ['ood', 46353], ['id', 15445], ['id', 27872], ['ood', 44684]], 'labels': [7, 2, 0, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8527517318725586})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6383699178695679})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6542230844497681})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.672853946685791})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7059587240219116})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8811, 'crossentropy': 0.628660107421875}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 30505], ['id', 10665], ['ood', 54298], ['ood', 21920], ['id', 21427]], 'labels': [9, 5, 8, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8626316785812378})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.642756998538971})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6520107984542847})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.716301679611206})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7042701244354248})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8812, 'crossentropy': 0.614239306640625}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 51634], ['id', 21069], ['id', 46502], ['id', 7341], ['id', 43116]], 'labels': [7, 0, 8, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8801391124725342})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6020315885543823})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6401086449623108})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6670877933502197})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6792883276939392})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8932, 'crossentropy': 0.56946103515625}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 36800], ['id', 47264], ['ood', 57341], ['ood', 13728], ['ood', 31412]], 'labels': [5, 9, 2, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8739315271377563})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.645391583442688})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6799854040145874})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6931706070899963})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7025866508483887})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8874, 'crossentropy': 0.608450927734375}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 43056], ['ood', 51881], ['ood', 16474], ['ood', 220], ['id', 45182]], 'labels': [5, 5, 9, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8998308777809143})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6867418885231018})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.652625322341919})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6692819595336914})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6503633856773376})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7226626873016357})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.789760410785675})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7261068820953369})
store['active_learning_steps'][58]['training']['best_epoch']=5
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8981, 'crossentropy': 0.590559521484375}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 33099], ['ood', 45041], ['ood', 12755], ['id', 26231], ['ood', 18007]], 'labels': [3, 4, 1, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8825520873069763})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.641610860824585})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6908807754516602})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6800963878631592})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.701671838760376})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8781, 'crossentropy': 0.623746337890625}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 4879], ['ood', 15072], ['ood', 2005], ['ood', 1629], ['id', 30465]], 'labels': [9, 9, 8, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8026697039604187})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.629359245300293})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6590946912765503})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6633645296096802})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6643884181976318})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8929, 'crossentropy': 0.571123095703125}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 26124], ['ood', 39467], ['id', 2698], ['id', 5955], ['id', 23521]], 'labels': [6, 9, 5, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8942257165908813})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6267522573471069})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5905500650405884})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6630692481994629})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6757901906967163})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6753324270248413})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8922, 'crossentropy': 0.566621484375}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 56344], ['ood', 35295], ['id', 51811], ['id', 5169], ['ood', 35386]], 'labels': [1, 0, 3, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8442168235778809})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6624048948287964})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6368379592895508})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6640106439590454})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6676907539367676})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.715561032295227})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8948, 'crossentropy': 0.57803818359375}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 6578], ['id', 17872], ['id', 27650], ['ood', 53292], ['ood', 21648]], 'labels': [4, 1, 8, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8545416593551636})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6994008421897888})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6824419498443604})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7269937992095947})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7061947584152222})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7497076988220215})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.5795578125}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 11332], ['id', 38866], ['ood', 47304], ['ood', 44135], ['ood', 45247]], 'labels': [0, 8, 4, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.733549952507019})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5936115980148315})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5875413417816162})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5891860723495483})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6461365222930908})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6003649234771729})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.502783056640625}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 51639], ['id', 48531], ['ood', 50734], ['id', 49666], ['id', 10394]], 'labels': [4, 2, 1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8548789620399475})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6623126268386841})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6659455299377441})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6556452512741089})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7157129049301147})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6864352226257324})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6780008673667908})
store['active_learning_steps'][65]['training']['best_epoch']=4
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.567149267578125}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 8613], ['id', 14936], ['ood', 4494], ['id', 2447], ['ood', 29787]], 'labels': [5, 1, 2, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9046754240989685})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.620894193649292})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5857603549957275})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6165468692779541})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.679124653339386})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6233201622962952})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.509627685546875}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 51695], ['ood', 23909], ['id', 47858], ['ood', 24919], ['id', 50679]], 'labels': [3, 8, 5, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8413274884223938})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7272288799285889})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6141015291213989})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6845357418060303})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.607693076133728})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6300902366638184})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6888148784637451})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7687482237815857})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.549462451171875}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 37622], ['id', 46865], ['id', 58363], ['id', 15286], ['id', 7854]], 'labels': [3, 1, 9, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9148852825164795})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6727454662322998})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6398200392723083})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6764318943023682})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7364056706428528})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6864624619483948})
store['active_learning_steps'][68]['training']['best_epoch']=3
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8933, 'crossentropy': 0.5786529296875}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 47059], ['id', 41267], ['id', 23608], ['ood', 32862], ['ood', 29878]], 'labels': [3, 3, 4, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9054930806159973})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6317551732063293})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5611456036567688})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.534238338470459})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6482753753662109})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.633229672908783})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7179878950119019})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9142, 'crossentropy': 0.503626708984375}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 9615], ['ood', 56915], ['id', 28433], ['id', 1392], ['id', 41893]], 'labels': [4, 1, 8, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8901407122612})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6105753183364868})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6064974069595337})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6192224025726318})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6015588045120239})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5692975521087646})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6029921770095825})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7679986953735352})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.682249903678894})
store['active_learning_steps'][70]['training']['best_epoch']=6
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.505794873046875}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 9002], ['id', 25733], ['ood', 27362], ['id', 42841], ['id', 15790]], 'labels': [6, 7, 9, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.858191728591919})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6068259477615356})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5828858017921448})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5389291048049927})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5965464115142822})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6084784269332886})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6576725244522095})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.483224365234375}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 58015], ['ood', 7480], ['id', 55919], ['id', 59307], ['ood', 29422]], 'labels': [0, 1, 2, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7670912742614746})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5441571474075317})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5418412685394287})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5645835399627686})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5388888120651245})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6008049845695496})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6011010408401489})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5759865641593933})
store['active_learning_steps'][72]['training']['best_epoch']=5
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.493034765625}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 30090], ['id', 36052], ['ood', 22450], ['ood', 27218], ['id', 27927]], 'labels': [2, 7, 3, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8389942646026611})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5887413024902344})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5679326057434082})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5664945244789124})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6390769481658936})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6034337282180786})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6075196862220764})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.913, 'crossentropy': 0.48161494140625}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 50721], ['ood', 6074], ['id', 44884], ['id', 53938], ['id', 34853]], 'labels': [7, 9, 9, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8993425965309143})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6256529092788696})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.551802933216095})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5440092086791992})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5520910024642944})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5816267728805542})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6336103677749634})
store['active_learning_steps'][74]['training']['best_epoch']=4
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.507833203125}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 9434], ['ood', 25315], ['id', 34087], ['ood', 15172], ['id', 51960]], 'labels': [7, 4, 2, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8803110718727112})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5620481967926025})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5429607033729553})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5505987405776978})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.583503246307373})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5877498388290405})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.488415771484375}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 8083], ['id', 55262], ['id', 47216], ['id', 18566], ['id', 55036]], 'labels': [9, 1, 1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7980714440345764})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5523948669433594})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5733182430267334})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6136707663536072})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5009762048721313})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5957716703414917})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.564711332321167})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.580030620098114})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.446326708984375}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 13631], ['ood', 13541], ['ood', 58210], ['ood', 54578], ['id', 22459]], 'labels': [0, 1, 6, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8631441593170166})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6557358503341675})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5583745837211609})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.598749041557312})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6416085958480835})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5838677883148193})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.48926904296875}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 39789], ['id', 40463], ['id', 47634], ['id', 3470], ['id', 2686]], 'labels': [0, 3, 8, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9115016460418701})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6410189867019653})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.662665605545044})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.604316234588623})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5956776142120361})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5857511758804321})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6005659103393555})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6013303399085999})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6349086165428162})
store['active_learning_steps'][78]['training']['best_epoch']=6
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.52221591796875}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 41461], ['ood', 48742], ['id', 58631], ['ood', 42514], ['ood', 30054]], 'labels': [4, 5, 7, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8351370096206665})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5720530152320862})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5633072257041931})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5280524492263794})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5647401213645935})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5483324527740479})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5618872046470642})
store['active_learning_steps'][79]['training']['best_epoch']=4
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9209, 'crossentropy': 0.447357958984375}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 22510], ['ood', 35075], ['ood', 58140], ['id', 10331], ['id', 13334]], 'labels': [9, 5, 0, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8108751773834229})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5894532203674316})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5587807893753052})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5506151914596558})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5501999855041504})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5741629600524902})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5665448904037476})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5645186305046082})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.452362158203125}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 50371], ['ood', 20059], ['id', 10874], ['id', 57700], ['id', 59293]], 'labels': [1, 7, 0, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8231099843978882})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6060413122177124})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5827540159225464})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5224354863166809})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5268583297729492})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5456345677375793})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5827073454856873})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.458795361328125}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 43114], ['ood', 5736], ['id', 35916], ['ood', 8583], ['ood', 13371]], 'labels': [9, 2, 8, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8079797029495239})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.516632080078125})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.49500152468681335})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4934735894203186})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5463861227035522})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5489674806594849})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5239434242248535})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9219, 'crossentropy': 0.462546533203125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 16187], ['id', 19164], ['ood', 9054], ['id', 18274], ['id', 13812]], 'labels': [6, 7, 8, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.827441930770874})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5715731978416443})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5235490798950195})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49440646171569824})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5600782632827759})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5173164010047913})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5508075952529907})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.442315478515625}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 23645], ['id', 48912], ['ood', 6002], ['ood', 49450], ['ood', 25158]], 'labels': [1, 2, 4, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8468458652496338})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5570252537727356})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5499554872512817})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5532121658325195})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5722626447677612})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5355177521705627})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5695497393608093})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5391957759857178})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5917830467224121})
store['active_learning_steps'][84]['training']['best_epoch']=6
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.49954873046875}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 38088], ['ood', 15038], ['id', 57413], ['ood', 6196], ['id', 25161]], 'labels': [7, 1, 6, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7348607778549194})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5809211134910583})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4749554395675659})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5459926128387451})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5041335225105286})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.508209228515625})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.43602294921875}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 52633], ['ood', 56291], ['ood', 53373], ['ood', 18803], ['ood', 5256]], 'labels': [4, 9, 0, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9207382798194885})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.611564040184021})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5409270524978638})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5798020362854004})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.519666314125061})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5342180132865906})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5686098337173462})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5346881151199341})
store['active_learning_steps'][86]['training']['best_epoch']=5
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.49258076171875}
