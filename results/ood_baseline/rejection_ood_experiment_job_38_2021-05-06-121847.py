store = {}
store['timestamp']=1620299927
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=38']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=38
store['worker_id']=38
store['num_workers']=40
store['config']={'seed': 56, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.122427463531494})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.489058256149292})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.77932071685791})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.615347146987915})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7009, 'crossentropy': 1.9213984375}
store['active_learning_steps'][0]['acquisition']={'indices': [970, 5338, 37061, 22082, 35136], 'labels': [-1, 8, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.368159532546997})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.5623836517333984})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.117973804473877})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.008833885192871})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6812, 'crossentropy': 2.1352607421875}
store['active_learning_steps'][1]['acquisition']={'indices': [9503, 33919, 25655, 3806, 536], 'labels': [9, 6, 9, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.2957139015197754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.7683563232421875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.3592476844787598})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.654538631439209})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6988, 'crossentropy': 1.9443912109375}
store['active_learning_steps'][2]['acquisition']={'indices': [50034, 45715, 41327, 4461, 13835], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.1562299728393555})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.4732279777526855})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.0283875465393066})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7646336555480957})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6986, 'crossentropy': 1.95598203125}
store['active_learning_steps'][3]['acquisition']={'indices': [22639, 56290, 35186, 4405, 19605], 'labels': [1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.3183722496032715})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.6408467292785645})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.7244510650634766})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.1395840644836426})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7105, 'crossentropy': 1.9332310546875}
store['active_learning_steps'][4]['acquisition']={'indices': [44773, 3187, 2965, 22256, 16122], 'labels': [5, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1675171852111816})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.5734353065490723})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 3.17234206199646})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.620554208755493})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7085, 'crossentropy': 1.796512109375}
store['active_learning_steps'][5]['acquisition']={'indices': [22742, 35690, 574, 12447, 47091], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.1559722423553467})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.381096601486206})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.53299880027771})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.9191203117370605})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7349, 'crossentropy': 1.737882421875}
store['active_learning_steps'][6]['acquisition']={'indices': [56263, 45979, 52460, 28498, 47217], 'labels': [2, -1, -1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1875267028808594})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.405327081680298})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.578524589538574})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.0179824829101562})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6859, 'crossentropy': 1.9388533203125}
store['active_learning_steps'][7]['acquisition']={'indices': [42810, 34850, 6759, 29140, 1937], 'labels': [-1, 2, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8426344394683838})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.2422375679016113})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.4431657791137695})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.855236530303955})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7285, 'crossentropy': 1.7146626953125}
store['active_learning_steps'][8]['acquisition']={'indices': [55739, 53484, 44610, 29466, 13195], 'labels': [5, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.1330604553222656})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.456510066986084})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.892671823501587})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.9199419021606445})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6877, 'crossentropy': 1.9219708984375}
store['active_learning_steps'][9]['acquisition']={'indices': [55439, 43997, 31423, 11994, 52108], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.9990572929382324})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.399081230163574})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.521820545196533})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.2938003540039062})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7231, 'crossentropy': 1.657272265625}
store['active_learning_steps'][10]['acquisition']={'indices': [21482, 33441, 15661, 47646, 25622], 'labels': [7, 1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.359625816345215})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9294838905334473})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.8502392768859863})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.1892964839935303})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6852, 'crossentropy': 1.979651171875}
store['active_learning_steps'][11]['acquisition']={'indices': [36301, 40413, 237, 23174, 46060], 'labels': [3, -1, 4, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0780580043792725})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.097578525543213})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.572017192840576})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.5398592948913574})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7352, 'crossentropy': 1.6789849609375}
store['active_learning_steps'][12]['acquisition']={'indices': [52177, 58436, 30012, 18121, 58024], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.9362388849258423})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.62747859954834})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.469383478164673})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.6932919025421143})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7128, 'crossentropy': 1.65095703125}
store['active_learning_steps'][13]['acquisition']={'indices': [14887, 40014, 54050, 49629, 44581], 'labels': [5, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.0942628383636475})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.565107822418213})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.848355531692505})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 3.093134641647339})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7206, 'crossentropy': 1.839925390625}
store['active_learning_steps'][14]['acquisition']={'indices': [56764, 7231, 7784, 53881, 19685], 'labels': [1, 8, -1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8049805164337158})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.193223476409912})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.2485127449035645})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.362215995788574})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7485, 'crossentropy': 1.48943330078125}
store['active_learning_steps'][15]['acquisition']={'indices': [3873, 38418, 10216, 50179, 26232], 'labels': [-1, -1, -1, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.847574234008789})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.196646213531494})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.370879888534546})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.5594091415405273})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7515, 'crossentropy': 1.6196177734375}
store['active_learning_steps'][16]['acquisition']={'indices': [22748, 30083, 21740, 37290, 38208], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7875151634216309})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.0539727210998535})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.2834267616271973})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.5378782749176025})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7586, 'crossentropy': 1.4640751953125}
store['active_learning_steps'][17]['acquisition']={'indices': [22379, 6754, 34308, 37133, 29409], 'labels': [5, 3, 2, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.6871280670166016})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.2682065963745117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.3052749633789062})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.0989415645599365})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7772, 'crossentropy': 1.42750361328125}
store['active_learning_steps'][18]['acquisition']={'indices': [46567, 17303, 10504, 10423, 42094], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.7372053861618042})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.7470064163208008})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.165001392364502})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.2744548320770264})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7479, 'crossentropy': 1.50215478515625}
store['active_learning_steps'][19]['acquisition']={'indices': [40157, 9352, 26753, 24450, 532], 'labels': [6, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.6881115436553955})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.9608774185180664})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.290560245513916})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.53414249420166})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7862, 'crossentropy': 1.3464484375}
store['active_learning_steps'][20]['acquisition']={'indices': [11592, 36652, 57460, 31374, 54037], 'labels': [6, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.4310328960418701})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5648348331451416})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.6777379512786865})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.9788379669189453})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7803, 'crossentropy': 1.28672841796875}
store['active_learning_steps'][21]['acquisition']={'indices': [9433, 50392, 2901, 44991, 4820], 'labels': [7, -1, 8, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.3065130710601807})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.3934569358825684})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.6606223583221436})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6563314199447632})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.79, 'crossentropy': 1.12548525390625}
store['active_learning_steps'][22]['acquisition']={'indices': [34811, 42927, 36629, 20469, 23823], 'labels': [-1, 1, -1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.250736951828003})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.4515246152877808})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.56900954246521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.457958698272705})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7965, 'crossentropy': 1.19229150390625}
store['active_learning_steps'][23]['acquisition']={'indices': [22654, 41380, 59686, 14427, 24774], 'labels': [6, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0951740741729736})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4009525775909424})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3414247035980225})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4967857599258423})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8101, 'crossentropy': 1.062501171875}
store['active_learning_steps'][24]['acquisition']={'indices': [13852, 57463, 30460, 59439, 46042], 'labels': [-1, -1, 8, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1732923984527588})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.282975196838379})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3645015954971313})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5729255676269531})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8168, 'crossentropy': 1.0743703125}
store['active_learning_steps'][25]['acquisition']={'indices': [56702, 58600, 53827, 41868, 18964], 'labels': [9, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1881484985351562})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2753148078918457})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2337121963500977})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.4666627645492554})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8023, 'crossentropy': 1.08432236328125}
store['active_learning_steps'][26]['acquisition']={'indices': [25060, 40927, 30126, 43189, 55425], 'labels': [7, -1, 1, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0687847137451172})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2035791873931885})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.199319839477539})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3689357042312622})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8115, 'crossentropy': 1.0201880859375}
store['active_learning_steps'][27]['acquisition']={'indices': [50691, 40614, 15978, 53922, 28803], 'labels': [-1, 2, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0204739570617676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1302714347839355})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3669254779815674})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3823165893554688})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8228, 'crossentropy': 0.9550888671875}
store['active_learning_steps'][28]['acquisition']={'indices': [6472, 12797, 34237, 56988, 50366], 'labels': [5, 2, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.030625820159912})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0870640277862549})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2374191284179688})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3662514686584473})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8144, 'crossentropy': 0.9885111328125}
store['active_learning_steps'][29]['acquisition']={'indices': [36657, 34563, 41020, 50554, 48040], 'labels': [1, 8, 4, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1807136535644531})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2335240840911865})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4104804992675781})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4840930700302124})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.807, 'crossentropy': 1.06812880859375}
store['active_learning_steps'][30]['acquisition']={'indices': [50712, 7445, 42614, 9897, 18051], 'labels': [-1, -1, 0, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0701119899749756})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0699756145477295})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2952237129211426})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2960381507873535})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3428242206573486})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8212, 'crossentropy': 1.10497080078125}
store['active_learning_steps'][31]['acquisition']={'indices': [12155, 17084, 11866, 27557, 57512], 'labels': [-1, 8, 6, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0441274642944336})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2103979587554932})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.317386507987976})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.501572847366333})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8158, 'crossentropy': 0.96818095703125}
store['active_learning_steps'][32]['acquisition']={'indices': [43544, 27897, 12246, 3124, 53469], 'labels': [9, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9275993704795837})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1184093952178955})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.164865255355835})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.4096379280090332})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8339, 'crossentropy': 0.889931640625}
store['active_learning_steps'][33]['acquisition']={'indices': [11076, 50344, 1925, 12829, 35927], 'labels': [-1, 0, 9, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0009864568710327})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2068513631820679})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3090684413909912})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3518459796905518})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8258, 'crossentropy': 0.98493876953125}
store['active_learning_steps'][34]['acquisition']={'indices': [40992, 17612, 48658, 27102, 39221], 'labels': [-1, 9, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9517636895179749})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0455849170684814})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2358603477478027})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1786972284317017})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8348, 'crossentropy': 0.90990537109375}
store['active_learning_steps'][35]['acquisition']={'indices': [10092, 5797, 476, 18887, 15765], 'labels': [-1, 9, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9446096420288086})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.034944772720337})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.115644931793213})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.103233814239502})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8493, 'crossentropy': 0.87543046875}
store['active_learning_steps'][36]['acquisition']={'indices': [6031, 29260, 31532, 22933, 47263], 'labels': [-1, -1, 9, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8644796013832092})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9333300590515137})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9573668241500854})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0049142837524414})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8503, 'crossentropy': 0.818923193359375}
store['active_learning_steps'][37]['acquisition']={'indices': [10079, 25917, 23328, 15860, 50744], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9357168674468994})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0715694427490234})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1237497329711914})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.061159610748291})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8376, 'crossentropy': 0.85980126953125}
store['active_learning_steps'][38]['acquisition']={'indices': [8071, 10819, 6326, 7488, 41304], 'labels': [-1, 9, 0, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9395147562026978})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9795773029327393})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9896478652954102})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1026349067687988})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8475, 'crossentropy': 0.85396669921875}
store['active_learning_steps'][39]['acquisition']={'indices': [45355, 8942, 11476, 45395, 13769], 'labels': [-1, -1, 3, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8438658118247986})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9880051612854004})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0287691354751587})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0045883655548096})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.853, 'crossentropy': 0.790735400390625}
store['active_learning_steps'][40]['acquisition']={'indices': [54397, 32712, 9327, 55609, 16329], 'labels': [3, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9071922302246094})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8941289186477661})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.973461389541626})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1146728992462158})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1232659816741943})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8718, 'crossentropy': 0.8314705078125}
store['active_learning_steps'][41]['acquisition']={'indices': [9141, 11881, 15787, 40245, 46338], 'labels': [-1, 8, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8338919878005981})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8390275239944458})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9129710793495178})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9812782406806946})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8393, 'crossentropy': 0.844529296875}
store['active_learning_steps'][42]['acquisition']={'indices': [53917, 45675, 36340, 50353, 59321], 'labels': [-1, -1, -1, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8723113536834717})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0014209747314453})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0415652990341187})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9737918972969055})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8504, 'crossentropy': 0.87168291015625}
store['active_learning_steps'][43]['acquisition']={'indices': [32000, 56684, 17793, 11166, 27681], 'labels': [8, 9, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.832221508026123})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9180116057395935})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8981204032897949})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9514721632003784})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8626, 'crossentropy': 0.788884228515625}
store['active_learning_steps'][44]['acquisition']={'indices': [45790, 41322, 2553, 24938, 7193], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9263168573379517})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0219372510910034})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.134535312652588})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1507933139801025})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8426, 'crossentropy': 0.88948271484375}
store['active_learning_steps'][45]['acquisition']={'indices': [56924, 24632, 17204, 8641, 37308], 'labels': [-1, 2, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8252081274986267})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9254580140113831})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.983850359916687})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1390743255615234})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8572, 'crossentropy': 0.785514892578125}
store['active_learning_steps'][46]['acquisition']={'indices': [54602, 1291, 58754, 45999, 45954], 'labels': [6, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8924018144607544})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9479214549064636})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9540558457374573})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0405144691467285})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8488, 'crossentropy': 0.87566318359375}
store['active_learning_steps'][47]['acquisition']={'indices': [41619, 41378, 35355, 6821, 33283], 'labels': [3, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8633037805557251})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9672318696975708})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2279047966003418})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.012749433517456})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8555, 'crossentropy': 0.8355177734375}
store['active_learning_steps'][48]['acquisition']={'indices': [17865, 30859, 31980, 14581, 39835], 'labels': [-1, -1, -1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8202304840087891})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9391729831695557})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9580458998680115})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1118899583816528})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8411, 'crossentropy': 0.866311328125}
store['active_learning_steps'][49]['acquisition']={'indices': [22233, 25948, 44387, 7184, 8993], 'labels': [-1, 1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7899483442306519})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8784802556037903})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9964897632598877})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.987027645111084})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8535, 'crossentropy': 0.806410498046875}
store['active_learning_steps'][50]['acquisition']={'indices': [20845, 37768, 1181, 31011, 14808], 'labels': [-1, 8, 1, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8811236619949341})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8444263339042664})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9388753175735474})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9784091114997864})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0418152809143066})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8647, 'crossentropy': 0.861912890625}
store['active_learning_steps'][51]['acquisition']={'indices': [35071, 11533, 37833, 9090, 13303], 'labels': [2, 1, 7, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7775861620903015})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8162057399749756})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8240927457809448})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9733673334121704})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.855, 'crossentropy': 0.744088037109375}
store['active_learning_steps'][52]['acquisition']={'indices': [39902, 429, 7775, 36928, 17316], 'labels': [8, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8614140748977661})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9080535173416138})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9014368057250977})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0089651346206665})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8419, 'crossentropy': 0.8802109375}
store['active_learning_steps'][53]['acquisition']={'indices': [50590, 58995, 54606, 43786, 395], 'labels': [6, 1, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.742132842540741})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7676799297332764})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8380815982818604})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8622702360153198})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8676, 'crossentropy': 0.773642578125}
store['active_learning_steps'][54]['acquisition']={'indices': [25362, 31018, 44533, 41013, 9095], 'labels': [8, -1, -1, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7865250110626221})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8746838569641113})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8621382713317871})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.895595908164978})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8581, 'crossentropy': 0.776486083984375}
store['active_learning_steps'][55]['acquisition']={'indices': [31042, 52906, 56422, 905, 449], 'labels': [3, 1, 4, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8027803301811218})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8680746555328369})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.912830114364624})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9708871245384216})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8575, 'crossentropy': 0.80430107421875}
store['active_learning_steps'][56]['acquisition']={'indices': [56921, 46325, 47851, 35164, 3971], 'labels': [-1, 4, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7852159738540649})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8463659882545471})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9071866869926453})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9403514862060547})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8594, 'crossentropy': 0.7759341796875}
store['active_learning_steps'][57]['acquisition']={'indices': [32258, 54582, 55744, 9344, 23496], 'labels': [5, 4, 7, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8463733196258545})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8483607769012451})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9580825567245483})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9488004446029663})
store['active_learning_steps'][58]['training']['best_epoch']=1
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8528, 'crossentropy': 0.8358734375}
store['active_learning_steps'][58]['acquisition']={'indices': [58991, 35972, 1496, 15391, 499], 'labels': [-1, -1, 1, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7932771444320679})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8590304851531982})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8573604822158813})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8696884512901306})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8558, 'crossentropy': 0.791151953125}
store['active_learning_steps'][59]['acquisition']={'indices': [21706, 57733, 5978, 58756, 6598], 'labels': [-1, -1, 0, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.807873010635376})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9168893098831177})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8213480710983276})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8930166959762573})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8475, 'crossentropy': 0.807439501953125}
store['active_learning_steps'][60]['acquisition']={'indices': [42261, 3438, 45715, 7383, 50242], 'labels': [-1, -1, 7, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8741140365600586})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8671872019767761})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8856786489486694})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.997344970703125})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0930988788604736})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8723, 'crossentropy': 0.818791259765625}
store['active_learning_steps'][61]['acquisition']={'indices': [12553, 39877, 39786, 7090, 32955], 'labels': [-1, -1, -1, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.825562596321106})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7573744654655457})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8939833045005798})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.893548846244812})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0215017795562744})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8823, 'crossentropy': 0.72752578125}
store['active_learning_steps'][62]['acquisition']={'indices': [55984, 48092, 50056, 48776, 31548], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8088657259941101})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7585591673851013})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8061233758926392})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8371164798736572})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8329823613166809})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8908, 'crossentropy': 0.677696630859375}
store['active_learning_steps'][63]['acquisition']={'indices': [33864, 58486, 32654, 25774, 49201], 'labels': [0, 1, 2, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7700284719467163})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8359717726707458})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8412114381790161})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8246034979820251})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.793756103515625}
store['active_learning_steps'][64]['acquisition']={'indices': [47889, 36510, 46817, 16881, 42454], 'labels': [5, 9, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8246109485626221})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7591517567634583})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8064616918563843})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8440312147140503})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9684290885925293})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.882, 'crossentropy': 0.771533837890625}
store['active_learning_steps'][65]['acquisition']={'indices': [20343, 30246, 3778, 58850, 9764], 'labels': [-1, 0, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8190019726753235})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8360728025436401})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8645527362823486})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9009274840354919})
store['active_learning_steps'][66]['training']['best_epoch']=1
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8623, 'crossentropy': 0.784489453125}
store['active_learning_steps'][66]['acquisition']={'indices': [18075, 7136, 11957, 14349, 50841], 'labels': [1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8105213642120361})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7273886203765869})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7571271657943726})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9286841750144958})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9290560483932495})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8909, 'crossentropy': 0.69908857421875}
store['active_learning_steps'][67]['acquisition']={'indices': [2314, 4299, 15985, 44908, 58198], 'labels': [2, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7694041728973389})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7631112337112427})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8706625699996948})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8814274072647095})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.795490026473999})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8877, 'crossentropy': 0.7168177734375}
store['active_learning_steps'][68]['acquisition']={'indices': [22777, 21584, 2278, 24236, 17643], 'labels': [-1, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7264300584793091})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.779770016670227})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8014408946037292})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8445398807525635})
store['active_learning_steps'][69]['training']['best_epoch']=1
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8631, 'crossentropy': 0.708887939453125}
store['active_learning_steps'][69]['acquisition']={'indices': [29974, 54221, 37634, 8841, 54420], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7980140447616577})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7750622034072876})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7631565928459167})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.817504346370697})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9110607504844666})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.87923663854599})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8894, 'crossentropy': 0.77443671875}
store['active_learning_steps'][70]['acquisition']={'indices': [58186, 15755, 58337, 8671, 52178], 'labels': [-1, 9, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7272995710372925})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.769202709197998})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8345950245857239})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9566059708595276})
store['active_learning_steps'][71]['training']['best_epoch']=1
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8701, 'crossentropy': 0.71523896484375}
store['active_learning_steps'][71]['acquisition']={'indices': [52568, 39221, 38704, 41575, 31001], 'labels': [-1, 6, 9, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8138023018836975})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8077399134635925})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7883709073066711})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8813362121582031})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9806671738624573})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.0176299810409546})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8892, 'crossentropy': 0.76815185546875}
store['active_learning_steps'][72]['acquisition']={'indices': [42808, 36107, 51558, 24066, 47392], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8078937530517578})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7702838182449341})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.814418375492096})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8662134408950806})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8156753778457642})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8871, 'crossentropy': 0.733576611328125}
store['active_learning_steps'][73]['acquisition']={'indices': [48482, 25187, 25084, 48385, 43837], 'labels': [3, 3, 5, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8012223243713379})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7687100172042847})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8883085250854492})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9068803787231445})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8761518597602844})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8774, 'crossentropy': 0.764740625}
store['active_learning_steps'][74]['acquisition']={'indices': [10239, 39933, 47158, 2292, 27440], 'labels': [-1, 3, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6968700885772705})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6865546703338623})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.684161901473999})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8410264849662781})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7888388633728027})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8936194181442261})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.65342109375}
store['active_learning_steps'][75]['acquisition']={'indices': [42878, 9143, 59452, 54938, 46634], 'labels': [8, -1, -1, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7497439384460449})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6374711990356445})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6945513486862183})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.774640679359436})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7089828848838806})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.625476953125}
store['active_learning_steps'][76]['acquisition']={'indices': [33870, 13618, 48884, 59837, 30605], 'labels': [7, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8219810724258423})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7900891304016113})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8316670656204224})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8828909993171692})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8866665363311768})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8871, 'crossentropy': 0.699033837890625}
store['active_learning_steps'][77]['acquisition']={'indices': [56404, 10543, 18593, 35450, 58962], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7978177070617676})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6953446865081787})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7584539651870728})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8612140417098999})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7824137806892395})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.683417431640625}
store['active_learning_steps'][78]['acquisition']={'indices': [36346, 48279, 26262, 7881, 47388], 'labels': [4, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7304860353469849})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7335389852523804})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6710778474807739})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7045987844467163})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6688733100891113})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.717804491519928})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7611333727836609})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7349240779876709})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.65226669921875}
store['active_learning_steps'][79]['acquisition']={'indices': [12267, 51721, 29846, 40090, 36306], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7018239498138428})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.657417893409729})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7601808309555054})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6992651224136353})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8575024008750916})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8991, 'crossentropy': 0.64213876953125}
store['active_learning_steps'][80]['acquisition']={'indices': [36266, 29773, 1705, 32684, 3197], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.755582332611084})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7624439001083374})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8111745715141296})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8329179286956787})
store['active_learning_steps'][81]['training']['best_epoch']=1
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8631, 'crossentropy': 0.7729869140625}
store['active_learning_steps'][81]['acquisition']={'indices': [42213, 31223, 54104, 49250, 38376], 'labels': [4, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8127222061157227})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7601230144500732})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8234317302703857})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8366106748580933})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9582895636558533})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8881, 'crossentropy': 0.7309517578125}
store['active_learning_steps'][82]['acquisition']={'indices': [24079, 35831, 6163, 51149, 45740], 'labels': [-1, 1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7555531859397888})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7063897848129272})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6457574367523193})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7294175624847412})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8109856843948364})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7259520888328552})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.619030810546875}
store['active_learning_steps'][83]['acquisition']={'indices': [4142, 13397, 9130, 25315, 7259], 'labels': [-1, 0, 1, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7344696521759033})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7602172493934631})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6468396186828613})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7558330297470093})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8022642731666565})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8555029630661011})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.63782353515625}
store['active_learning_steps'][84]['acquisition']={'indices': [23281, 2216, 5339, 55261, 24113], 'labels': [3, 9, 9, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7337213754653931})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7060744762420654})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6216416358947754})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7216863036155701})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7288980484008789})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7510339021682739})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.602013623046875}
store['active_learning_steps'][85]['acquisition']={'indices': [22502, 6611, 20084, 32705, 52255], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.766422688961029})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6870120167732239})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6685980558395386})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7669849991798401})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7105894088745117})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7228000164031982})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.645190771484375}
store['active_learning_steps'][86]['acquisition']={'indices': [41016, 31020, 39938, 10960, 4388], 'labels': [5, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7968021631240845})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6823599934577942})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8039373159408569})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7037229537963867})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8090610504150391})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8959, 'crossentropy': 0.628207958984375}
store['active_learning_steps'][87]['acquisition']={'indices': [33782, 29915, 14882, 27023, 24370], 'labels': [-1, 5, 4, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.79509037733078})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7085456252098083})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6751881837844849})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6614034175872803})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7654283046722412})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7253890037536621})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7600204944610596})
store['active_learning_steps'][88]['training']['best_epoch']=4
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.66916484375}
store['active_learning_steps'][88]['acquisition']={'indices': [5190, 7572, 3234, 54289, 45352], 'labels': [3, 1, 1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6852970123291016})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6471390724182129})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7526463866233826})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7316855788230896})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7341293692588806})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.627263818359375}
store['active_learning_steps'][89]['acquisition']={'indices': [36059, 17372, 21606, 47842, 14568], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6892396211624146})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6291582584381104})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.688471794128418})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7404077053070068})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.726546049118042})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9006, 'crossentropy': 0.60979501953125}
store['active_learning_steps'][90]['acquisition']={'indices': [39152, 8360, 52050, 53507, 35253], 'labels': [-1, 3, -1, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8216431140899658})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6555802226066589})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7299187779426575})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6995903253555298})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6920455098152161})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.600072509765625}
store['active_learning_steps'][91]['acquisition']={'indices': [28540, 36321, 7457, 52595, 47517], 'labels': [0, 2, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7234588861465454})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7139590382575989})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7461895942687988})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.735889732837677})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7247098684310913})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.70371376953125}
store['active_learning_steps'][92]['acquisition']={'indices': [14040, 55915, 41021, 27289, 49913], 'labels': [2, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7589913606643677})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.600120484828949})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6220331192016602})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6762916445732117})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6703588962554932})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.589603662109375}
store['active_learning_steps'][93]['acquisition']={'indices': [1511, 3684, 23933, 30506, 840], 'labels': [-1, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6624153852462769})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6196316480636597})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7079808712005615})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7126626968383789})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6374440789222717})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9011, 'crossentropy': 0.614980859375}
store['active_learning_steps'][94]['acquisition']={'indices': [52494, 48001, 30083, 32146, 48669], 'labels': [-1, 7, 6, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7128723859786987})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6458510160446167})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6559362411499023})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.677681565284729})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7757987976074219})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.8916, 'crossentropy': 0.642198876953125}
store['active_learning_steps'][95]['acquisition']={'indices': [20189, 31244, 46113, 26703, 50457], 'labels': [7, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.767397403717041})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6610684394836426})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7949565649032593})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7202730774879456})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.843393087387085})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.644575146484375}
store['active_learning_steps'][96]['acquisition']={'indices': [32930, 29128, 35583, 31413, 55658], 'labels': [-1, -1, 4, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7853281497955322})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.742902398109436})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8047027587890625})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7872058153152466})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7750420570373535})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.63755478515625}
store['active_learning_steps'][97]['acquisition']={'indices': [50290, 11431, 40416, 54940, 53824], 'labels': [2, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7656302452087402})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6291812658309937})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7077574729919434})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6659643650054932})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6486750245094299})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9021, 'crossentropy': 0.594448681640625}
store['active_learning_steps'][98]['acquisition']={'indices': [30430, 27588, 20642, 36356, 8922], 'labels': [1, 4, 0, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.690095067024231})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.650328516960144})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6589149236679077})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6861748695373535})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7152942419052124})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9063, 'crossentropy': 0.59670458984375}
store['active_learning_steps'][99]['acquisition']={'indices': [9014, 16232, 33357, 41351, 9697], 'labels': [8, 8, 3, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7341760993003845})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.587013840675354})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6089394092559814})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6580647230148315})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6444914937019348})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.53919130859375}
store['active_learning_steps'][100]['acquisition']={'indices': [51636, 6521, 7193, 32611, 5236], 'labels': [7, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7373650670051575})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6306267380714417})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6414248943328857})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6634719967842102})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.687955915927887})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.606035888671875}
store['active_learning_steps'][101]['acquisition']={'indices': [28471, 18209, 22515, 13150, 26960], 'labels': [-1, 5, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6966509819030762})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6741511821746826})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5784683227539062})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6282819509506226})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6521873474121094})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6337174773216248})
store['active_learning_steps'][102]['training']['best_epoch']=3
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.535062451171875}
store['active_learning_steps'][102]['acquisition']={'indices': [52086, 41132, 12936, 23900, 43469], 'labels': [-1, 8, -1, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7290429472923279})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6649394035339355})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.614313006401062})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6483747959136963})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6826273202896118})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6991167068481445})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.56499462890625}
store['active_learning_steps'][103]['acquisition']={'indices': [44270, 48564, 21275, 5866, 1719], 'labels': [8, 5, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7709482908248901})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.635420560836792})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6090071201324463})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6702485084533691})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6407654285430908})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6908189058303833})
store['active_learning_steps'][104]['training']['best_epoch']=3
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.546518359375}
store['active_learning_steps'][104]['acquisition']={'indices': [40190, 39977, 34183, 10368, 52456], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6893682479858398})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6545556783676147})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6207990646362305})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6248205900192261})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6539573669433594})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7933957576751709})
store['active_learning_steps'][105]['training']['best_epoch']=3
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.53982099609375}
store['active_learning_steps'][105]['acquisition']={'indices': [15198, 8412, 39682, 44746, 7255], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7597295641899109})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.642888069152832})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6726123094558716})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7160780429840088})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6384579539299011})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.744525671005249})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7482700347900391})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6986355185508728})
store['active_learning_steps'][106]['training']['best_epoch']=5
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.604522998046875}
store['active_learning_steps'][106]['acquisition']={'indices': [20012, 6632, 8781, 44891, 12029], 'labels': [0, 3, -1, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6622239351272583})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5400005578994751})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6238980293273926})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5803443193435669})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6146747469902039})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.514476171875}
store['active_learning_steps'][107]['acquisition']={'indices': [33967, 55777, 59977, 43111, 45573], 'labels': [-1, 6, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7017421722412109})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6111711859703064})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6149028539657593})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7043982744216919})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6415375471115112})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.57994873046875}
store['active_learning_steps'][108]['acquisition']={'indices': [58775, 20089, 23852, 20133, 46704], 'labels': [-1, -1, 1, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7027727365493774})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5934008359909058})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6257151365280151})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6687906980514526})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5545705556869507})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6069366335868835})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.61583411693573})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6437941789627075})
store['active_learning_steps'][109]['training']['best_epoch']=5
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9256, 'crossentropy': 0.52003583984375}
store['active_learning_steps'][109]['acquisition']={'indices': [56626, 28334, 13300, 47724, 32412], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7719342708587646})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6657513380050659})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6602096557617188})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6547435522079468})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7382621169090271})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7117215394973755})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7153317928314209})
store['active_learning_steps'][110]['training']['best_epoch']=4
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.570479443359375}
store['active_learning_steps'][110]['acquisition']={'indices': [54878, 8455, 19294, 6785, 31301], 'labels': [-1, -1, -1, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6415475606918335})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5629703998565674})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6364799737930298})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6130939722061157})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6241461038589478})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.511853076171875}
store['active_learning_steps'][111]['acquisition']={'indices': [37062, 55849, 31093, 4471, 39183], 'labels': [9, 9, 1, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7444618940353394})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6291800737380981})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6092538833618164})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6754873991012573})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6057081818580627})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6219799518585205})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6475541591644287})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6077631711959839})
store['active_learning_steps'][112]['training']['best_epoch']=5
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.550320947265625}
store['active_learning_steps'][112]['acquisition']={'indices': [5760, 26159, 1225, 45640, 43145], 'labels': [-1, -1, 7, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7424607872962952})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6292150020599365})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6274946331977844})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6051865220069885})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6636244058609009})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.701549768447876})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.725296139717102})
store['active_learning_steps'][113]['training']['best_epoch']=4
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.555619384765625}
store['active_learning_steps'][113]['acquisition']={'indices': [17566, 45479, 44093, 31582, 21764], 'labels': [2, 6, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6864058375358582})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5510540008544922})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5668673515319824})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5796867609024048})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5793641805648804})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.52710751953125}
store['active_learning_steps'][114]['acquisition']={'indices': [47743, 17, 11615, 26496, 58225], 'labels': [2, -1, 0, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7557395696640015})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6203427314758301})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6304953098297119})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6669949293136597})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6293457746505737})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.554087939453125}
store['active_learning_steps'][115]['acquisition']={'indices': [55815, 42832, 59127, 23856, 35990], 'labels': [9, 8, -1, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6786127686500549})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6865543723106384})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6254590749740601})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6196607947349548})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.641353964805603})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6968601942062378})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.694021463394165})
store['active_learning_steps'][116]['training']['best_epoch']=4
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.580857470703125}
store['active_learning_steps'][116]['acquisition']={'indices': [36793, 47505, 23152, 34947, 13729], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.688023567199707})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6113429665565491})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5700982809066772})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6453741192817688})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.599191427230835})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7507215738296509})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.556639404296875}
store['active_learning_steps'][117]['acquisition']={'indices': [16634, 36966, 4570, 44702, 51142], 'labels': [-1, -1, 3, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6951425671577454})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5653842687606812})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6067942380905151})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5863876342773438})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5813400745391846})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.51128349609375}
store['active_learning_steps'][118]['acquisition']={'indices': [26731, 32869, 13577, 4610, 33866], 'labels': [-1, 0, -1, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7514976859092712})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6054747104644775})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5992832183837891})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6815111041069031})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6850040555000305})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6474563479423523})
store['active_learning_steps'][119]['training']['best_epoch']=3
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.546475732421875}
store['active_learning_steps'][119]['acquisition']={'indices': [35280, 17020, 24880, 56710, 59817], 'labels': [6, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7696058750152588})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6189817190170288})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5745770931243896})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5645922422409058})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6281449794769287})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6558781862258911})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6079023480415344})
store['active_learning_steps'][120]['training']['best_epoch']=4
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.556218798828125}
store['active_learning_steps'][120]['acquisition']={'indices': [50022, 42801, 26716, 12768, 25124], 'labels': [-1, -1, 6, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6801215410232544})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5852259397506714})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6068965792655945})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6253867149353027})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5822675824165344})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6566891670227051})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6179078817367554})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6501604318618774})
store['active_learning_steps'][121]['training']['best_epoch']=5
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.531541943359375}
store['active_learning_steps'][121]['acquisition']={'indices': [31805, 54663, 10800, 14118, 51860], 'labels': [-1, -1, -1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8045917749404907})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5668821334838867})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5360777378082275})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6005311012268066})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5786318182945251})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6255476474761963})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.513268701171875}
store['active_learning_steps'][122]['acquisition']={'indices': [47105, 15097, 57957, 58557, 2335], 'labels': [-1, -1, 1, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7193878889083862})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5902485847473145})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6502803564071655})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6325286626815796})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5619686841964722})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6118793487548828})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6237273216247559})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7331224679946899})
store['active_learning_steps'][123]['training']['best_epoch']=5
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.51841533203125}
store['active_learning_steps'][123]['acquisition']={'indices': [2602, 25564, 17446, 30772, 54063], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7287594079971313})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5901049375534058})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5899169445037842})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6349563598632812})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6038345694541931})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6324399709701538})
store['active_learning_steps'][124]['training']['best_epoch']=3
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.53009619140625}
store['active_learning_steps'][124]['acquisition']={'indices': [1508, 38443, 12856, 42550, 3267], 'labels': [-1, -1, -1, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6298177242279053})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6377185583114624})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5565769076347351})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5575382709503174})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5641671419143677})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5620293617248535})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.50122421875}
store['active_learning_steps'][125]['acquisition']={'indices': [23249, 31065, 34395, 58104, 5195], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7029858827590942})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5141135454177856})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5333360433578491})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5902423858642578})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5346240401268005})
store['active_learning_steps'][126]['training']['best_epoch']=2
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.465181982421875}
store['active_learning_steps'][126]['acquisition']={'indices': [9108, 36909, 48505, 17158, 42462], 'labels': [-1, 4, -1, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6983884572982788})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5764669179916382})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6260635852813721})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6167771220207214})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7198548316955566})
store['active_learning_steps'][127]['training']['best_epoch']=2
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.527661669921875}
store['active_learning_steps'][127]['acquisition']={'indices': [42729, 10414, 5431, 39868, 47144], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6272168755531311})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5514394044876099})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5662306547164917})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5828394889831543})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6603566408157349})
store['active_learning_steps'][128]['training']['best_epoch']=2
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.48569970703125}
store['active_learning_steps'][128]['acquisition']={'indices': [59709, 54728, 46747, 51206, 7915], 'labels': [6, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6950944662094116})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5956445932388306})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5923980474472046})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6093246936798096})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5267981886863708})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7178440093994141})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6390132904052734})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6444334983825684})
store['active_learning_steps'][129]['training']['best_epoch']=5
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.501649609375}
store['active_learning_steps'][129]['acquisition']={'indices': [11217, 46439, 56252, 52735, 335], 'labels': [-1, 0, -1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7139869928359985})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5772373080253601})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6380640268325806})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5573943853378296})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5658445954322815})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6186771392822266})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6574438810348511})
store['active_learning_steps'][130]['training']['best_epoch']=4
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.507064013671875}
store['active_learning_steps'][130]['acquisition']={'indices': [42812, 19016, 27426, 2104, 48925], 'labels': [-1, -1, -1, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6562344431877136})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5723868608474731})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5402697324752808})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5821044445037842})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5822031497955322})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5772954225540161})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.478440380859375}
store['active_learning_steps'][131]['acquisition']={'indices': [56660, 46142, 6693, 35822, 52662], 'labels': [1, 1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6717804074287415})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5905616879463196})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5876450538635254})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5762425661087036})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5550209283828735})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6362602710723877})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5923130512237549})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.576461911201477})
store['active_learning_steps'][132]['training']['best_epoch']=5
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.5077044921875}
store['active_learning_steps'][132]['acquisition']={'indices': [58725, 6031, 31283, 12570, 44232], 'labels': [7, -1, 3, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7569087743759155})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5939798355102539})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.561714768409729})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6034247875213623})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5958142280578613})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6015332937240601})
store['active_learning_steps'][133]['training']['best_epoch']=3
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.50421240234375}
store['active_learning_steps'][133]['acquisition']={'indices': [20328, 16450, 53735, 8312, 30813], 'labels': [-1, 4, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6577377915382385})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5320044755935669})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4886972904205322})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5458781719207764})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5700808763504028})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.614803671836853})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.457698974609375}
store['active_learning_steps'][134]['acquisition']={'indices': [34107, 44234, 16824, 16253, 24950], 'labels': [8, 9, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7429788708686829})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.542499303817749})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5271205902099609})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5475335717201233})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5313194990158081})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5926276445388794})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.46785810546875}
store['active_learning_steps'][135]['acquisition']={'indices': [22533, 52858, 10612, 42659, 51701], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7744505405426025})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6186173558235168})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5347400307655334})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5779963731765747})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.544282078742981})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5725736618041992})
store['active_learning_steps'][136]['training']['best_epoch']=3
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.52907939453125}
store['active_learning_steps'][136]['acquisition']={'indices': [24549, 10236, 5649, 37860, 4962], 'labels': [9, -1, -1, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6544471979141235})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5206658840179443})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5200457572937012})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47669872641563416})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5201421976089478})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5137060284614563})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4755514860153198})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5408545136451721})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5992681980133057})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47631990909576416})
store['active_learning_steps'][137]['training']['best_epoch']=7
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.459883203125}
store['active_learning_steps'][137]['acquisition']={'indices': [44429, 48980, 44676, 10542, 38507], 'labels': [9, -1, 8, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6831042766571045})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5281432271003723})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5462849736213684})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5330085754394531})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5247159004211426})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.591374397277832})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5896723866462708})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6007518768310547})
store['active_learning_steps'][138]['training']['best_epoch']=5
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.520577294921875}
store['active_learning_steps'][138]['acquisition']={'indices': [2473, 54845, 18270, 4381, 678], 'labels': [-1, 3, 1, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7087221741676331})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5178282260894775})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45088058710098267})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49728041887283325})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5653941035270691})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5162360668182373})
store['active_learning_steps'][139]['training']['best_epoch']=3
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.45065283203125}
store['active_learning_steps'][139]['acquisition']={'indices': [36238, 48783, 56502, 5912, 11876], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6905369162559509})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5398526191711426})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5238101482391357})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5203955173492432})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.579865574836731})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5098387598991394})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5692621469497681})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5663902759552002})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5788089036941528})
store['active_learning_steps'][140]['training']['best_epoch']=6
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.486285009765625}
store['active_learning_steps'][140]['acquisition']={'indices': [525, 26136, 34505, 57357, 5334], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.656493604183197})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5337424278259277})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.538593590259552})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5229908227920532})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5604966878890991})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5656523704528809})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5189619064331055})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49121034145355225})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5645774602890015})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5568443536758423})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5615765452384949})
store['active_learning_steps'][141]['training']['best_epoch']=8
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.4595962890625}
store['active_learning_steps'][141]['acquisition']={'indices': [57345, 24342, 40070, 56008, 36444], 'labels': [5, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6529576182365417})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5356712341308594})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.548414945602417})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5051610469818115})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5019316673278809})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5360153317451477})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5099484920501709})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5488603711128235})
store['active_learning_steps'][142]['training']['best_epoch']=5
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.47756328125}
store['active_learning_steps'][142]['acquisition']={'indices': [36729, 48083, 55766, 9723, 57830], 'labels': [5, 6, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6323763132095337})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.503930926322937})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5237654447555542})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5094729661941528})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5100799798965454})
store['active_learning_steps'][143]['training']['best_epoch']=2
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.493553125}
store['active_learning_steps'][143]['acquisition']={'indices': [48542, 3677, 38619, 36271, 31593], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6261934041976929})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49937355518341064})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4891788959503174})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47103604674339294})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5085523128509521})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5147247314453125})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5327538251876831})
store['active_learning_steps'][144]['training']['best_epoch']=4
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.4625478515625}
store['active_learning_steps'][144]['acquisition']={'indices': [6591, 37451, 50231, 48667, 35574], 'labels': [-1, 6, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6769934892654419})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5344863533973694})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5414828062057495})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5498149394989014})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.524070680141449})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5503005385398865})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5664726495742798})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6426701545715332})
store['active_learning_steps'][145]['training']['best_epoch']=5
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.48828203125}
store['active_learning_steps'][145]['acquisition']={'indices': [7193, 5095, 4408, 6248, 46914], 'labels': [5, 2, 6, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6931369304656982})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5206987857818604})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5263330340385437})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.480932354927063})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5633684396743774})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5739153623580933})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.539470911026001})
store['active_learning_steps'][146]['training']['best_epoch']=4
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.445710546875}
store['active_learning_steps'][146]['acquisition']={'indices': [41807, 1261, 7828, 44645, 55501], 'labels': [-1, 4, 1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.703529417514801})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5244975686073303})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.511894166469574})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.511391282081604})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49894407391548157})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5056195259094238})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6283184289932251})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5462350249290466})
store['active_learning_steps'][147]['training']['best_epoch']=5
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.464825537109375}
store['active_learning_steps'][147]['acquisition']={'indices': [3606, 852, 43964, 12873, 46047], 'labels': [-1, 6, 2, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6578332185745239})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5771386623382568})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.507570207118988})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4994836449623108})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5300799608230591})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5959622859954834})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5732648372650146})
store['active_learning_steps'][148]['training']['best_epoch']=4
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.438084619140625}
store['active_learning_steps'][148]['acquisition']={'indices': [24790, 4537, 48308, 30243, 15037], 'labels': [-1, 8, 7, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6863603591918945})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5014528632164001})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48632508516311646})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5546576976776123})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5617855787277222})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5241019129753113})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.470035302734375}
store['active_learning_steps'][149]['acquisition']={'indices': [36733, 47081, 3376, 52333, 11176], 'labels': [-1, 5, -1, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6644363403320312})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5419719815254211})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5061508417129517})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5072529911994934})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5251806378364563})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5318927764892578})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.4982609375}
store['active_learning_steps'][150]['acquisition']={'indices': [35989, 14835, 34840, 39191, 23907], 'labels': [4, -1, 6, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.673723042011261})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5387430787086487})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5011259317398071})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4859766364097595})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.45991772413253784})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5492208003997803})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5228661298751831})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5351388454437256})
store['active_learning_steps'][151]['training']['best_epoch']=5
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.424869140625}
store['active_learning_steps'][151]['acquisition']={'indices': [21856, 27979, 41995, 44454, 11647], 'labels': [6, 4, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7028801441192627})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5099121332168579})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4480782151222229})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4869389533996582})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4885883331298828})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5182949304580688})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9282, 'crossentropy': 0.43902294921875}
store['active_learning_steps'][152]['acquisition']={'indices': [47658, 41373, 645, 49390, 8334], 'labels': [-1, -1, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6681033968925476})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5001150369644165})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5025674700737})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49192243814468384})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.50782310962677})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5247737765312195})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5430257320404053})
store['active_learning_steps'][153]['training']['best_epoch']=4
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.438453173828125}
store['active_learning_steps'][153]['acquisition']={'indices': [31812, 58668, 54944, 23833, 52410], 'labels': [7, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6922818422317505})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5365694761276245})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5292982459068298})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5636415481567383})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5262141227722168})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5171909332275391})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5395857095718384})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5521230697631836})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5280007123947144})
store['active_learning_steps'][154]['training']['best_epoch']=6
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9354, 'crossentropy': 0.4828375}
store['active_learning_steps'][154]['acquisition']={'indices': [13411, 8479, 32161, 985, 59845], 'labels': [-1, 5, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6510918140411377})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.533437967300415})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.485815167427063})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4937465786933899})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5022869110107422})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5134119987487793})
store['active_learning_steps'][155]['training']['best_epoch']=3
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.44271025390625}
store['active_learning_steps'][155]['acquisition']={'indices': [40138, 20757, 16313, 52452, 29645], 'labels': [8, 6, -1, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6927154660224915})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5528122186660767})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4788553714752197})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4681398868560791})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4791167378425598})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4757356643676758})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5106799602508545})
store['active_learning_steps'][156]['training']['best_epoch']=4
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.392837451171875}
store['active_learning_steps'][156]['acquisition']={'indices': [24375, 45112, 33800, 6845, 42071], 'labels': [7, 0, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6658403873443604})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5042569637298584})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5091663002967834})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4844367504119873})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5083782076835632})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5371135473251343})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5441212058067322})
store['active_learning_steps'][157]['training']['best_epoch']=4
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9293, 'crossentropy': 0.489727099609375}
store['active_learning_steps'][157]['acquisition']={'indices': [51724, 49418, 21831, 41684, 48686], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.694230854511261})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.505881130695343})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5131443738937378})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4878525137901306})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5227861404418945})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5301727652549744})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49074816703796387})
store['active_learning_steps'][158]['training']['best_epoch']=4
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9373, 'crossentropy': 0.42290869140625}
store['active_learning_steps'][158]['acquisition']={'indices': [22422, 7489, 10233, 59422, 14450], 'labels': [-1, -1, 8, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6003948450088501})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.48488855361938477})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4870226979255676})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49686354398727417})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4474533200263977})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5305289626121521})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5350483655929565})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5473823547363281})
store['active_learning_steps'][159]['training']['best_epoch']=5
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.43745185546875}
store['active_learning_steps'][159]['acquisition']={'indices': [30971, 2054, 59178, 15403, 40932], 'labels': [-1, 7, 3, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6368751525878906})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5193765759468079})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4586363434791565})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4709165394306183})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4863680601119995})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49206286668777466})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.426829052734375}
store['active_learning_steps'][160]['acquisition']={'indices': [49232, 10108, 32628, 5956, 21150], 'labels': [-1, 6, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.596333384513855})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49117791652679443})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4734950661659241})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4475095868110657})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5449228882789612})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4860128164291382})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.520252525806427})
store['active_learning_steps'][161]['training']['best_epoch']=4
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9389, 'crossentropy': 0.433627685546875}
store['active_learning_steps'][161]['acquisition']={'indices': [33728, 2843, 2835, 5468, 12000], 'labels': [6, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6660035848617554})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49528926610946655})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46416568756103516})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4427587389945984})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5187801122665405})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5210047364234924})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4902294874191284})
store['active_learning_steps'][162]['training']['best_epoch']=4
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9366, 'crossentropy': 0.411148095703125}
store['active_learning_steps'][162]['acquisition']={'indices': [8364, 52038, 10054, 31045, 54730], 'labels': [7, 3, 8, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7303009033203125})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5010945796966553})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49135667085647583})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5140830278396606})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5206369161605835})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5376104116439819})
store['active_learning_steps'][163]['training']['best_epoch']=3
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.428478271484375}
store['active_learning_steps'][163]['acquisition']={'indices': [39963, 27888, 14340, 4160, 59584], 'labels': [4, 2, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6254816055297852})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4902234673500061})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48167097568511963})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41829031705856323})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45791617035865784})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4674863815307617})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48348742723464966})
store['active_learning_steps'][164]['training']['best_epoch']=4
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.3870423828125}
store['active_learning_steps'][164]['acquisition']={'indices': [36921, 6008, 50391, 31110, 58533], 'labels': [-1, 0, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6733380556106567})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5056617856025696})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4357832074165344})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44755634665489197})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.45448464155197144})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4439955949783325})
store['active_learning_steps'][165]['training']['best_epoch']=3
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.38724833984375}
store['active_learning_steps'][165]['acquisition']={'indices': [7933, 32076, 29573, 6759, 18683], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7009894847869873})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4652196764945984})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5025292634963989})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.44526374340057373})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4759901165962219})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.536369800567627})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4605686366558075})
store['active_learning_steps'][166]['training']['best_epoch']=4
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9402, 'crossentropy': 0.405820849609375}
store['active_learning_steps'][166]['acquisition']={'indices': [31850, 37171, 34041, 16638, 55624], 'labels': [-1, -1, -1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5986618995666504})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5254485607147217})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5226138234138489})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5248321294784546})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.476370632648468})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5215248465538025})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5423086881637573})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6035288572311401})
store['active_learning_steps'][167]['training']['best_epoch']=5
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9402, 'crossentropy': 0.42824013671875}
store['active_learning_steps'][167]['acquisition']={'indices': [12680, 16530, 40007, 294, 41315], 'labels': [1, 3, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6653895974159241})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5199670791625977})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4941759705543518})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4641302824020386})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4762957692146301})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5361212491989136})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5572401881217957})
store['active_learning_steps'][168]['training']['best_epoch']=4
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.4218880859375}
store['active_learning_steps'][168]['acquisition']={'indices': [15035, 28035, 26126, 26627, 11460], 'labels': [4, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6049540042877197})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4721585214138031})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41732245683670044})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44124770164489746})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47025713324546814})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4795832633972168})
store['active_learning_steps'][169]['training']['best_epoch']=3
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.944, 'crossentropy': 0.3807516357421875}
store['active_learning_steps'][169]['acquisition']={'indices': [46675, 33537, 47572, 1766, 12805], 'labels': [-1, 5, -1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6619573831558228})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.49372702836990356})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4528190493583679})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4488486051559448})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41984641551971436})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43168893456459045})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5554456114768982})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49482977390289307})
store['active_learning_steps'][170]['training']['best_epoch']=5
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.364232080078125}
store['active_learning_steps'][170]['acquisition']={'indices': [47434, 16954, 24318, 35463, 48009], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6238085031509399})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49490588903427124})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5575357675552368})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5064892172813416})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5616636276245117})
store['active_learning_steps'][171]['training']['best_epoch']=2
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.42952939453125}
store['active_learning_steps'][171]['acquisition']={'indices': [55535, 33436, 6088, 54559, 51462], 'labels': [7, -1, 7, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6620402336120605})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5387715101242065})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5070830583572388})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48967260122299194})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5361166000366211})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4771989583969116})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5529881119728088})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5103689432144165})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46022629737854004})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5114402770996094})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4788397550582886})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4971497654914856})
store['active_learning_steps'][172]['training']['best_epoch']=9
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9455, 'crossentropy': 0.438982470703125}
store['active_learning_steps'][172]['acquisition']={'indices': [11840, 2302, 28449, 37138, 52495], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6680091619491577})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.562936544418335})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47719746828079224})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5256258249282837})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5235486030578613})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5342188477516174})
store['active_learning_steps'][173]['training']['best_epoch']=3
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.42673662109375}
store['active_learning_steps'][173]['acquisition']={'indices': [42612, 42636, 16836, 10749, 41316], 'labels': [0, -1, 7, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6632115840911865})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.472606897354126})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4571225047111511})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4468350112438202})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4667261838912964})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47769391536712646})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49683433771133423})
store['active_learning_steps'][174]['training']['best_epoch']=4
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.41216171875}
store['active_learning_steps'][174]['acquisition']={'indices': [22138, 53065, 40655, 18794, 44844], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6653314232826233})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.46819406747817993})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4344460368156433})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5108934640884399})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4996233284473419})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5455513000488281})
store['active_learning_steps'][175]['training']['best_epoch']=3
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.3951586669921875}
store['active_learning_steps'][175]['acquisition']={'indices': [48710, 25843, 49423, 2001, 47479], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][176]['training']={}
store['active_learning_steps'][176]['training']['epochs']=[]
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.658919632434845})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.506879985332489})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4743903577327728})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.466028094291687})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5591974854469299})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5268535614013672})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.529742419719696})
store['active_learning_steps'][176]['training']['best_epoch']=4
store['active_learning_steps'][176]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.41366298828125}
store['active_learning_steps'][176]['acquisition']={'indices': [11303, 20596, 53906, 37120, 23439], 'labels': [-1, 6, 8, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][177]['training']={}
store['active_learning_steps'][177]['training']['epochs']=[]
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6447286605834961})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5110504031181335})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.47938793897628784})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4406999349594116})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47739577293395996})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4854239821434021})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4905772805213928})
store['active_learning_steps'][177]['training']['best_epoch']=4
store['active_learning_steps'][177]['evaluation_metrics']={'accuracy': 0.9442, 'crossentropy': 0.39539677734375}
store['active_learning_steps'][177]['acquisition']={'indices': [10295, 18384, 23108, 43063, 7995], 'labels': [7, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][178]['training']={}
store['active_learning_steps'][178]['training']['epochs']=[]
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6488518714904785})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5548787117004395})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48313212394714355})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49204665422439575})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5047916769981384})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5483256578445435})
store['active_learning_steps'][178]['training']['best_epoch']=3
store['active_learning_steps'][178]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.43437822265625}
store['active_learning_steps'][178]['acquisition']={'indices': [50034, 34525, 34236, 7054, 3980], 'labels': [-1, 3, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][179]['training']={}
store['active_learning_steps'][179]['training']['epochs']=[]
store['active_learning_steps'][179]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.685067892074585})
store['active_learning_steps'][179]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5131264328956604})
store['active_learning_steps'][179]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4467904269695282})
store['active_learning_steps'][179]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44814538955688477})
store['active_learning_steps'][179]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4725792407989502})
store['active_learning_steps'][179]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4551829695701599})
store['active_learning_steps'][179]['training']['best_epoch']=3
store['active_learning_steps'][179]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.41455986328125}
store['active_learning_steps'][179]['acquisition']={'indices': [48639, 45883, 42083, 40527, 28705], 'labels': [7, 5, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][180]['training']={}
store['active_learning_steps'][180]['training']['epochs']=[]
store['active_learning_steps'][180]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6868553161621094})
store['active_learning_steps'][180]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48064666986465454})
store['active_learning_steps'][180]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4147687554359436})
store['active_learning_steps'][180]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.462999552488327})
store['active_learning_steps'][180]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4689508080482483})
store['active_learning_steps'][180]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4566357135772705})
store['active_learning_steps'][180]['training']['best_epoch']=3
store['active_learning_steps'][180]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.3770835205078125}
store['active_learning_steps'][180]['acquisition']={'indices': [26723, 7083, 52497, 17824, 9892], 'labels': [6, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][181]['training']={}
store['active_learning_steps'][181]['training']['epochs']=[]
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6013851165771484})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4633415937423706})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4592360258102417})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49323731660842896})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45961934328079224})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45589348673820496})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4798603057861328})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4697234034538269})
store['active_learning_steps'][181]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47878581285476685})
store['active_learning_steps'][181]['training']['best_epoch']=6
store['active_learning_steps'][181]['evaluation_metrics']={'accuracy': 0.9472, 'crossentropy': 0.38539814453125}
