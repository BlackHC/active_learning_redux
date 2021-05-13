store = {}
store['timestamp']=1620259766
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=21']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=21
store['worker_id']=21
store['num_workers']=40
store['config']={'seed': 22, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4040708541870117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8182177543640137})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8356027603149414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.934849739074707})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6696, 'crossentropy': 2.2352109375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 44214], ['id', 31894], ['id', 31859], ['id', 15791], ['ood', 8747]], 'labels': [9, 1, 6, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.105020523071289})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.286207675933838})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.6391258239746094})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7856922149658203})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6356, 'crossentropy': 1.8171404296875}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 27939], ['id', 47348], ['id', 2853], ['ood', 24326], ['id', 22598]], 'labels': [6, 5, 1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6853618621826172})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.9188735485076904})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.277225971221924})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.5993618965148926})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.708, 'crossentropy': 1.46314853515625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 29206], ['id', 34761], ['id', 48338], ['id', 58171], ['ood', 20164]], 'labels': [5, 9, 6, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.8740736246109009})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.3643479347229004})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.3356311321258545})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.484889507293701})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.659, 'crossentropy': 1.60530400390625}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 43052], ['id', 10155], ['id', 27833], ['ood', 44245], ['ood', 11543]], 'labels': [9, 3, 6, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3579504489898682})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6943094730377197})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.7440850734710693})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.9468865394592285})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7078, 'crossentropy': 1.3001728515625}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 42987], ['id', 25879], ['id', 24862], ['ood', 20197], ['id', 35141]], 'labels': [2, 8, 2, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.162724494934082})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.174628734588623})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3338676691055298})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.3865139484405518})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7622, 'crossentropy': 1.08781708984375}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 23403], ['id', 49404], ['ood', 47214], ['ood', 3610], ['ood', 23812]], 'labels': [1, 3, 9, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1056265830993652})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2079310417175293})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.551098108291626})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.602579116821289})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7827, 'crossentropy': 0.9994013671875}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 42231], ['ood', 49406], ['ood', 19243], ['ood', 28511], ['ood', 59857]], 'labels': [8, 0, 6, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.155104398727417})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1091790199279785})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3452377319335938})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.314465045928955})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3430538177490234})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7907, 'crossentropy': 0.9895833984375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 11397], ['id', 12325], ['ood', 5861], ['id', 6296], ['ood', 56180]], 'labels': [5, 0, 6, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.365159273147583})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4552009105682373})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.5778988599777222})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.4907917976379395})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7306, 'crossentropy': 1.17400078125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 56635], ['ood', 46628], ['ood', 4752], ['id', 13584], ['id', 21074]], 'labels': [0, 3, 8, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2725279331207275})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3096511363983154})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.4146595001220703})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.4888336658477783})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7517, 'crossentropy': 1.1033814453125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 38635], ['ood', 15779], ['id', 13176], ['ood', 47612], ['id', 24873]], 'labels': [2, 2, 8, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.152292251586914})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.204820990562439})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.343646764755249})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.432917833328247})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7869, 'crossentropy': 0.98224306640625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 32311], ['id', 58289], ['ood', 23667], ['ood', 4470], ['id', 25007]], 'labels': [9, 4, 2, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.177118182182312})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1957210302352905})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2047648429870605})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3114372491836548})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7508, 'crossentropy': 1.06656259765625}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 27978], ['ood', 15452], ['id', 13165], ['id', 48627], ['id', 47091]], 'labels': [5, 7, 5, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0341429710388184})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1180959939956665})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1282117366790771})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.102921724319458})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7968, 'crossentropy': 0.90335322265625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 14156], ['id', 4118], ['ood', 54727], ['ood', 21011], ['ood', 33603]], 'labels': [4, 9, 0, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9809293746948242})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0330989360809326})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2618281841278076})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3583300113677979})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7929, 'crossentropy': 0.9181076171875}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 3411], ['id', 52178], ['id', 15061], ['id', 17710], ['id', 8202]], 'labels': [3, 7, 6, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.979560375213623})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1828296184539795})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0562248229980469})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2406973838806152})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.781, 'crossentropy': 0.95143857421875}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 37240], ['ood', 54178], ['ood', 34764], ['id', 7959], ['ood', 40165]], 'labels': [5, 8, 2, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9321157932281494})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9567451477050781})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9313646554946899})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9724252223968506})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.001094102859497})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.078365683555603})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8195, 'crossentropy': 0.94767080078125}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 13418], ['id', 29993], ['ood', 17408], ['ood', 46034], ['ood', 46883]], 'labels': [5, 9, 5, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9722151756286621})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8600026369094849})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9211150407791138})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9287516474723816})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9480875730514526})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8241, 'crossentropy': 0.89704638671875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 30512], ['ood', 26505], ['ood', 47715], ['id', 23761], ['ood', 22770]], 'labels': [1, 1, 9, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9045250415802002})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8757702112197876})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9436335563659668})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9371533393859863})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.975467324256897})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8369, 'crossentropy': 0.783411083984375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 29025], ['id', 5721], ['id', 41568], ['ood', 49145], ['ood', 13424]], 'labels': [2, 6, 4, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9372907876968384})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7601256966590881})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8660382032394409})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9107507467269897})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9558861255645752})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8559, 'crossentropy': 0.73023037109375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 39052], ['id', 26137], ['ood', 44118], ['id', 42713], ['id', 49334]], 'labels': [9, 4, 7, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9322710037231445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8345903754234314})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8614252209663391})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.902301549911499})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8978514671325684})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8531, 'crossentropy': 0.760847900390625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 39468], ['id', 1235], ['id', 14051], ['id', 16889], ['ood', 18289]], 'labels': [5, 9, 6, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8931549787521362})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8068803548812866})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8172169923782349})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8472505807876587})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8626657724380493})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8544, 'crossentropy': 0.758236962890625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 20652], ['id', 35069], ['id', 28277], ['id', 22667], ['ood', 16553]], 'labels': [4, 1, 5, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.9849329590797424})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8955714702606201})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9331454634666443})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0319311618804932})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9767044186592102})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.835, 'crossentropy': 0.8357259765625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 52629], ['id', 15563], ['ood', 54047], ['id', 10522], ['id', 59177]], 'labels': [0, 4, 3, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.959835946559906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8498675227165222})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8825798034667969})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8678810000419617})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9400036334991455})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8477, 'crossentropy': 0.75966025390625}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 42148], ['id', 20676], ['ood', 59329], ['ood', 5294], ['ood', 30804]], 'labels': [9, 9, 7, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8742213249206543})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8299511671066284})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8283941149711609})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9566390514373779})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9028083682060242})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9157258868217468})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8529, 'crossentropy': 0.768892919921875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 25324], ['id', 37480], ['id', 45158], ['id', 40307], ['ood', 19176]], 'labels': [1, 7, 2, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8762736320495605})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8463584184646606})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8433550596237183})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8730897903442383})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8946967124938965})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.978546142578125})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8636, 'crossentropy': 0.783345947265625}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 50505], ['ood', 15143], ['ood', 33481], ['id', 24996], ['ood', 6793]], 'labels': [7, 3, 9, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9195845723152161})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8471437692642212})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8017507195472717})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8939944505691528})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9050858020782471})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9774267673492432})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8531, 'crossentropy': 0.777676220703125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 41642], ['ood', 14404], ['id', 8617], ['ood', 47623], ['ood', 163]], 'labels': [6, 9, 2, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.9364715814590454})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8145644664764404})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8228925466537476})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.878404974937439})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9974557161331177})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8514, 'crossentropy': 0.763691259765625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 10646], ['id', 19947], ['id', 4175], ['ood', 2195], ['ood', 59477]], 'labels': [9, 6, 7, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8826358318328857})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8486405611038208})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.002575397491455})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9732930660247803})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9595164656639099})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8478, 'crossentropy': 0.78641171875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 30743], ['id', 4230], ['ood', 35505], ['id', 55137], ['id', 59589]], 'labels': [8, 2, 3, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8652581572532654})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7343739867210388})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8485983610153198})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7984733581542969})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8833503723144531})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8624, 'crossentropy': 0.679181396484375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 57184], ['id', 1040], ['ood', 16753], ['ood', 23461], ['ood', 25114]], 'labels': [4, 0, 1, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8638111352920532})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7297670841217041})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7355297803878784})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8195558786392212})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7944620847702026})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8634, 'crossentropy': 0.680250830078125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 26530], ['id', 58782], ['id', 872], ['id', 8183], ['id', 35625]], 'labels': [6, 0, 0, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8325773477554321})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7576112747192383})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7723533511161804})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7844575047492981})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9131981134414673})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.871, 'crossentropy': 0.675190771484375}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 47690], ['id', 30233], ['ood', 19429], ['id', 43312], ['ood', 21681]], 'labels': [1, 5, 9, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8394885063171387})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7610806226730347})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8030812740325928})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7899542450904846})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8509600162506104})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8748, 'crossentropy': 0.638478125}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 15681], ['id', 54247], ['id', 23748], ['ood', 38032], ['id', 47312]], 'labels': [3, 2, 9, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8412861227989197})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7256155014038086})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7379170656204224})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8042150735855103})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8078163862228394})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8668, 'crossentropy': 0.67105146484375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 21072], ['ood', 16143], ['ood', 9288], ['id', 51002], ['id', 47682]], 'labels': [9, 2, 7, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9730138778686523})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7439392805099487})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7685458064079285})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7932274341583252})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8666995763778687})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8747, 'crossentropy': 0.661588818359375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 27006], ['id', 5684], ['id', 17652], ['id', 51119], ['ood', 3716]], 'labels': [6, 6, 6, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.920470118522644})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7258623838424683})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7306585311889648})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8392511606216431})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.818302571773529})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8647, 'crossentropy': 0.687773974609375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 44778], ['id', 56510], ['id', 15505], ['id', 53700], ['id', 27978]], 'labels': [9, 7, 0, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7953016757965088})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7227230072021484})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7428747415542603})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7222113013267517})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8202430009841919})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8868700265884399})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7969793677330017})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.671384033203125}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 28814], ['id', 11404], ['id', 44577], ['ood', 43947], ['ood', 59718]], 'labels': [2, 1, 7, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8790673017501831})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7411723136901855})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8279271125793457})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7709215879440308})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.790542721748352})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8666, 'crossentropy': 0.70470966796875}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 5894], ['id', 59385], ['ood', 58144], ['ood', 37873], ['id', 53722]], 'labels': [0, 9, 0, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8396716117858887})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8193211555480957})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.854316234588623})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8562384843826294})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7825455665588379})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7954501509666443})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.838652491569519})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9057605862617493})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8836, 'crossentropy': 0.7139642578125}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 2651], ['ood', 41792], ['ood', 22453], ['ood', 40733], ['id', 3451]], 'labels': [1, 9, 1, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8415641784667969})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6872869729995728})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7236549258232117})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7404057383537292})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7398849725723267})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8768, 'crossentropy': 0.6208591796875}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 14169], ['ood', 908], ['ood', 24437], ['ood', 39192], ['ood', 18725]], 'labels': [1, 7, 2, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8153567910194397})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6845036745071411})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7480302453041077})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7781763076782227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8542085886001587})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8715, 'crossentropy': 0.66846982421875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 18126], ['ood', 35689], ['ood', 50789], ['ood', 28403], ['id', 23211]], 'labels': [8, 5, 6, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.884299635887146})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7479038238525391})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7884238958358765})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7969807386398315})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7673763036727905})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8677, 'crossentropy': 0.685665869140625}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 49166], ['ood', 47846], ['ood', 41426], ['ood', 5604], ['id', 54042]], 'labels': [9, 5, 2, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8493322134017944})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7280138731002808})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7819191813468933})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7611352205276489})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7968692779541016})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8744, 'crossentropy': 0.6664330078125}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 11735], ['ood', 22917], ['id', 21856], ['ood', 55184], ['ood', 57899]], 'labels': [6, 4, 6, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8291096687316895})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6342500448226929})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.733871340751648})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7920430898666382})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7073278427124023})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8846, 'crossentropy': 0.60142724609375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 52005], ['ood', 26518], ['id', 43182], ['ood', 3062], ['ood', 23351]], 'labels': [2, 0, 8, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8174065351486206})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7068233489990234})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7168844938278198})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7414367198944092})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6513689160346985})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7619736194610596})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7421250343322754})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8575246334075928})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.621532568359375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 12684], ['id', 8990], ['id', 1362], ['id', 21710], ['ood', 27486]], 'labels': [5, 7, 8, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7555217742919922})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6311740875244141})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.712112545967102})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7440000176429749})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6933577060699463})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.59746796875}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 32798], ['ood', 7949], ['ood', 6778], ['ood', 57791], ['id', 30411]], 'labels': [7, 5, 5, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7828893065452576})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5923044681549072})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6677956581115723})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6388427019119263})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6962382793426514})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.533848486328125}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 41885], ['id', 10758], ['ood', 57676], ['id', 5150], ['ood', 4359]], 'labels': [3, 4, 7, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.779643177986145})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7043912410736084})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.683536946773529})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7176263332366943})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6955440640449524})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7293806076049805})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8877, 'crossentropy': 0.60539033203125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 24178], ['id', 27393], ['ood', 11050], ['id', 11922], ['ood', 46886]], 'labels': [9, 2, 6, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8349336385726929})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6523292660713196})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6886674165725708})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8732815384864807})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7287442684173584})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8876, 'crossentropy': 0.60931337890625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 21306], ['ood', 2801], ['id', 35896], ['id', 10082], ['id', 12592]], 'labels': [3, 8, 0, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8693047761917114})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6481289863586426})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6400461196899414})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.631296694278717})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.600372850894928})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6682994365692139})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6973663568496704})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6833267211914062})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.550958447265625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 23757], ['id', 54593], ['ood', 38350], ['ood', 51528], ['ood', 29355]], 'labels': [2, 8, 6, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8244061470031738})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6069087982177734})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5930110812187195})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6515354514122009})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6970981359481812})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6769202947616577})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.527464794921875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 31107], ['ood', 17164], ['id', 30579], ['id', 21927], ['id', 36729]], 'labels': [5, 0, 7, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8367968797683716})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6256049871444702})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6598347425460815})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.678497314453125})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6732324361801147})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.5846271484375}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 25673], ['id', 62], ['ood', 9883], ['id', 55370], ['ood', 1697]], 'labels': [4, 6, 3, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8530336618423462})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7240009903907776})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6702565550804138})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6269841194152832})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7145322561264038})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7371224164962769})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7139122486114502})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.564144091796875}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 35685], ['ood', 54068], ['id', 7736], ['id', 17538], ['ood', 52454]], 'labels': [2, 9, 2, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.812666118144989})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6389573812484741})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7424969673156738})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6510918736457825})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6537911891937256})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.889, 'crossentropy': 0.574882958984375}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 31004], ['id', 57413], ['ood', 43153], ['id', 45945], ['ood', 14691]], 'labels': [6, 6, 1, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.871846079826355})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6269650459289551})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6397730112075806})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6906698942184448})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6945270299911499})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8885, 'crossentropy': 0.59994013671875}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 2825], ['id', 26194], ['ood', 4280], ['ood', 9304], ['id', 10802]], 'labels': [6, 3, 4, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8476963043212891})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6360743045806885})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5855878591537476})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6816188097000122})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7259474992752075})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6703456044197083})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8959, 'crossentropy': 0.551415771484375}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 30272], ['ood', 31019], ['id', 54397], ['ood', 52810], ['ood', 2431]], 'labels': [7, 0, 3, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7579338550567627})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6392033100128174})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6373716592788696})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7423561811447144})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6083357334136963})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7193868160247803})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7299588322639465})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7581403255462646})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.558772119140625}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 2061], ['id', 20696], ['ood', 9411], ['ood', 801], ['ood', 15748]], 'labels': [2, 4, 5, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7580218315124512})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5895850658416748})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5832213163375854})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5842146277427673})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6579275131225586})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.593213677406311})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.543937841796875}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 36927], ['ood', 50927], ['ood', 58815], ['id', 20139], ['ood', 29562]], 'labels': [8, 6, 9, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8235724568367004})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6651970148086548})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5612086057662964})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.646694540977478})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5957940816879272})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7414794564247131})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.51164375}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 28515], ['ood', 55862], ['id', 44753], ['ood', 11008], ['ood', 22534]], 'labels': [4, 6, 5, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8117126226425171})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6269009113311768})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5910617709159851})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6304442882537842})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5739157199859619})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6020251512527466})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6165626049041748})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6610521674156189})
store['active_learning_steps'][58]['training']['best_epoch']=5
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.52895029296875}
store['active_learning_steps'][58]['acquisition']={'indices': [['ood', 29700], ['id', 7571], ['ood', 46024], ['ood', 12573], ['ood', 20670]], 'labels': [5, 6, 4, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8278051018714905})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6277161836624146})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6234033703804016})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.726753830909729})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6719726324081421})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6486637592315674})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9011, 'crossentropy': 0.5338591796875}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 364], ['id', 24621], ['ood', 41701], ['ood', 11268], ['id', 7744]], 'labels': [7, 3, 6, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9203066825866699})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6643999218940735})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6368993520736694})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6578662991523743})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7191133499145508})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.660662055015564})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.596415185546875}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 12602], ['ood', 15315], ['ood', 10119], ['ood', 31250], ['id', 36180]], 'labels': [3, 5, 9, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7683072090148926})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5962643027305603})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.600641667842865})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5520963072776794})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5874722599983215})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6184794902801514})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6142047047615051})
store['active_learning_steps'][61]['training']['best_epoch']=4
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.496072412109375}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 46019], ['ood', 11592], ['id', 7057], ['ood', 23256], ['ood', 5483]], 'labels': [7, 2, 1, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8222746849060059})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.624328076839447})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6093837022781372})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6657564640045166})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6421047449111938})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6863213777542114})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.551705224609375}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 35428], ['ood', 58226], ['id', 10632], ['ood', 49787], ['id', 25707]], 'labels': [8, 6, 8, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7996341586112976})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.637622594833374})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6069557666778564})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5778846740722656})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6587302684783936})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6804165244102478})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.639985203742981})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.534224951171875}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 19813], ['id', 47729], ['id', 48027], ['ood', 12656], ['id', 29979]], 'labels': [4, 1, 1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7593125104904175})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.588349461555481})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5612131357192993})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6299756169319153})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5196665525436401})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6657004952430725})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6586958169937134})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6975083351135254})
store['active_learning_steps'][64]['training']['best_epoch']=5
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.49093779296875}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 55389], ['ood', 4534], ['id', 17532], ['id', 3761], ['ood', 36781]], 'labels': [9, 1, 7, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8528841733932495})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5675725936889648})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.550299882888794})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.564061164855957})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.612055778503418})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.617708146572113})
store['active_learning_steps'][65]['training']['best_epoch']=3
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.495451171875}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 38138], ['id', 44383], ['id', 29142], ['ood', 13939], ['ood', 57611]], 'labels': [0, 5, 8, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9032700061798096})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6505229473114014})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5782852172851562})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6209815740585327})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.561002254486084})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6369471549987793})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6057056188583374})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6262558698654175})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.508732861328125}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 3574], ['id', 56385], ['ood', 31757], ['ood', 59548], ['id', 13080]], 'labels': [2, 6, 6, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8435312509536743})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5852537751197815})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5694218873977661})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.563933253288269})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.61788010597229})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5755146741867065})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6717327833175659})
store['active_learning_steps'][67]['training']['best_epoch']=4
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.49866103515625}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 56759], ['ood', 27083], ['id', 25891], ['id', 46902], ['ood', 27636]], 'labels': [7, 5, 5, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7994378805160522})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5829837918281555})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5838853716850281})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.555899977684021})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5812543630599976})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6074079275131226})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6297245621681213})
store['active_learning_steps'][68]['training']['best_epoch']=4
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.49743486328125}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 35505], ['id', 21991], ['id', 46165], ['id', 53998], ['ood', 37160]], 'labels': [0, 1, 1, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8280249834060669})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5777105689048767})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6278586387634277})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5801201462745667})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5865596532821655})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.52987353515625}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 32899], ['ood', 50407], ['ood', 22580], ['id', 34365], ['ood', 39879]], 'labels': [4, 1, 6, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7682543992996216})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6088109016418457})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5503630638122559})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6238083839416504})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5741564035415649})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6227343082427979})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.48952939453125}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 14977], ['ood', 50905], ['id', 16517], ['ood', 3982], ['ood', 38862]], 'labels': [9, 4, 8, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8506867289543152})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6452398300170898})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6173179745674133})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.621163010597229})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6173927187919617})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6591102480888367})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.54641982421875}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 23908], ['id', 33529], ['ood', 1022], ['id', 45605], ['ood', 32288]], 'labels': [1, 3, 2, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8177943229675293})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6111329793930054})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5978988409042358})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5752940773963928})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5794066190719604})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.594398021697998})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6335866451263428})
store['active_learning_steps'][72]['training']['best_epoch']=4
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.497380126953125}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 3276], ['id', 5473], ['ood', 48374], ['ood', 13403], ['ood', 10556]], 'labels': [4, 7, 7, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.756275475025177})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5573562383651733})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5899003148078918})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5594673156738281})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6616965532302856})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.489643212890625}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 8509], ['ood', 26160], ['ood', 175], ['id', 22936], ['id', 51807]], 'labels': [3, 3, 7, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7917860746383667})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6133939027786255})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6134757995605469})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5931599140167236})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6632181406021118})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6704625487327576})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6883957386016846})
store['active_learning_steps'][74]['training']['best_epoch']=4
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.522154541015625}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 54061], ['id', 10960], ['ood', 7666], ['ood', 5646], ['id', 31853]], 'labels': [8, 4, 2, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8138828277587891})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5658643245697021})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5945212841033936})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5807183384895325})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6000901460647583})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.5519607421875}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 44278], ['id', 54496], ['ood', 20568], ['id', 7544], ['ood', 55153]], 'labels': [7, 6, 6, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8087775707244873})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6041295528411865})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5454127788543701})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5871937274932861})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5950192809104919})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6559196710586548})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.472762451171875}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 29081], ['id', 55194], ['ood', 30609], ['id', 6251], ['ood', 20012]], 'labels': [2, 3, 3, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8419584035873413})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.563476026058197})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5874605178833008})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6247236728668213})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5907105803489685})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.516499755859375}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 5639], ['ood', 4639], ['id', 18171], ['ood', 40115], ['ood', 52182]], 'labels': [4, 3, 0, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8388134241104126})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6517664194107056})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6152782440185547})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5992246866226196})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6788126230239868})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6186305284500122})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6306444406509399})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.501173388671875}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 3435], ['ood', 12856], ['ood', 29109], ['id', 49802], ['id', 30901]], 'labels': [8, 0, 5, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8758766651153564})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5702091455459595})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6301988363265991})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6068270802497864})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6316820979118347})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.5424291015625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 5865], ['ood', 30139], ['id', 23047], ['ood', 19196], ['ood', 45737]], 'labels': [9, 2, 3, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8922257423400879})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6093662977218628})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6249609589576721})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6361033916473389})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6370015144348145})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.55929287109375}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 49434], ['id', 57951], ['id', 3376], ['ood', 44205], ['ood', 15581]], 'labels': [2, 5, 0, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8729881048202515})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6013948917388916})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5659703612327576})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5878843665122986})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5575799345970154})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6118006110191345})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6064955592155457})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6436297297477722})
store['active_learning_steps'][81]['training']['best_epoch']=5
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.481512255859375}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 57790], ['ood', 53949], ['id', 54288], ['ood', 37100], ['ood', 31926]], 'labels': [2, 4, 6, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.770797848701477})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5972445011138916})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.571692943572998})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6056007742881775})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6411523818969727})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5661139488220215})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5938222408294678})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5926123857498169})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.573879063129425})
store['active_learning_steps'][82]['training']['best_epoch']=6
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.476437841796875}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 34954], ['ood', 7305], ['id', 50939], ['id', 49037], ['ood', 59793]], 'labels': [9, 6, 5, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.854027509689331})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6285861134529114})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5950539112091064})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6135294437408447})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6301980018615723})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6443227529525757})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.54518759765625}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 54075], ['id', 15397], ['ood', 34149], ['id', 5637], ['id', 48666]], 'labels': [0, 1, 8, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8310140371322632})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6136962175369263})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5522882342338562})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.559969425201416})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6048167943954468})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6069419384002686})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.484472021484375}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 5585], ['ood', 38324], ['id', 1908], ['ood', 58287], ['ood', 37773]], 'labels': [0, 4, 3, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8328143358230591})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5898545980453491})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5652591586112976})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5511999130249023})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5610657930374146})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6022931337356567})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6236922740936279})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.478738916015625}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 37223], ['ood', 21245], ['ood', 57705], ['id', 2788], ['id', 3314]], 'labels': [5, 0, 3, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8495115637779236})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5989323854446411})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5987788438796997})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.614172101020813})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5576425194740295})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6410267353057861})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6100927591323853})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6516140699386597})
store['active_learning_steps'][86]['training']['best_epoch']=5
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.503089208984375}
