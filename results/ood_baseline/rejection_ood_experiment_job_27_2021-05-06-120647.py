store = {}
store['timestamp']=1620299207
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=27']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=27
store['worker_id']=27
store['num_workers']=40
store['config']={'seed': 34, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2561469078063965})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.37519907951355})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.5818400382995605})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.778855800628662})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6971, 'crossentropy': 1.9335654296875}
store['active_learning_steps'][0]['acquisition']={'indices': [33079, 42263, 20165, 33651, 3460], 'labels': [0, -1, -1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.9511191844940186})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.3807661533355713})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.3203461170196533})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.423921823501587})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.719, 'crossentropy': 1.814090234375}
store['active_learning_steps'][1]['acquisition']={'indices': [51225, 45278, 12544, 47351, 11848], 'labels': [-1, -1, 3, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.4386892318725586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.7917308807373047})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7877798080444336})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.07138729095459})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6888, 'crossentropy': 2.128912890625}
store['active_learning_steps'][2]['acquisition']={'indices': [26078, 17026, 17745, 2855, 30548], 'labels': [-1, 3, -1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2512083053588867})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.6259729862213135})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.7181873321533203})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.105123281478882})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7029, 'crossentropy': 1.953700390625}
store['active_learning_steps'][3]['acquisition']={'indices': [15653, 53666, 33751, 52259, 17913], 'labels': [9, 7, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.091554880142212})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.282742500305176})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.5771801471710205})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.9267749786376953})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7061, 'crossentropy': 1.88721796875}
store['active_learning_steps'][4]['acquisition']={'indices': [37507, 5891, 12999, 10712, 26674], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.9313610792160034})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.333479881286621})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.7448179721832275})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.6335794925689697})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7153, 'crossentropy': 1.737099609375}
store['active_learning_steps'][5]['acquisition']={'indices': [56841, 29523, 12085, 30419, 15085], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.2026917934417725})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.5538809299468994})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.845360279083252})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9126996994018555})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6987, 'crossentropy': 1.981997265625}
store['active_learning_steps'][6]['acquisition']={'indices': [24369, 58124, 46606, 8556, 32031], 'labels': [-1, -1, 2, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9873563051223755})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.347963809967041})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.3627114295959473})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.5031824111938477})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7105, 'crossentropy': 1.88761484375}
store['active_learning_steps'][7]['acquisition']={'indices': [24281, 55596, 34340, 34316, 32490], 'labels': [3, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.9914880990982056})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.2136309146881104})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.559169292449951})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.4997353553771973})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7025, 'crossentropy': 1.8502490234375}
store['active_learning_steps'][8]['acquisition']={'indices': [7223, 44878, 46233, 23328, 45716], 'labels': [-1, 9, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.1370959281921387})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.424950361251831})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.5276498794555664})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.1038804054260254})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6904, 'crossentropy': 1.981051171875}
store['active_learning_steps'][9]['acquisition']={'indices': [17345, 17147, 8019, 30476, 40721], 'labels': [-1, 9, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.1350808143615723})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.6797351837158203})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7031350135803223})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.223586320877075})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6969, 'crossentropy': 2.082703515625}
store['active_learning_steps'][10]['acquisition']={'indices': [47441, 32819, 50418, 20822, 48597], 'labels': [3, 7, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.080695390701294})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.580261707305908})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8331329822540283})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.9222843647003174})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7106, 'crossentropy': 1.9375673828125}
store['active_learning_steps'][11]['acquisition']={'indices': [54703, 48065, 12872, 19745, 27728], 'labels': [0, 3, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8656554222106934})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.525419235229492})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.747725486755371})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.075484037399292})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7105, 'crossentropy': 1.83904453125}
store['active_learning_steps'][12]['acquisition']={'indices': [45647, 37001, 8460, 30880, 41841], 'labels': [-1, 7, 2, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.8845937252044678})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6846628189086914})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.5971434116363525})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.7370195388793945})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.707, 'crossentropy': 1.6881736328125}
store['active_learning_steps'][13]['acquisition']={'indices': [28573, 3985, 43957, 20589, 58205], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.8718485832214355})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.296353578567505})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.834077835083008})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.2573792934417725})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7106, 'crossentropy': 1.730486328125}
store['active_learning_steps'][14]['acquisition']={'indices': [2954, 41067, 14792, 37858, 27195], 'labels': [6, 3, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0011398792266846})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.1816039085388184})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5843729972839355})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.5264225006103516})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7065, 'crossentropy': 1.787283984375}
store['active_learning_steps'][15]['acquisition']={'indices': [3688, 38369, 43191, 45951, 53929], 'labels': [8, 9, 2, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.8826658725738525})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.4431800842285156})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.456902027130127})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.8355002403259277})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7127, 'crossentropy': 1.91289375}
store['active_learning_steps'][16]['acquisition']={'indices': [57550, 38751, 47677, 50493, 53190], 'labels': [7, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.572495698928833})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.2097952365875244})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.5138092041015625})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.5369198322296143})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7311, 'crossentropy': 1.61154462890625}
store['active_learning_steps'][17]['acquisition']={'indices': [11549, 28526, 37089, 47212, 14939], 'labels': [-1, -1, 5, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.6871466636657715})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.0067601203918457})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.2279293537139893})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.51348876953125})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7415, 'crossentropy': 1.548727734375}
store['active_learning_steps'][18]['acquisition']={'indices': [32521, 22019, 58476, 4606, 10400], 'labels': [-1, 2, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.8115746974945068})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.028140068054199})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.3893895149230957})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.3501968383789062})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7407, 'crossentropy': 1.5025583984375}
store['active_learning_steps'][19]['acquisition']={'indices': [4443, 56960, 57192, 52349, 41856], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.6370190382003784})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.0283515453338623})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.1479949951171875})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.110215425491333})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.734, 'crossentropy': 1.61516904296875}
store['active_learning_steps'][20]['acquisition']={'indices': [36840, 17893, 49902, 44891, 26334], 'labels': [7, 3, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6710617542266846})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.8640873432159424})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.423624038696289})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.3374667167663574})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7361, 'crossentropy': 1.5887291015625}
store['active_learning_steps'][21]['acquisition']={'indices': [8255, 25992, 17377, 37536, 23348], 'labels': [1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.5398874282836914})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.8809435367584229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.6882109642028809})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.9211475849151611})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7639, 'crossentropy': 1.4827333984375}
store['active_learning_steps'][22]['acquisition']={'indices': [56305, 25140, 1966, 42209, 45815], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3763787746429443})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.8306410312652588})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.7136218547821045})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 2.128012180328369})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7837, 'crossentropy': 1.27946572265625}
store['active_learning_steps'][23]['acquisition']={'indices': [21879, 28743, 23868, 5236, 17872], 'labels': [9, 1, 9, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.5976369380950928})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.7254300117492676})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.2221720218658447})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.468158721923828})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7592, 'crossentropy': 1.4124931640625}
store['active_learning_steps'][24]['acquisition']={'indices': [59085, 36305, 38409, 28449, 43725], 'labels': [1, 6, 2, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.4295270442962646})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.7111365795135498})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.9601942300796509})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 2.062232494354248})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.773, 'crossentropy': 1.323717578125}
store['active_learning_steps'][25]['acquisition']={'indices': [17697, 25779, 4226, 9348, 53272], 'labels': [2, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.386032223701477})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.7706151008605957})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.266421318054199})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 2.3989486694335938})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7714, 'crossentropy': 1.2899595703125}
store['active_learning_steps'][26]['acquisition']={'indices': [44584, 6436, 6293, 11285, 51954], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.658332109451294})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.718989610671997})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.2575125694274902})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.42470121383667})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7498, 'crossentropy': 1.46460693359375}
store['active_learning_steps'][27]['acquisition']={'indices': [35467, 56247, 12516, 59782, 55657], 'labels': [-1, 4, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3315670490264893})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3556737899780273})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.5446968078613281})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.8449599742889404})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7722, 'crossentropy': 1.1668603515625}
store['active_learning_steps'][28]['acquisition']={'indices': [5112, 40912, 40136, 39139, 6315], 'labels': [-1, -1, 9, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.1735588312149048})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2666728496551514})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.5084707736968994})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.569267749786377})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7917, 'crossentropy': 1.018641015625}
store['active_learning_steps'][29]['acquisition']={'indices': [2957, 23483, 17444, 38824, 26770], 'labels': [1, -1, 4, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0363391637802124})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3755772113800049})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1938761472702026})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4048230648040771})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8169, 'crossentropy': 0.95096259765625}
store['active_learning_steps'][30]['acquisition']={'indices': [59584, 48052, 53455, 5271, 27263], 'labels': [5, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1166250705718994})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2463173866271973})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.421825647354126})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.5998563766479492})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7921, 'crossentropy': 0.99535234375}
store['active_learning_steps'][31]['acquisition']={'indices': [34011, 50375, 42770, 32269, 9408], 'labels': [-1, -1, 4, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9820918440818787})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1707563400268555})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3833138942718506})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3839690685272217})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8266, 'crossentropy': 0.851610546875}
store['active_learning_steps'][32]['acquisition']={'indices': [2286, 53930, 46543, 5585, 49127], 'labels': [3, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9445145130157471})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.08980393409729})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2170321941375732})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2011802196502686})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.828, 'crossentropy': 0.87879951171875}
store['active_learning_steps'][33]['acquisition']={'indices': [26930, 17118, 50433, 14165, 6239], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.944959282875061})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9898346662521362})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.079797387123108})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1411240100860596})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8176, 'crossentropy': 0.87529013671875}
store['active_learning_steps'][34]['acquisition']={'indices': [28271, 36823, 19457, 16829, 31106], 'labels': [-1, -1, -1, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9061685800552368})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9437388181686401})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1426243782043457})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2922840118408203})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8473, 'crossentropy': 0.81865986328125}
store['active_learning_steps'][35]['acquisition']={'indices': [13516, 46455, 36129, 42401, 56343], 'labels': [3, 6, -1, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9892696738243103})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1261237859725952})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2225455045700073})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.411651849746704})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8148, 'crossentropy': 0.9057978515625}
store['active_learning_steps'][36]['acquisition']={'indices': [39999, 25157, 43760, 12389, 4346], 'labels': [5, 2, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9880176186561584})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0686254501342773})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3071675300598145})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3843965530395508})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8221, 'crossentropy': 0.878959375}
store['active_learning_steps'][37]['acquisition']={'indices': [22715, 16459, 13037, 26917, 14416], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9066973328590393})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.010121464729309})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.211565375328064})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1855223178863525})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8167, 'crossentropy': 0.84056357421875}
store['active_learning_steps'][38]['acquisition']={'indices': [8224, 30473, 4109, 21205, 1839], 'labels': [6, 0, 1, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9581568241119385})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2343755960464478})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3212604522705078})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.3690896034240723})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8298, 'crossentropy': 0.806521142578125}
store['active_learning_steps'][39]['acquisition']={'indices': [4179, 15390, 51815, 37642, 9999], 'labels': [3, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0556083917617798})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1936531066894531})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1122524738311768})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2692168951034546})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8303, 'crossentropy': 0.86149814453125}
store['active_learning_steps'][40]['acquisition']={'indices': [16391, 38207, 59286, 21473, 47052], 'labels': [-1, -1, -1, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.045395016670227})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.227617621421814})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1843173503875732})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1947367191314697})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8188, 'crossentropy': 0.90876533203125}
store['active_learning_steps'][41]['acquisition']={'indices': [36808, 4903, 58373, 20830, 49138], 'labels': [9, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9579324722290039})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9963010549545288})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1063315868377686})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1295971870422363})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8314, 'crossentropy': 0.8508376953125}
store['active_learning_steps'][42]['acquisition']={'indices': [19426, 29841, 48438, 5652, 11167], 'labels': [6, 9, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.948900580406189})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0265402793884277})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.040524959564209})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9970588088035583})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8271, 'crossentropy': 0.81548984375}
store['active_learning_steps'][43]['acquisition']={'indices': [3110, 39741, 4072, 52360, 31441], 'labels': [4, 3, 6, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9457552433013916})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9665796160697937})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9911457896232605})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1054567098617554})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8379, 'crossentropy': 0.801206689453125}
store['active_learning_steps'][44]['acquisition']={'indices': [47758, 32774, 59954, 23069, 25983], 'labels': [-1, 8, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.913672924041748})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9665691256523132})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9639356732368469})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9138725399971008})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8211, 'crossentropy': 0.840415625}
store['active_learning_steps'][45]['acquisition']={'indices': [43564, 57307, 43439, 25174, 20800], 'labels': [-1, 2, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8277071714401245})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8599202632904053})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9988785982131958})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9546789526939392})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8526, 'crossentropy': 0.746683056640625}
store['active_learning_steps'][46]['acquisition']={'indices': [53625, 13547, 19170, 43862, 10343], 'labels': [6, -1, 5, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8675609827041626})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9322326183319092})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9286011457443237})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0573337078094482})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8412, 'crossentropy': 0.76110390625}
store['active_learning_steps'][47]['acquisition']={'indices': [12450, 48442, 59862, 41357, 33413], 'labels': [6, 4, 4, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8459569811820984})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8402887582778931})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9533486366271973})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9540568590164185})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0028890371322632})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8836, 'crossentropy': 0.732349853515625}
store['active_learning_steps'][48]['acquisition']={'indices': [56664, 2090, 52187, 54863, 39568], 'labels': [-1, -1, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7933559417724609})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8360955715179443})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9435247182846069})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.932369589805603})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8675, 'crossentropy': 0.696890380859375}
store['active_learning_steps'][49]['acquisition']={'indices': [43127, 34968, 5913, 42732, 22190], 'labels': [5, -1, -1, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8049188852310181})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8617053031921387})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9240952730178833})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9032431840896606})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8554, 'crossentropy': 0.747295703125}
store['active_learning_steps'][50]['acquisition']={'indices': [23228, 39134, 48582, 15829, 21391], 'labels': [-1, 9, 4, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7971978783607483})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.781954288482666})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8131588101387024})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9254294633865356})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8450196385383606})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8911, 'crossentropy': 0.659314501953125}
store['active_learning_steps'][51]['acquisition']={'indices': [47647, 52209, 53196, 26394, 49479], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8931169509887695})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.847987174987793})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9844579696655273})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9317666292190552})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0511837005615234})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8724, 'crossentropy': 0.725829736328125}
store['active_learning_steps'][52]['acquisition']={'indices': [36607, 12440, 8416, 18655, 49653], 'labels': [9, -1, 9, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8989869356155396})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9100664258003235})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8527241945266724})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9501310586929321})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0547759532928467})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9997900724411011})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8746, 'crossentropy': 0.7992923828125}
store['active_learning_steps'][53]['acquisition']={'indices': [45920, 504, 16479, 49072, 41844], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9418498277664185})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9120430946350098})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.958250880241394})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9802151918411255})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0493392944335938})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8762, 'crossentropy': 0.7740443359375}
store['active_learning_steps'][54]['acquisition']={'indices': [23091, 58534, 9699, 58037, 21366], 'labels': [8, 6, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8296593427658081})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7681850790977478})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8334058523178101})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8559621572494507})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.969876766204834})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8745, 'crossentropy': 0.709226806640625}
store['active_learning_steps'][55]['acquisition']={'indices': [53463, 50427, 40567, 13732, 1075], 'labels': [-1, -1, 5, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8626782894134521})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8966549634933472})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8587183952331543})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9353931546211243})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.000540852546692})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.075721025466919})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.73705068359375}
store['active_learning_steps'][56]['acquisition']={'indices': [2033, 47251, 9729, 53874, 5451], 'labels': [-1, 5, 9, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7926490306854248})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7643349170684814})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8530590534210205})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0008258819580078})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9124346971511841})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8781, 'crossentropy': 0.68456630859375}
store['active_learning_steps'][57]['acquisition']={'indices': [59411, 55132, 37473, 37599, 27890], 'labels': [5, -1, 8, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8535449504852295})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8314836025238037})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7978365421295166})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.928361177444458})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8339154720306396})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9312995672225952})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8929, 'crossentropy': 0.67904912109375}
store['active_learning_steps'][58]['acquisition']={'indices': [55010, 59305, 14361, 20316, 38540], 'labels': [-1, 5, -1, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7689662575721741})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8762613534927368})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8777170777320862})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8774194717407227})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8679, 'crossentropy': 0.708135888671875}
store['active_learning_steps'][59]['acquisition']={'indices': [4817, 55213, 40003, 54768, 37919], 'labels': [6, 6, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8253848552703857})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7594465017318726})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8438526391983032})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8646830320358276})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8522881269454956})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.887, 'crossentropy': 0.648032763671875}
store['active_learning_steps'][60]['acquisition']={'indices': [39272, 30172, 22740, 42201, 46806], 'labels': [-1, -1, 7, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8080781102180481})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7932564616203308})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8271377086639404})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8694531917572021})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.96306312084198})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8835, 'crossentropy': 0.687382177734375}
store['active_learning_steps'][61]['acquisition']={'indices': [7063, 935, 34369, 8869, 48038], 'labels': [6, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7975820302963257})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8951186537742615})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7640284299850464})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9911590814590454})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9744242429733276})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1267893314361572})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.889, 'crossentropy': 0.6805904296875}
store['active_learning_steps'][62]['acquisition']={'indices': [44594, 53401, 9032, 42701, 18740], 'labels': [-1, -1, 0, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7319025993347168})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7382950186729431})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8303083181381226})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.851186990737915})
store['active_learning_steps'][63]['training']['best_epoch']=1
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8538, 'crossentropy': 0.7304248046875}
store['active_learning_steps'][63]['acquisition']={'indices': [16584, 11874, 12974, 3900, 31470], 'labels': [-1, -1, 8, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7289748191833496})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8196970224380493})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7619837522506714})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8030562996864319})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.6769748046875}
store['active_learning_steps'][64]['acquisition']={'indices': [7197, 31804, 5861, 49609, 24894], 'labels': [7, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7967504262924194})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6998653411865234})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7369785308837891})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8907896280288696})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0067826509475708})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.61896044921875}
store['active_learning_steps'][65]['acquisition']={'indices': [14004, 36970, 15953, 14749, 26492], 'labels': [7, -1, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8070901036262512})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7813786864280701})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8218449354171753})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8911491632461548})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8659940958023071})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8828, 'crossentropy': 0.699483203125}
store['active_learning_steps'][66]['acquisition']={'indices': [7571, 3358, 27507, 21829, 43405], 'labels': [-1, 3, 7, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7930170893669128})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.776016891002655})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.831275463104248})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.82615065574646})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9690968990325928})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8811, 'crossentropy': 0.69215517578125}
store['active_learning_steps'][67]['acquisition']={'indices': [11592, 13306, 23502, 11631, 14524], 'labels': [6, -1, 9, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.805666446685791})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7765862345695496})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8810333013534546})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8114290237426758})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.821897566318512})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8913, 'crossentropy': 0.670035546875}
store['active_learning_steps'][68]['acquisition']={'indices': [22209, 53088, 41213, 55498, 22434], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7263485193252563})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7438258528709412})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7686108350753784})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.851303219795227})
store['active_learning_steps'][69]['training']['best_epoch']=1
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8757, 'crossentropy': 0.69347314453125}
store['active_learning_steps'][69]['acquisition']={'indices': [31153, 36180, 11186, 36918, 20551], 'labels': [3, 3, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7642970085144043})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6956840753555298})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7253959774971008})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.822901725769043})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9360234141349792})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.609722509765625}
store['active_learning_steps'][70]['acquisition']={'indices': [20293, 27636, 857, 8313, 39532], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7552372217178345})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7846009135246277})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7930614948272705})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8814876079559326})
store['active_learning_steps'][71]['training']['best_epoch']=1
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8627, 'crossentropy': 0.709551123046875}
store['active_learning_steps'][71]['acquisition']={'indices': [28035, 20314, 36505, 10972, 56444], 'labels': [1, -1, 2, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7917430400848389})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6964742541313171})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8242325782775879})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8816441297531128})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8788409233093262})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8939, 'crossentropy': 0.613956298828125}
store['active_learning_steps'][72]['acquisition']={'indices': [56178, 44629, 45613, 48146, 39342], 'labels': [-1, 0, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7631965279579163})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7963364124298096})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8186032772064209})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9056813716888428})
store['active_learning_steps'][73]['training']['best_epoch']=1
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8629, 'crossentropy': 0.726402392578125}
store['active_learning_steps'][73]['acquisition']={'indices': [21765, 50813, 31143, 55802, 21677], 'labels': [-1, -1, 6, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8263279795646667})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.720301628112793})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7606140375137329})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.860203742980957})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8689603805541992})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8877, 'crossentropy': 0.667599560546875}
store['active_learning_steps'][74]['acquisition']={'indices': [1599, 50060, 53674, 19492, 16116], 'labels': [3, 5, 4, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7598937749862671})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7281502485275269})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8525681495666504})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8983092308044434})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9202669858932495})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8869, 'crossentropy': 0.660207080078125}
store['active_learning_steps'][75]['acquisition']={'indices': [24789, 58260, 31565, 41860, 6573], 'labels': [3, -1, 9, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7436858415603638})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8221094608306885})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8424782752990723})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7741042375564575})
store['active_learning_steps'][76]['training']['best_epoch']=1
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8678, 'crossentropy': 0.71431494140625}
store['active_learning_steps'][76]['acquisition']={'indices': [53759, 31465, 25752, 19099, 27175], 'labels': [5, 1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7943005561828613})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7027746438980103})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8452401757240295})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7382979393005371})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7809929847717285})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8997, 'crossentropy': 0.62977392578125}
store['active_learning_steps'][77]['acquisition']={'indices': [44192, 22676, 33016, 35750, 55667], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.720564067363739})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7353227734565735})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8406974077224731})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7978850603103638})
store['active_learning_steps'][78]['training']['best_epoch']=1
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8768, 'crossentropy': 0.6763251953125}
store['active_learning_steps'][78]['acquisition']={'indices': [56012, 22731, 13662, 216, 33914], 'labels': [3, 2, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8207442164421082})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7833133935928345})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9276794195175171})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9029781818389893})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8715623617172241})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8843, 'crossentropy': 0.700258935546875}
store['active_learning_steps'][79]['acquisition']={'indices': [47893, 8856, 39126, 14675, 43966], 'labels': [7, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7840769290924072})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7126397490501404})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7385758757591248})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8047834634780884})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7736274003982544})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.63153037109375}
store['active_learning_steps'][80]['acquisition']={'indices': [42412, 25226, 35542, 36459, 7653], 'labels': [-1, -1, 3, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7325021028518677})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7341629266738892})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7182523012161255})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8076374530792236})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7916141748428345})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7785145044326782})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9021, 'crossentropy': 0.6505126953125}
store['active_learning_steps'][81]['acquisition']={'indices': [54982, 41444, 43291, 43874, 31545], 'labels': [-1, 4, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7862609624862671})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7234179973602295})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7981202602386475})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.737313449382782})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8570756912231445})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.667079931640625}
store['active_learning_steps'][82]['acquisition']={'indices': [50549, 2236, 6886, 43440, 25588], 'labels': [-1, 4, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6782276630401611})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6976872086524963})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.811721682548523})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7951211929321289})
store['active_learning_steps'][83]['training']['best_epoch']=1
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8753, 'crossentropy': 0.672321240234375}
store['active_learning_steps'][83]['acquisition']={'indices': [12305, 31926, 21456, 14460, 34025], 'labels': [-1, 5, 7, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6426552534103394})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6677407026290894})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7481416463851929})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7366985082626343})
store['active_learning_steps'][84]['training']['best_epoch']=1
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.879, 'crossentropy': 0.6275025390625}
store['active_learning_steps'][84]['acquisition']={'indices': [6266, 35389, 51075, 719, 36275], 'labels': [6, -1, 6, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7425651550292969})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.716943621635437})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6640326976776123})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6897015571594238})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7551948428153992})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8134990930557251})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9025, 'crossentropy': 0.587291015625}
store['active_learning_steps'][85]['acquisition']={'indices': [34962, 15755, 41314, 48898, 4945], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7227120399475098})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7110124230384827})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6986111402511597})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7573567628860474})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7421796321868896})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7621698975563049})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.6144130859375}
store['active_learning_steps'][86]['acquisition']={'indices': [13620, 57428, 10447, 34860, 57281], 'labels': [8, -1, 8, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7341018915176392})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7203464508056641})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7275873422622681})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7460048794746399})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7275776863098145})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.6116771484375}
store['active_learning_steps'][87]['acquisition']={'indices': [38532, 16748, 36433, 35080, 30037], 'labels': [1, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6242090463638306})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5962655544281006})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6383522748947144})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.654596209526062})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6633402109146118})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.5321181640625}
store['active_learning_steps'][88]['acquisition']={'indices': [37954, 3172, 43475, 41105, 48342], 'labels': [0, 6, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7072135210037231})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6386822462081909})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6367163062095642})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7458155155181885})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6831929683685303})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6727492213249207})
store['active_learning_steps'][89]['training']['best_epoch']=3
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.55190078125}
store['active_learning_steps'][89]['acquisition']={'indices': [13077, 1399, 7530, 49481, 2127], 'labels': [-1, 9, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7012141942977905})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6809152960777283})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7061910629272461})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7221851944923401})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.739173412322998})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9015, 'crossentropy': 0.568804052734375}
store['active_learning_steps'][90]['acquisition']={'indices': [35169, 38856, 55021, 17445, 40069], 'labels': [-1, -1, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6830543279647827})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6534876823425293})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6452091336250305})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7335276007652283})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6982594728469849})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7971149682998657})
store['active_learning_steps'][91]['training']['best_epoch']=3
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.5603447265625}
store['active_learning_steps'][91]['acquisition']={'indices': [18256, 45772, 8122, 9251, 3986], 'labels': [1, -1, 3, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7558325529098511})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7880198955535889})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6948778033256531})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6882830262184143})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.721487283706665})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7133331298828125})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7683098316192627})
store['active_learning_steps'][92]['training']['best_epoch']=4
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.556015576171875}
store['active_learning_steps'][92]['acquisition']={'indices': [26821, 22921, 39035, 23393, 21844], 'labels': [2, 7, -1, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7058278322219849})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7281869053840637})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6416290402412415})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6718847751617432})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7232153415679932})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7086151838302612})
store['active_learning_steps'][93]['training']['best_epoch']=3
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.5061912109375}
store['active_learning_steps'][93]['acquisition']={'indices': [24941, 9590, 4413, 58610, 58235], 'labels': [-1, 1, 5, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7816489338874817})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6681468486785889})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7182966470718384})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.708184003829956})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7268494367599487})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.560995751953125}
store['active_learning_steps'][94]['acquisition']={'indices': [34536, 15523, 25277, 5862, 1159], 'labels': [3, -1, 9, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7196456789970398})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6493109464645386})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6302005052566528})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6559334993362427})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6899198293685913})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6491248607635498})
store['active_learning_steps'][95]['training']['best_epoch']=3
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.54340498046875}
store['active_learning_steps'][95]['acquisition']={'indices': [37514, 7687, 24962, 19429, 1352], 'labels': [2, 0, 0, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7437493801116943})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6667346954345703})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6148592829704285})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7162512540817261})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.702307939529419})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6976830959320068})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.532931201171875}
store['active_learning_steps'][96]['acquisition']={'indices': [23703, 18592, 52695, 4293, 45201], 'labels': [-1, -1, 2, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7112740278244019})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6446524858474731})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6211692094802856})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.726762592792511})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7758158445358276})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7720614671707153})
store['active_learning_steps'][97]['training']['best_epoch']=3
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.536306787109375}
store['active_learning_steps'][97]['acquisition']={'indices': [17941, 46115, 19869, 1286, 47980], 'labels': [0, 2, -1, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6959772109985352})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.655500054359436})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6753916144371033})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7225184440612793})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7461414337158203})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.8995, 'crossentropy': 0.54839287109375}
store['active_learning_steps'][98]['acquisition']={'indices': [25899, 36508, 57267, 57326, 33938], 'labels': [1, 5, 9, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6662417650222778})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5815847516059875})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.584182858467102})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6280279159545898})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6222903728485107})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.5230111328125}
store['active_learning_steps'][99]['acquisition']={'indices': [15588, 43579, 29909, 51192, 45639], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6864163875579834})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6266335248947144})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6536430716514587})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5901786088943481})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6196755766868591})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6840898990631104})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.722030758857727})
store['active_learning_steps'][100]['training']['best_epoch']=4
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9184, 'crossentropy': 0.528694970703125}
store['active_learning_steps'][100]['acquisition']={'indices': [5717, 58449, 43267, 25615, 40631], 'labels': [3, 3, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7244833707809448})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.614122211933136})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6470799446105957})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5882903337478638})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6239670515060425})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7351874113082886})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6516979336738586})
store['active_learning_steps'][101]['training']['best_epoch']=4
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.513433984375}
store['active_learning_steps'][101]['acquisition']={'indices': [13390, 57534, 34915, 9765, 24199], 'labels': [-1, 7, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6479015946388245})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6179319620132446})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5916681289672852})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6752482652664185})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6162866950035095})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6985417008399963})
store['active_learning_steps'][102]['training']['best_epoch']=3
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.513117822265625}
store['active_learning_steps'][102]['acquisition']={'indices': [48788, 36746, 53748, 9686, 21485], 'labels': [3, 6, 2, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7071505784988403})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5909844636917114})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6577478647232056})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6567726135253906})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6849257946014404})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.514245751953125}
store['active_learning_steps'][103]['acquisition']={'indices': [8499, 24405, 5134, 560, 40357], 'labels': [-1, -1, 4, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6731760501861572})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5896434187889099})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6211315393447876})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5872969627380371})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6152288913726807})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5990180969238281})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6760945320129395})
store['active_learning_steps'][104]['training']['best_epoch']=4
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.49414833984375}
store['active_learning_steps'][104]['acquisition']={'indices': [28618, 35950, 24503, 51579, 40094], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6702439785003662})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6163716912269592})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6272425651550293})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6431434750556946})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6394935846328735})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.913, 'crossentropy': 0.4957171875}
store['active_learning_steps'][105]['acquisition']={'indices': [48711, 26635, 11587, 59796, 45945], 'labels': [-1, 2, 5, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7413458824157715})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5609462261199951})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5861940979957581})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6203081607818604})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5770114660263062})
store['active_learning_steps'][106]['training']['best_epoch']=2
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.477204833984375}
store['active_learning_steps'][106]['acquisition']={'indices': [40699, 6621, 23137, 51251, 13995], 'labels': [2, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6783214807510376})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.59709632396698})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6075443029403687})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6264218091964722})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6095072031021118})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.50640419921875}
store['active_learning_steps'][107]['acquisition']={'indices': [52808, 43541, 40476, 58102, 41163], 'labels': [8, 7, 7, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6418665647506714})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6257908344268799})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5873919725418091})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6150074005126953})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6416250467300415})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7055798768997192})
store['active_learning_steps'][108]['training']['best_epoch']=3
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.527756298828125}
store['active_learning_steps'][108]['acquisition']={'indices': [39895, 50041, 7121, 38909, 1426], 'labels': [9, 9, 8, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6607014536857605})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5770647525787354})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.627006471157074})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6252237558364868})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6158270835876465})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.512357666015625}
store['active_learning_steps'][109]['acquisition']={'indices': [5840, 8225, 18031, 53197, 21501], 'labels': [1, -1, 4, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7083189487457275})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6602813005447388})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.656447172164917})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7591675519943237})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7059394717216492})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6980054378509521})
store['active_learning_steps'][110]['training']['best_epoch']=3
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.53079892578125}
store['active_learning_steps'][110]['acquisition']={'indices': [26876, 54717, 46103, 867, 7349], 'labels': [-1, 6, 1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7078057527542114})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5601133108139038})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6719710826873779})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6517162322998047})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6925936341285706})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.49832646484375}
store['active_learning_steps'][111]['acquisition']={'indices': [46717, 42984, 20285, 26586, 25246], 'labels': [7, -1, -1, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6708592176437378})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5749803781509399})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6952624320983887})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6823798418045044})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6162375211715698})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9152, 'crossentropy': 0.484667041015625}
store['active_learning_steps'][112]['acquisition']={'indices': [41574, 2091, 44895, 2555, 42238], 'labels': [4, 5, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6455905437469482})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5773109793663025})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6033240556716919})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5840858221054077})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5987238883972168})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.506094677734375}
store['active_learning_steps'][113]['acquisition']={'indices': [41739, 7904, 20990, 53147, 45857], 'labels': [-1, 9, 1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7095274925231934})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5671417713165283})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6082051992416382})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6263539791107178})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.658774197101593})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.506082275390625}
store['active_learning_steps'][114]['acquisition']={'indices': [21094, 53377, 59029, 32205, 37160], 'labels': [1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6977944374084473})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5873162746429443})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5926523804664612})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6335863471031189})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6076392531394958})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.501972216796875}
store['active_learning_steps'][115]['acquisition']={'indices': [14485, 28624, 2731, 23398, 28248], 'labels': [5, 7, 1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7126239538192749})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5665386915206909})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6518151760101318})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5740567445755005})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6544318199157715})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.516444970703125}
store['active_learning_steps'][116]['acquisition']={'indices': [56738, 11056, 38628, 2765, 33672], 'labels': [3, 7, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6260974407196045})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5670493841171265})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5373854637145996})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5657867193222046})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5799305438995361})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6151007413864136})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.50894794921875}
store['active_learning_steps'][117]['acquisition']={'indices': [41893, 16063, 42152, 33197, 44050], 'labels': [8, -1, -1, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6731430292129517})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5833472609519958})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6067789793014526})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.571943998336792})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6153305768966675})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6675596237182617})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6373009085655212})
store['active_learning_steps'][118]['training']['best_epoch']=4
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.49476904296875}
store['active_learning_steps'][118]['acquisition']={'indices': [39526, 35127, 5915, 23599, 51558], 'labels': [-1, -1, -1, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6038376092910767})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5993556380271912})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.55135178565979})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.661260724067688})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6483260989189148})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6004443764686584})
store['active_learning_steps'][119]['training']['best_epoch']=3
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.4886279296875}
store['active_learning_steps'][119]['acquisition']={'indices': [48171, 14877, 7355, 15224, 43666], 'labels': [-1, -1, -1, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6950161457061768})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5928176641464233})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6616934537887573})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6493973135948181})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.578368067741394})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.629572868347168})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6684360504150391})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6749399304389954})
store['active_learning_steps'][120]['training']['best_epoch']=5
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.47790712890625}
store['active_learning_steps'][120]['acquisition']={'indices': [10007, 34140, 38645, 40133, 54378], 'labels': [-1, 3, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7071883678436279})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5795718431472778})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6087996363639832})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5674360990524292})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5861012935638428})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.630427360534668})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5838072299957275})
store['active_learning_steps'][121]['training']['best_epoch']=4
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.510123828125}
store['active_learning_steps'][121]['acquisition']={'indices': [8891, 6190, 25797, 4151, 50459], 'labels': [1, 2, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6869752407073975})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5657994747161865})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5341907143592834})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6009722948074341})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6207523345947266})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5980397462844849})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.50304765625}
store['active_learning_steps'][122]['acquisition']={'indices': [34736, 11913, 54469, 8076, 34540], 'labels': [3, 4, -1, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6635509133338928})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5573295950889587})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5775513052940369})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6320500373840332})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6347235441207886})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.472611572265625}
store['active_learning_steps'][123]['acquisition']={'indices': [53764, 32279, 43651, 56930, 31440], 'labels': [-1, -1, 5, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6515558958053589})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5922538638114929})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5349348187446594})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5682957172393799})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6096029281616211})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6301666498184204})
store['active_learning_steps'][124]['training']['best_epoch']=3
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.484764111328125}
store['active_learning_steps'][124]['acquisition']={'indices': [31413, 29548, 12687, 39209, 18242], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6637266874313354})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5899941921234131})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5767815709114075})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5901585817337036})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5841612815856934})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5786706209182739})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.516130126953125}
store['active_learning_steps'][125]['acquisition']={'indices': [12190, 31722, 9418, 24324, 1805], 'labels': [-1, 3, 3, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7064647674560547})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5544267892837524})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5798124670982361})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.514386773109436})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6139003038406372})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5837643146514893})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5729987025260925})
store['active_learning_steps'][126]['training']['best_epoch']=4
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.445861865234375}
store['active_learning_steps'][126]['acquisition']={'indices': [6673, 42383, 59988, 31125, 4465], 'labels': [-1, 8, 7, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7677645683288574})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.565474271774292})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5822407603263855})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5587278604507446})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6101822257041931})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5873935222625732})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5569555163383484})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6444644331932068})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6402140259742737})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6446296572685242})
store['active_learning_steps'][127]['training']['best_epoch']=7
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.447468212890625}
store['active_learning_steps'][127]['acquisition']={'indices': [18036, 21511, 48805, 43513, 55239], 'labels': [2, -1, -1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6959478855133057})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6313438415527344})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.566736102104187})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6146366000175476})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5680936574935913})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5910695791244507})
store['active_learning_steps'][128]['training']['best_epoch']=3
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.4964234375}
store['active_learning_steps'][128]['acquisition']={'indices': [12657, 39356, 16134, 19279, 17089], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7008596658706665})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5706027150154114})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6209182143211365})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5573748350143433})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6085680723190308})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5976724624633789})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6160370111465454})
store['active_learning_steps'][129]['training']['best_epoch']=4
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.463047509765625}
store['active_learning_steps'][129]['acquisition']={'indices': [50102, 39887, 23495, 35363, 52632], 'labels': [-1, 6, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6700197458267212})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5536324977874756})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5834726095199585})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5566757917404175})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6492899656295776})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.495561328125}
store['active_learning_steps'][130]['acquisition']={'indices': [46388, 40527, 36586, 26028, 10289], 'labels': [-1, -1, 0, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6619035005569458})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5489442944526672})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5786207318305969})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6264821290969849})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5624284744262695})
store['active_learning_steps'][131]['training']['best_epoch']=2
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.481790087890625}
store['active_learning_steps'][131]['acquisition']={'indices': [32785, 41497, 54314, 43938, 307], 'labels': [-1, 9, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7056629061698914})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.569556713104248})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5248662829399109})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5773007869720459})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6091617345809937})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6460196375846863})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.44187041015625}
store['active_learning_steps'][132]['acquisition']={'indices': [32981, 17518, 10347, 30606, 18574], 'labels': [2, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7276344299316406})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5476049184799194})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5627977848052979})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5593792200088501})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.627960205078125})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.499402490234375}
store['active_learning_steps'][133]['acquisition']={'indices': [32632, 54221, 17926, 41093, 3339], 'labels': [1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7329473495483398})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5798213481903076})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5987616777420044})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5951179265975952})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.634290337562561})
store['active_learning_steps'][134]['training']['best_epoch']=2
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.512943505859375}
store['active_learning_steps'][134]['acquisition']={'indices': [6865, 45737, 40149, 6685, 58581], 'labels': [4, 8, 8, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.659081220626831})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6047126650810242})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5090628862380981})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5536377429962158})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6731257438659668})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6129879355430603})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.46825888671875}
store['active_learning_steps'][135]['acquisition']={'indices': [38784, 49627, 8698, 52593, 18368], 'labels': [2, -1, 7, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7012090682983398})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.542849063873291})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5726503133773804})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5363636016845703})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5538910031318665})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5948222875595093})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5596138834953308})
store['active_learning_steps'][136]['training']['best_epoch']=4
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9278, 'crossentropy': 0.46566484375}
store['active_learning_steps'][136]['acquisition']={'indices': [21483, 59480, 16684, 5974, 39319], 'labels': [7, -1, 6, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6672482490539551})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5170950889587402})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5131603479385376})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5489538311958313})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5668567419052124})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6200450658798218})
store['active_learning_steps'][137]['training']['best_epoch']=3
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.458924609375}
store['active_learning_steps'][137]['acquisition']={'indices': [52309, 13071, 637, 17379, 13766], 'labels': [-1, -1, -1, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6619470119476318})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5970462560653687})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5919086933135986})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6317514181137085})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6372261047363281})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6230452656745911})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.478487548828125}
store['active_learning_steps'][138]['acquisition']={'indices': [37169, 49607, 28201, 41960, 42855], 'labels': [-1, -1, 7, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7591034770011902})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5700783729553223})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5747690200805664})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5515117645263672})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5699549913406372})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5980143547058105})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6094527244567871})
store['active_learning_steps'][139]['training']['best_epoch']=4
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.444580419921875}
store['active_learning_steps'][139]['acquisition']={'indices': [38528, 15750, 31120, 34441, 46198], 'labels': [1, 7, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6718897819519043})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5578713417053223})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5277950167655945})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.518519937992096})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6096495389938354})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5823326110839844})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5659630298614502})
store['active_learning_steps'][140]['training']['best_epoch']=4
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.463620703125}
store['active_learning_steps'][140]['acquisition']={'indices': [55751, 54880, 30046, 59814, 45317], 'labels': [-1, 5, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6561787128448486})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5691529512405396})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5806708931922913})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5525591373443604})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6275733709335327})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6181937456130981})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6065074801445007})
store['active_learning_steps'][141]['training']['best_epoch']=4
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.47117138671875}
store['active_learning_steps'][141]['acquisition']={'indices': [27081, 49743, 29370, 27135, 3793], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6924328804016113})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5556403398513794})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5444127321243286})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5739357471466064})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6513783931732178})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5553958415985107})
store['active_learning_steps'][142]['training']['best_epoch']=3
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.467150048828125}
store['active_learning_steps'][142]['acquisition']={'indices': [6632, 7689, 38186, 32744, 6083], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.720786452293396})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5115123391151428})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6106470823287964})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5709913969039917})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.580315351486206})
store['active_learning_steps'][143]['training']['best_epoch']=2
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.4781921875}
store['active_learning_steps'][143]['acquisition']={'indices': [35639, 9812, 36104, 11349, 36345], 'labels': [-1, 3, 9, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6738541126251221})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6240561008453369})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5100966691970825})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5724056959152222})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5750411748886108})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6277650594711304})
store['active_learning_steps'][144]['training']['best_epoch']=3
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.438470654296875}
store['active_learning_steps'][144]['acquisition']={'indices': [42974, 41649, 15109, 21554, 6588], 'labels': [1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7168383598327637})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5597760677337646})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5250694751739502})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5619217157363892})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.560772180557251})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5393408536911011})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.46030576171875}
store['active_learning_steps'][145]['acquisition']={'indices': [41842, 46527, 30748, 41322, 12233], 'labels': [6, -1, 0, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7090616822242737})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5087069869041443})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5365952253341675})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5535403490066528})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5602545738220215})
store['active_learning_steps'][146]['training']['best_epoch']=2
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.92, 'crossentropy': 0.460830615234375}
store['active_learning_steps'][146]['acquisition']={'indices': [7327, 21744, 22935, 23783, 2884], 'labels': [-1, 1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7276092171669006})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6082985401153564})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6909394860267639})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6315702199935913})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6406958103179932})
store['active_learning_steps'][147]['training']['best_epoch']=2
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.51959462890625}
store['active_learning_steps'][147]['acquisition']={'indices': [10870, 12094, 9428, 25184, 11988], 'labels': [-1, -1, 9, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6152610182762146})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5445694923400879})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4939882755279541})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5568358898162842})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5237333178520203})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5083509683609009})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.418909375}
store['active_learning_steps'][148]['acquisition']={'indices': [38235, 28202, 43984, 54657, 15178], 'labels': [-1, -1, 1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7929240465164185})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5967363715171814})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.565009593963623})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5841928720474243})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5876572132110596})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6045206785202026})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.46764853515625}
store['active_learning_steps'][149]['acquisition']={'indices': [44823, 22326, 55193, 8325, 22193], 'labels': [2, 7, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6670509576797485})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5473421216011047})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.543056070804596})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5890233516693115})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6054675579071045})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5943616628646851})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.45881591796875}
store['active_learning_steps'][150]['acquisition']={'indices': [8089, 8862, 18933, 1481, 29823], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7177661657333374})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5401679277420044})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5718849897384644})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5843586325645447})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5446890592575073})
store['active_learning_steps'][151]['training']['best_epoch']=2
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.473482080078125}
store['active_learning_steps'][151]['acquisition']={'indices': [52143, 3028, 50004, 59432, 8401], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6340807676315308})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5768564939498901})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5604043006896973})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5706034898757935})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5899841785430908})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6244882345199585})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.460030712890625}
store['active_learning_steps'][152]['acquisition']={'indices': [11839, 41169, 40187, 25574, 8045], 'labels': [5, 2, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6788645386695862})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.586769163608551})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4735706150531769})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.579124927520752})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.571322500705719})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5731003880500793})
store['active_learning_steps'][153]['training']['best_epoch']=3
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.42039423828125}
store['active_learning_steps'][153]['acquisition']={'indices': [16798, 27653, 5709, 51486, 54674], 'labels': [8, 6, 6, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7658354043960571})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6297317743301392})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.59083491563797})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5848467350006104})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5679484605789185})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6569199562072754})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6382008194923401})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7069462537765503})
store['active_learning_steps'][154]['training']['best_epoch']=5
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.445501611328125}
store['active_learning_steps'][154]['acquisition']={'indices': [36109, 18183, 9035, 16504, 25327], 'labels': [9, 7, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6698035597801208})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5095348954200745})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5531887412071228})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5557928085327148})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5762465596199036})
store['active_learning_steps'][155]['training']['best_epoch']=2
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.458328173828125}
store['active_learning_steps'][155]['acquisition']={'indices': [55803, 6797, 7200, 9018, 41629], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.62861168384552})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5576053857803345})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5395205020904541})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5813342332839966})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6102718710899353})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.54231858253479})
store['active_learning_steps'][156]['training']['best_epoch']=3
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.47073388671875}
store['active_learning_steps'][156]['acquisition']={'indices': [6409, 21820, 48905, 21195, 54445], 'labels': [-1, 5, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6420702934265137})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5392992496490479})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.49415335059165955})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5457791090011597})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5718778371810913})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5855609774589539})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9205, 'crossentropy': 0.442929638671875}
store['active_learning_steps'][157]['acquisition']={'indices': [31598, 9956, 29875, 23109, 50437], 'labels': [-1, 8, 3, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6668927073478699})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5258784294128418})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5480657815933228})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5323730111122131})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5480318069458008})
store['active_learning_steps'][158]['training']['best_epoch']=2
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.470288330078125}
store['active_learning_steps'][158]['acquisition']={'indices': [42136, 31167, 52451, 57212, 39376], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7698385715484619})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5819717049598694})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5525617599487305})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5888697504997253})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6011183857917786})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6232094764709473})
store['active_learning_steps'][159]['training']['best_epoch']=3
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.449354931640625}
store['active_learning_steps'][159]['acquisition']={'indices': [56411, 32228, 31328, 6636, 41460], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6531649827957153})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5932331085205078})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5486351251602173})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5791075229644775})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6183793544769287})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5832313299179077})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.449324072265625}
store['active_learning_steps'][160]['acquisition']={'indices': [29531, 49244, 48067, 10100, 28854], 'labels': [8, -1, 4, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7044653296470642})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5670322179794312})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5534292459487915})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5892839431762695})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6276408433914185})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.614143967628479})
store['active_learning_steps'][161]['training']['best_epoch']=3
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.461441845703125}
store['active_learning_steps'][161]['acquisition']={'indices': [40407, 20015, 49904, 15682, 28565], 'labels': [6, 8, 9, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7009337544441223})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5579245090484619})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6702284812927246})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6228400468826294})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6078376770019531})
store['active_learning_steps'][162]['training']['best_epoch']=2
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9144, 'crossentropy': 0.500707421875}
store['active_learning_steps'][162]['acquisition']={'indices': [41134, 26101, 24229, 43795, 49405], 'labels': [-1, 6, 2, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6756279468536377})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5746325254440308})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6097849011421204})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5567737817764282})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.601549506187439})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6086257696151733})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6850153207778931})
store['active_learning_steps'][163]['training']['best_epoch']=4
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.457431103515625}
