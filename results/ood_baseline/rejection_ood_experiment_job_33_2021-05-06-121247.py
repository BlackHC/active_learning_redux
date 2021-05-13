store = {}
store['timestamp']=1620299567
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=33']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=33
store['worker_id']=33
store['num_workers']=40
store['config']={'seed': 46, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.385983467102051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6500322818756104})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9436097145080566})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.7514076232910156})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6658, 'crossentropy': 2.15819140625}
store['active_learning_steps'][0]['acquisition']={'indices': [31766, 12664, 13063, 5669, 51488], 'labels': [1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.252570152282715})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.622464179992676})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9617583751678467})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7903401851654053})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6687, 'crossentropy': 1.9788275390625}
store['active_learning_steps'][1]['acquisition']={'indices': [22370, 7648, 24487, 13243, 47281], 'labels': [1, -1, 1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1406383514404297})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.609994888305664})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.648052930831909})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.7355051040649414})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6699, 'crossentropy': 2.170923046875}
store['active_learning_steps'][2]['acquisition']={'indices': [47490, 24985, 46410, 20269, 58407], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.36033296585083})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6958160400390625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.7119526863098145})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.8921828269958496})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6748, 'crossentropy': 2.074771484375}
store['active_learning_steps'][3]['acquisition']={'indices': [46493, 27954, 26248, 5995, 46066], 'labels': [-1, 5, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.3220396041870117})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6894779205322266})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.967890977859497})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1765389442443848})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6768, 'crossentropy': 1.8966009765625}
store['active_learning_steps'][4]['acquisition']={'indices': [56118, 41789, 19459, 52949, 49429], 'labels': [-1, 0, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.9315426349639893})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.238959312438965})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.553896188735962})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.5871527194976807})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7089, 'crossentropy': 1.6764904296875}
store['active_learning_steps'][5]['acquisition']={'indices': [48909, 24519, 33362, 36689, 5201], 'labels': [7, 5, 7, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8751113414764404})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.408536434173584})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.60271954536438})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.6372857093811035})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7139, 'crossentropy': 1.78881953125}
store['active_learning_steps'][6]['acquisition']={'indices': [25588, 35050, 45960, 53953, 30788], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.9171063899993896})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9648051261901855})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.372220516204834})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.153956651687622})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7022, 'crossentropy': 1.7341001953125}
store['active_learning_steps'][7]['acquisition']={'indices': [41944, 57567, 26387, 48941, 18891], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.9830639362335205})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.233255386352539})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.5976572036743164})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.118659019470215})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7058, 'crossentropy': 1.6404630859375}
store['active_learning_steps'][8]['acquisition']={'indices': [39261, 39931, 42113, 44796, 44069], 'labels': [7, -1, 1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.66145920753479})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.2827978134155273})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.163997173309326})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.3331398963928223})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7424, 'crossentropy': 1.578169921875}
store['active_learning_steps'][9]['acquisition']={'indices': [3681, 33803, 14860, 46551, 6396], 'labels': [5, 4, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.4893866777420044})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.0161333084106445})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.3051326274871826})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.2438783645629883})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.756, 'crossentropy': 1.400101171875}
store['active_learning_steps'][10]['acquisition']={'indices': [33507, 38556, 26254, 32856, 9640], 'labels': [-1, 7, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.700716495513916})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.8368139266967773})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.980683445930481})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.1865055561065674})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7273, 'crossentropy': 1.581648046875}
store['active_learning_steps'][11]['acquisition']={'indices': [9903, 16943, 2746, 49593, 885], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.6392383575439453})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9911973476409912})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.2292404174804688})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.294750213623047})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7215, 'crossentropy': 1.5275123046875}
store['active_learning_steps'][12]['acquisition']={'indices': [16652, 7323, 19634, 5698, 37346], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5672636032104492})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.8731539249420166})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.149134397506714})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2788538932800293})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7391, 'crossentropy': 1.4865208984375}
store['active_learning_steps'][13]['acquisition']={'indices': [29443, 30347, 14999, 37579, 59954], 'labels': [7, 8, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.3389960527420044})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.8463671207427979})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.7515419721603394})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.8946093320846558})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7803, 'crossentropy': 1.2657408203125}
store['active_learning_steps'][14]['acquisition']={'indices': [25237, 29084, 59674, 6251, 28982], 'labels': [-1, 9, 4, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.432060956954956})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.5469783544540405})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.9227197170257568})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.8970141410827637})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7607, 'crossentropy': 1.38528662109375}
store['active_learning_steps'][15]['acquisition']={'indices': [40821, 33049, 55173, 45851, 48014], 'labels': [-1, 3, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.3372312784194946})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.6570746898651123})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7349348068237305})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 2.006538152694702})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7815, 'crossentropy': 1.1927611328125}
store['active_learning_steps'][16]['acquisition']={'indices': [23372, 35048, 49481, 48988, 49343], 'labels': [0, 1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.438186764717102})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.6630244255065918})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.9721097946166992})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9312629699707031})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7771, 'crossentropy': 1.3062814453125}
store['active_learning_steps'][17]['acquisition']={'indices': [7106, 594, 35293, 26242, 35018], 'labels': [3, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3222863674163818})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.731710433959961})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6698217391967773})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.8546168804168701})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8039, 'crossentropy': 1.20103125}
store['active_learning_steps'][18]['acquisition']={'indices': [10792, 51779, 7236, 40291, 27790], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2637286186218262})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7155673503875732})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.9880470037460327})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.9839460849761963})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7947, 'crossentropy': 1.17563798828125}
store['active_learning_steps'][19]['acquisition']={'indices': [32994, 20386, 5835, 32161, 26552], 'labels': [6, 7, 4, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4716354608535767})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.7198894023895264})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.8606526851654053})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.691828966140747})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7682, 'crossentropy': 1.30830078125}
store['active_learning_steps'][20]['acquisition']={'indices': [57105, 24966, 20037, 51033, 4644], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3967963457107544})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.5779703855514526})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.7825818061828613})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.9493604898452759})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7771, 'crossentropy': 1.24940498046875}
store['active_learning_steps'][21]['acquisition']={'indices': [12141, 7670, 58235, 3565, 29125], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.140904188156128})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4232378005981445})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7140142917633057})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.8529863357543945})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8007, 'crossentropy': 1.1650591796875}
store['active_learning_steps'][22]['acquisition']={'indices': [53917, 37521, 54479, 56379, 47610], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4068795442581177})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.6004376411437988})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.6081241369247437})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.7814462184906006})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7853, 'crossentropy': 1.21918974609375}
store['active_learning_steps'][23]['acquisition']={'indices': [14498, 45713, 52422, 46049, 40273], 'labels': [1, 6, 2, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.350954532623291})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.4208176136016846})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.8169851303100586})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.8801143169403076})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8014, 'crossentropy': 1.13783583984375}
store['active_learning_steps'][24]['acquisition']={'indices': [52806, 59582, 6291, 34297, 58350], 'labels': [-1, -1, 3, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.2500593662261963})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4714112281799316})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.734323263168335})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.901602029800415})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7953, 'crossentropy': 1.20924248046875}
store['active_learning_steps'][25]['acquisition']={'indices': [46932, 29259, 25253, 43347, 5414], 'labels': [3, 8, 1, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.37821364402771})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8837270736694336})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.9358456134796143})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.4669272899627686})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7893, 'crossentropy': 1.21881259765625}
store['active_learning_steps'][26]['acquisition']={'indices': [46888, 56899, 2065, 49682, 53129], 'labels': [7, 6, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3202024698257446})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.7288776636123657})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.5926344394683838})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.854546308517456})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8077, 'crossentropy': 1.14966279296875}
store['active_learning_steps'][27]['acquisition']={'indices': [26792, 25323, 2652, 49456, 40378], 'labels': [-1, -1, 3, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1681065559387207})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.6224784851074219})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.6468234062194824})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.7112717628479004})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7996, 'crossentropy': 1.08789892578125}
store['active_learning_steps'][28]['acquisition']={'indices': [12961, 6532, 32806, 34275, 19845], 'labels': [7, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.277174949645996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6173620223999023})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5710008144378662})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.6006848812103271})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8026, 'crossentropy': 1.13961767578125}
store['active_learning_steps'][29]['acquisition']={'indices': [33761, 27209, 52082, 1771, 32067], 'labels': [4, 0, -1, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.144963264465332})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.4854726791381836})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.6213809251785278})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6311087608337402})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7833, 'crossentropy': 1.10279560546875}
store['active_learning_steps'][30]['acquisition']={'indices': [48659, 41085, 7463, 16405, 25522], 'labels': [-1, -1, 3, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1556099653244019})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.5579860210418701})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.724745750427246})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.7353997230529785})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8134, 'crossentropy': 0.99748740234375}
store['active_learning_steps'][31]['acquisition']={'indices': [11892, 26938, 4080, 24046, 52], 'labels': [6, 6, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.187328815460205})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.4329676628112793})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.588914155960083})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.6011512279510498})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7973, 'crossentropy': 1.08329765625}
store['active_learning_steps'][32]['acquisition']={'indices': [17643, 26048, 23532, 9509, 6511], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1405808925628662})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2403883934020996})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4227042198181152})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4260493516921997})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8168, 'crossentropy': 1.00340830078125}
store['active_learning_steps'][33]['acquisition']={'indices': [21453, 9334, 59150, 48079, 17827], 'labels': [2, 8, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1244966983795166})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2885204553604126})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3456785678863525})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4445570707321167})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8145, 'crossentropy': 1.0019072265625}
store['active_learning_steps'][34]['acquisition']={'indices': [51949, 28006, 22270, 20817, 23724], 'labels': [-1, 3, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1791926622390747})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3014647960662842})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.4030001163482666})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4791922569274902})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8055, 'crossentropy': 1.1091953125}
store['active_learning_steps'][35]['acquisition']={'indices': [17530, 57664, 24094, 58781, 15455], 'labels': [8, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2550048828125})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3201241493225098})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.5521907806396484})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.4742445945739746})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7934, 'crossentropy': 1.141791796875}
store['active_learning_steps'][36]['acquisition']={'indices': [49444, 23867, 43110, 10186, 12633], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0498155355453491})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3047982454299927})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3819689750671387})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.307781457901001})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8087, 'crossentropy': 1.0238833984375}
store['active_learning_steps'][37]['acquisition']={'indices': [39994, 24590, 10543, 37304, 46994], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2051666975021362})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.2356497049331665})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4922990798950195})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.5195372104644775})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8123, 'crossentropy': 1.079604296875}
store['active_learning_steps'][38]['acquisition']={'indices': [29071, 8039, 20561, 52946, 50211], 'labels': [-1, -1, 3, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1668338775634766})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5098987817764282})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.5611470937728882})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.6126492023468018})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8119, 'crossentropy': 1.03733857421875}
store['active_learning_steps'][39]['acquisition']={'indices': [32320, 31535, 44160, 48958, 42947], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1164300441741943})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2313823699951172})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2165952920913696})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5189803838729858})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8299, 'crossentropy': 0.966296875}
store['active_learning_steps'][40]['acquisition']={'indices': [14319, 8649, 9510, 32962, 49363], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1088767051696777})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1748790740966797})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3235217332839966})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3785192966461182})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7926, 'crossentropy': 1.08893896484375}
store['active_learning_steps'][41]['acquisition']={'indices': [20206, 33052, 33005, 58146, 43588], 'labels': [-1, -1, 1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.012636661529541})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2117087841033936})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3437975645065308})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.5131598711013794})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8252, 'crossentropy': 0.99591181640625}
store['active_learning_steps'][42]['acquisition']={'indices': [8861, 9358, 7881, 2923, 52218], 'labels': [7, 8, 3, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9293487071990967})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2329161167144775})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.3016380071640015})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.4325876235961914})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.839, 'crossentropy': 0.92713037109375}
store['active_learning_steps'][43]['acquisition']={'indices': [22613, 20151, 15082, 23496, 42783], 'labels': [7, -1, 1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9311379194259644})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0948288440704346})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2313228845596313})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1598390340805054})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8198, 'crossentropy': 0.9228642578125}
store['active_learning_steps'][44]['acquisition']={'indices': [42079, 46075, 9855, 45531, 7533], 'labels': [8, -1, 2, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0637757778167725})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2343690395355225})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2037980556488037})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.29404616355896})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8105, 'crossentropy': 1.004476171875}
store['active_learning_steps'][45]['acquisition']={'indices': [7732, 11842, 49218, 11917, 4193], 'labels': [2, -1, 0, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.921904444694519})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0294774770736694})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1656016111373901})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2059860229492188})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8261, 'crossentropy': 0.89978037109375}
store['active_learning_steps'][46]['acquisition']={'indices': [26845, 44782, 45290, 10141, 23274], 'labels': [-1, -1, -1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9150664806365967})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0564522743225098})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0344527959823608})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.081348180770874})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8388, 'crossentropy': 0.88319833984375}
store['active_learning_steps'][47]['acquisition']={'indices': [27316, 14271, 49618, 36892, 1582], 'labels': [-1, 1, 8, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9628078937530518})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0219228267669678})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9645650386810303})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0690873861312866})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8353, 'crossentropy': 0.90873681640625}
store['active_learning_steps'][48]['acquisition']={'indices': [53345, 53623, 9902, 25787, 14635], 'labels': [-1, 9, -1, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8813717365264893})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.975204348564148})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9996498823165894})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1248281002044678})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8321, 'crossentropy': 0.8709955078125}
store['active_learning_steps'][49]['acquisition']={'indices': [47079, 55659, 10973, 36796, 7799], 'labels': [0, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9192872047424316})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8463832139968872})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9967566728591919})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0172762870788574})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.116081953048706})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8677, 'crossentropy': 0.83075634765625}
store['active_learning_steps'][50]['acquisition']={'indices': [27577, 26148, 57830, 22778, 6343], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9588397741317749})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9467468857765198})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.983832836151123})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9208705425262451})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9659473896026611})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0002273321151733})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0629796981811523})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8747, 'crossentropy': 0.94862978515625}
store['active_learning_steps'][51]['acquisition']={'indices': [56427, 10321, 5660, 32806, 23197], 'labels': [2, -1, 3, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8736594319343567})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8378527760505676})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9416371583938599})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9197524785995483})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0003750324249268})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.873, 'crossentropy': 0.810209814453125}
store['active_learning_steps'][52]['acquisition']={'indices': [5818, 23038, 59945, 20024, 32588], 'labels': [7, 2, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.813784658908844})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.839655339717865})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9056488871574402})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0691248178482056})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8538, 'crossentropy': 0.776652880859375}
store['active_learning_steps'][53]['acquisition']={'indices': [37893, 55660, 22127, 10403, 27727], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9244428873062134})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8621397614479065})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9223262071609497})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9453921318054199})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9388790130615234})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8674, 'crossentropy': 0.88213271484375}
store['active_learning_steps'][54]['acquisition']={'indices': [55101, 34164, 15863, 15285, 451], 'labels': [-1, -1, 0, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9314696788787842})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8478907346725464})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.894971489906311})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.098483681678772})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.002063274383545})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8723, 'crossentropy': 0.81550654296875}
store['active_learning_steps'][55]['acquisition']={'indices': [10074, 36068, 15214, 10532, 10370], 'labels': [-1, -1, -1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7724894285202026})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8698486685752869})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7914186716079712})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9462832808494568})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8619, 'crossentropy': 0.755303759765625}
store['active_learning_steps'][56]['acquisition']={'indices': [24787, 13796, 1412, 8591, 14064], 'labels': [-1, -1, 7, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8224121332168579})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8306453227996826})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8893452882766724})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9520144462585449})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.857, 'crossentropy': 0.79596591796875}
store['active_learning_steps'][57]['acquisition']={'indices': [27314, 49148, 7525, 22533, 52916], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8571255207061768})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9031306505203247})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9501524567604065})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9346825480461121})
store['active_learning_steps'][58]['training']['best_epoch']=1
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8391, 'crossentropy': 0.83719599609375}
store['active_learning_steps'][58]['acquisition']={'indices': [53191, 38272, 25252, 11747, 47340], 'labels': [8, -1, 0, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8447675108909607})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8749921321868896})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9235632419586182})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9518027305603027})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8347, 'crossentropy': 0.81041484375}
store['active_learning_steps'][59]['acquisition']={'indices': [6586, 19825, 49267, 17086, 40770], 'labels': [1, -1, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9466102123260498})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8296335935592651})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8710092902183533})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9211442470550537})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9199231266975403})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8724, 'crossentropy': 0.8312103515625}
store['active_learning_steps'][60]['acquisition']={'indices': [49317, 886, 42343, 28495, 30836], 'labels': [1, -1, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8389492630958557})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8813337087631226})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8705905675888062})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0148063898086548})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8529, 'crossentropy': 0.8002943359375}
store['active_learning_steps'][61]['acquisition']={'indices': [53146, 42497, 15590, 21745, 22974], 'labels': [-1, -1, 0, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8491008281707764})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8022835850715637})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8815466165542603})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9703311920166016})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.985164225101471})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8668, 'crossentropy': 0.7916890625}
store['active_learning_steps'][62]['acquisition']={'indices': [11857, 35873, 16665, 49011, 49881], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7655894756317139})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7832890748977661})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9158234596252441})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8058233261108398})
store['active_learning_steps'][63]['training']['best_epoch']=1
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8704, 'crossentropy': 0.7520744140625}
store['active_learning_steps'][63]['acquisition']={'indices': [2370, 7490, 49691, 14262, 4460], 'labels': [9, 6, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8250184655189514})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8229475021362305})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9201732873916626})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8696210384368896})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.972383439540863})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.8071259765625}
store['active_learning_steps'][64]['acquisition']={'indices': [49994, 26693, 27807, 19285, 58673], 'labels': [4, -1, 6, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7918425798416138})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7970399260520935})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.922837495803833})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9467145204544067})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.849, 'crossentropy': 0.815591943359375}
store['active_learning_steps'][65]['acquisition']={'indices': [20818, 50451, 58368, 19258, 41147], 'labels': [-1, 5, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8648306727409363})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7985074520111084})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7977120280265808})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.907384991645813})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9988548755645752})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9192368984222412})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.81514990234375}
store['active_learning_steps'][66]['acquisition']={'indices': [17574, 13188, 19967, 42931, 43081], 'labels': [3, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7614004015922546})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7510746717453003})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8101979494094849})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8857595920562744})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.868728756904602})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8769, 'crossentropy': 0.767574853515625}
store['active_learning_steps'][67]['acquisition']={'indices': [2557, 42790, 10808, 19965, 12423], 'labels': [0, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7981505393981934})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8148137331008911})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8179337382316589})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8304997086524963})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8472, 'crossentropy': 0.83322001953125}
store['active_learning_steps'][68]['acquisition']={'indices': [47501, 58224, 48723, 55974, 28598], 'labels': [-1, 6, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8327529430389404})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8272231817245483})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8676308393478394})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8331573009490967})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0346839427947998})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8644, 'crossentropy': 0.830021484375}
store['active_learning_steps'][69]['acquisition']={'indices': [12507, 45712, 18706, 44219, 24068], 'labels': [5, 3, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7989808320999146})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7461023330688477})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.783602237701416})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8147854208946228})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8396615386009216})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8902, 'crossentropy': 0.7461201171875}
store['active_learning_steps'][70]['acquisition']={'indices': [33526, 20912, 5308, 46536, 44699], 'labels': [2, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7108017206192017})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7750742435455322})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8334188461303711})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8249393701553345})
store['active_learning_steps'][71]['training']['best_epoch']=1
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8665, 'crossentropy': 0.71446767578125}
store['active_learning_steps'][71]['acquisition']={'indices': [53576, 31658, 29527, 33706, 20645], 'labels': [-1, 2, 6, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7387034893035889})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7043907642364502})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8035556077957153})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8273069858551025})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8209248781204224})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.6786029296875}
store['active_learning_steps'][72]['acquisition']={'indices': [18876, 17964, 32804, 15715, 41196], 'labels': [-1, -1, -1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7429462671279907})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7817256450653076})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7464288473129272})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7257634997367859})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.74224454164505})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8153016567230225})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7993190288543701})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.67741640625}
store['active_learning_steps'][73]['acquisition']={'indices': [8537, 54525, 35215, 53877, 56590], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8065623044967651})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7437789440155029})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7981151342391968})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9000836610794067})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9340789318084717})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.738146044921875}
store['active_learning_steps'][74]['acquisition']={'indices': [57987, 6160, 25501, 30035, 2540], 'labels': [5, -1, -1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7837262749671936})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6779816150665283})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7276602983474731})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8248876929283142})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7921912670135498})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8955, 'crossentropy': 0.6508822265625}
store['active_learning_steps'][75]['acquisition']={'indices': [30109, 2260, 15899, 13572, 53858], 'labels': [-1, 1, 9, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7449084520339966})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7293174266815186})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7582603693008423})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8649618625640869})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8376486301422119})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8889, 'crossentropy': 0.71995419921875}
store['active_learning_steps'][76]['acquisition']={'indices': [3782, 29388, 52355, 21528, 49663], 'labels': [-1, 0, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8111858367919922})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7402713298797607})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7663412094116211})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7857981324195862})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7638989686965942})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8949, 'crossentropy': 0.696211767578125}
store['active_learning_steps'][77]['acquisition']={'indices': [396, 35911, 6397, 57990, 12388], 'labels': [5, 3, 7, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8425852656364441})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7939683198928833})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8211469650268555})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8575053811073303})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.938133716583252})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8869, 'crossentropy': 0.72984423828125}
store['active_learning_steps'][78]['acquisition']={'indices': [4418, 6432, 20736, 7247, 28065], 'labels': [-1, 7, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7472541928291321})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6373404264450073})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6898612380027771})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7104415893554688})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8675496578216553})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8905, 'crossentropy': 0.681616943359375}
store['active_learning_steps'][79]['acquisition']={'indices': [30731, 36053, 16406, 8836, 6864], 'labels': [-1, 4, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7869353890419006})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7073293924331665})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6949113607406616})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.703050434589386})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8119900226593018})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7481904029846191})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.732618505859375}
store['active_learning_steps'][80]['acquisition']={'indices': [46866, 42883, 21080, 11743, 27302], 'labels': [9, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8501884937286377})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7759079933166504})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8199067115783691})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8856230974197388})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8327937722206116})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8875, 'crossentropy': 0.736991748046875}
store['active_learning_steps'][81]['acquisition']={'indices': [41173, 54850, 13847, 54484, 15346], 'labels': [4, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7970088720321655})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7242422103881836})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8178659677505493})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8581027984619141})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7980965375900269})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8908, 'crossentropy': 0.689162744140625}
store['active_learning_steps'][82]['acquisition']={'indices': [30578, 55385, 694, 38683, 28124], 'labels': [0, 4, 8, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6907109618186951})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6893864274024963})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7473658323287964})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7075979113578796})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8428729772567749})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.63693916015625}
store['active_learning_steps'][83]['acquisition']={'indices': [15721, 53978, 35241, 26136, 30218], 'labels': [7, 5, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6870510578155518})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6525826454162598})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7076209783554077})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7023672461509705})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6949062347412109})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.8937, 'crossentropy': 0.662577392578125}
store['active_learning_steps'][84]['acquisition']={'indices': [49975, 14169, 59098, 51099, 46565], 'labels': [2, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8351829051971436})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6602303981781006})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7383691072463989})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6986333131790161})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.758057177066803})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8902, 'crossentropy': 0.666093408203125}
store['active_learning_steps'][85]['acquisition']={'indices': [5838, 51864, 12119, 31558, 9154], 'labels': [3, 8, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7794709205627441})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.682557225227356})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7308717370033264})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7811710834503174})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.855931282043457})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8926, 'crossentropy': 0.65563671875}
store['active_learning_steps'][86]['acquisition']={'indices': [7058, 54564, 48228, 30995, 14841], 'labels': [3, 8, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7322369813919067})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6096467971801758})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7138382196426392})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6645447015762329})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6789236068725586})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.604464990234375}
store['active_learning_steps'][87]['acquisition']={'indices': [55485, 7845, 47047, 37006, 10773], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7489310503005981})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.647066593170166})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6847562789916992})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7360180616378784})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7261031866073608})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9046, 'crossentropy': 0.600190869140625}
store['active_learning_steps'][88]['acquisition']={'indices': [16424, 18808, 3618, 9889, 8599], 'labels': [5, 5, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7330242395401001})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6597375869750977})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6620521545410156})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.713013231754303})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7310028076171875})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.62274072265625}
store['active_learning_steps'][89]['acquisition']={'indices': [53655, 28953, 30, 27580, 51044], 'labels': [-1, 3, -1, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.704257071018219})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6862072944641113})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6763036251068115})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7414634227752686})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7055906653404236})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7616905570030212})
store['active_learning_steps'][90]['training']['best_epoch']=3
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9075, 'crossentropy': 0.63287880859375}
store['active_learning_steps'][90]['acquisition']={'indices': [53177, 26433, 17952, 33792, 3209], 'labels': [-1, -1, 8, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7173446416854858})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6492148041725159})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6256837844848633})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6819360256195068})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7685720920562744})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8016738891601562})
store['active_learning_steps'][91]['training']['best_epoch']=3
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.641039990234375}
store['active_learning_steps'][91]['acquisition']={'indices': [40620, 10214, 21823, 26473, 20733], 'labels': [-1, 3, 7, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7091294527053833})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5996467471122742})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6348861455917358})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5999399423599243})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6975152492523193})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.601712060546875}
store['active_learning_steps'][92]['acquisition']={'indices': [49718, 58405, 53463, 14810, 42163], 'labels': [6, 8, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7656061053276062})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6702255010604858})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6951819658279419})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7604780197143555})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7683383822441101})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.645837841796875}
store['active_learning_steps'][93]['acquisition']={'indices': [35940, 12021, 55464, 488, 31155], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7596153616905212})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6396568417549133})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7294279336929321})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7567455172538757})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6903403997421265})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.63107158203125}
store['active_learning_steps'][94]['acquisition']={'indices': [4135, 46833, 45740, 48760, 728], 'labels': [4, 2, 4, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7033321857452393})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6761718988418579})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6717127561569214})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6580343246459961})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6791850328445435})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7504377365112305})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7490667104721069})
store['active_learning_steps'][95]['training']['best_epoch']=4
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.660966259765625}
store['active_learning_steps'][95]['acquisition']={'indices': [31280, 44816, 5113, 32540, 24622], 'labels': [-1, -1, 2, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7091516256332397})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.653477668762207})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6250936388969421})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6344833374023438})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7164928913116455})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7505850791931152})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.6060779296875}
store['active_learning_steps'][96]['acquisition']={'indices': [54630, 51080, 53818, 575, 13992], 'labels': [6, 7, 6, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6974880695343018})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.659706711769104})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.678238570690155})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6374033689498901})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6965423822402954})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7107659578323364})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7213828563690186})
store['active_learning_steps'][97]['training']['best_epoch']=4
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.64391630859375}
store['active_learning_steps'][97]['acquisition']={'indices': [45682, 31768, 2583, 40100, 42671], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6725515723228455})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6814490556716919})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6939029693603516})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7604013681411743})
store['active_learning_steps'][98]['training']['best_epoch']=1
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.674346435546875}
store['active_learning_steps'][98]['acquisition']={'indices': [20483, 3500, 46963, 23969, 53975], 'labels': [-1, -1, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6695464849472046})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7158300876617432})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6392556428909302})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6615005731582642})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6499384641647339})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6916254758834839})
store['active_learning_steps'][99]['training']['best_epoch']=3
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.593002685546875}
store['active_learning_steps'][99]['acquisition']={'indices': [11309, 2975, 21520, 49295, 20964], 'labels': [7, -1, 8, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7466546893119812})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6415971517562866})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6506891250610352})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6726530194282532})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.637946605682373})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7893683910369873})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7257065773010254})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7933342456817627})
store['active_learning_steps'][100]['training']['best_epoch']=5
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.641176416015625}
store['active_learning_steps'][100]['acquisition']={'indices': [51667, 1202, 43663, 9984, 54299], 'labels': [9, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7098489999771118})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6134086847305298})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6811250448226929})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7284146547317505})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6524133682250977})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.59350390625}
store['active_learning_steps'][101]['acquisition']={'indices': [30633, 20782, 47495, 51848, 8511], 'labels': [9, 6, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6783377528190613})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6508066654205322})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6636042594909668})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6933375597000122})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7557709217071533})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.8979, 'crossentropy': 0.615592919921875}
store['active_learning_steps'][102]['acquisition']={'indices': [15733, 15673, 26325, 53238, 19097], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7541354894638062})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6955010890960693})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6631805300712585})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7011395692825317})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.8213217258453369})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7694554924964905})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.5934373046875}
store['active_learning_steps'][103]['acquisition']={'indices': [51658, 12814, 31555, 46731, 28324], 'labels': [2, 3, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7123790383338928})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6585978269577026})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6824032664299011})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6328046917915344})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6902341842651367})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7242621183395386})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7903015613555908})
store['active_learning_steps'][104]['training']['best_epoch']=4
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.643956494140625}
store['active_learning_steps'][104]['acquisition']={'indices': [59672, 9104, 6314, 44484, 27713], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7277243137359619})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6018515825271606})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.615699052810669})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7145013809204102})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7376034259796143})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9074, 'crossentropy': 0.59729970703125}
store['active_learning_steps'][105]['acquisition']={'indices': [21023, 24610, 46734, 12120, 30174], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7134972810745239})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.591637372970581})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6192312836647034})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7298656702041626})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6768401265144348})
store['active_learning_steps'][106]['training']['best_epoch']=2
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.8973, 'crossentropy': 0.588797998046875}
store['active_learning_steps'][106]['acquisition']={'indices': [39045, 13776, 11756, 54785, 21831], 'labels': [6, 7, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6742348670959473})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6826096773147583})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6939904689788818})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7053306102752686})
store['active_learning_steps'][107]['training']['best_epoch']=1
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.8728, 'crossentropy': 0.6679599609375}
store['active_learning_steps'][107]['acquisition']={'indices': [26707, 43407, 48831, 28754, 20162], 'labels': [7, 2, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6991217732429504})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5827926397323608})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6067259311676025})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6270356774330139})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6380193829536438})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.5497341796875}
store['active_learning_steps'][108]['acquisition']={'indices': [32460, 18934, 38255, 9601, 29127], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7011284828186035})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6035067439079285})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5892053842544556})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6637709140777588})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6880619525909424})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6105482578277588})
store['active_learning_steps'][109]['training']['best_epoch']=3
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.550023046875}
store['active_learning_steps'][109]['acquisition']={'indices': [12777, 30183, 50661, 15491, 52639], 'labels': [-1, -1, -1, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.780104398727417})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5605995655059814})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6476305723190308})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6183189749717712})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6365315914154053})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.55199541015625}
store['active_learning_steps'][110]['acquisition']={'indices': [3694, 4379, 28464, 47524, 23478], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7336789965629578})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6381409168243408})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6730022430419922})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6484477519989014})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7284231185913086})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.572133837890625}
store['active_learning_steps'][111]['acquisition']={'indices': [12570, 51680, 1792, 47311, 59567], 'labels': [9, -1, -1, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7265052795410156})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6571526527404785})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6509166955947876})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6084007024765015})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6404153108596802})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6990557312965393})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7707030773162842})
store['active_learning_steps'][112]['training']['best_epoch']=4
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.60235302734375}
store['active_learning_steps'][112]['acquisition']={'indices': [35923, 2158, 47033, 10516, 35395], 'labels': [-1, 6, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7896476984024048})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6088515520095825})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.660435676574707})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6392463445663452})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7033883333206177})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.5654453125}
store['active_learning_steps'][113]['acquisition']={'indices': [42711, 36012, 7215, 26238, 10771], 'labels': [-1, -1, 8, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7226320505142212})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6658159494400024})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6821523308753967})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7091481685638428})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6884706020355225})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.63739921875}
store['active_learning_steps'][114]['acquisition']={'indices': [47938, 23318, 36120, 54280, 39051], 'labels': [5, 1, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7701195478439331})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6395741701126099})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6309046745300293})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.640236496925354})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.693869411945343})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.703827977180481})
store['active_learning_steps'][115]['training']['best_epoch']=3
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.602094775390625}
store['active_learning_steps'][115]['acquisition']={'indices': [33172, 44973, 31570, 54123, 36311], 'labels': [-1, -1, 1, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6918962001800537})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6445530652999878})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6045200824737549})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6477999687194824})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7444783449172974})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7530567049980164})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.585231787109375}
store['active_learning_steps'][116]['acquisition']={'indices': [18405, 59154, 3130, 30719, 5473], 'labels': [9, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.705623984336853})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6994081139564514})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6347589492797852})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6053621768951416})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6671709418296814})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6649112701416016})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7482542991638184})
store['active_learning_steps'][117]['training']['best_epoch']=4
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.60236474609375}
store['active_learning_steps'][117]['acquisition']={'indices': [19261, 50162, 1542, 37104, 44513], 'labels': [0, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7166590094566345})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5936229228973389})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6314307451248169})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6299040913581848})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6685984134674072})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.55339814453125}
store['active_learning_steps'][118]['acquisition']={'indices': [44627, 31212, 1379, 40017, 28981], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7222204208374023})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6507394313812256})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6223858594894409})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5954260230064392})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6141122579574585})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6513484120368958})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6749399900436401})
store['active_learning_steps'][119]['training']['best_epoch']=4
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.533331298828125}
store['active_learning_steps'][119]['acquisition']={'indices': [19019, 42060, 9453, 45714, 7700], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7458405494689941})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6444343328475952})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7654112577438354})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.605945348739624})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6332911252975464})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7093269228935242})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7407773733139038})
store['active_learning_steps'][120]['training']['best_epoch']=4
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.58454912109375}
store['active_learning_steps'][120]['acquisition']={'indices': [36272, 6995, 10605, 20878, 43728], 'labels': [-1, 4, 3, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7044517993927002})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5880880355834961})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.576961874961853})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6023410558700562})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6019083261489868})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6824766993522644})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.5579095703125}
store['active_learning_steps'][121]['acquisition']={'indices': [15055, 7115, 20000, 24770, 47983], 'labels': [2, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7753136157989502})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.678591251373291})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6368612051010132})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7301650643348694})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6406129598617554})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.73222815990448})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.612392919921875}
store['active_learning_steps'][122]['acquisition']={'indices': [21135, 17209, 13537, 13216, 49976], 'labels': [2, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6767578125})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6041266918182373})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6485517024993896})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6291850805282593})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6496224403381348})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.566997509765625}
store['active_learning_steps'][123]['acquisition']={'indices': [22864, 50972, 5842, 53724, 45305], 'labels': [-1, 7, 1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.678604006767273})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6194074749946594})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6313349008560181})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6654430627822876})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.623942494392395})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.904, 'crossentropy': 0.575012646484375}
store['active_learning_steps'][124]['acquisition']={'indices': [38140, 35239, 17542, 4727, 18264], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7984880208969116})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6282674074172974})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6232600808143616})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6615936756134033})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7377115488052368})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6832781434059143})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.59431474609375}
store['active_learning_steps'][125]['acquisition']={'indices': [47333, 59115, 8736, 33792, 54123], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7206041812896729})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5590263605117798})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.623561441898346})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6574227213859558})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6767565011978149})
store['active_learning_steps'][126]['training']['best_epoch']=2
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.55586923828125}
store['active_learning_steps'][126]['acquisition']={'indices': [53684, 14680, 12740, 77, 52060], 'labels': [-1, -1, 2, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.689031720161438})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6452435255050659})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.633873462677002})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6169022917747498})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7745378613471985})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7029488682746887})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7370316982269287})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.53528173828125}
store['active_learning_steps'][127]['acquisition']={'indices': [21459, 28344, 23842, 54049, 33157], 'labels': [7, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6883972883224487})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5699061155319214})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6064596176147461})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6764098405838013})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6261134743690491})
store['active_learning_steps'][128]['training']['best_epoch']=2
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.5480326171875}
store['active_learning_steps'][128]['acquisition']={'indices': [59473, 58595, 40839, 15177, 17939], 'labels': [5, -1, 9, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6596275568008423})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6326301097869873})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6468967199325562})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6435517072677612})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7642355561256409})
store['active_learning_steps'][129]['training']['best_epoch']=2
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.588907958984375}
store['active_learning_steps'][129]['acquisition']={'indices': [37948, 17692, 4886, 8946, 26237], 'labels': [-1, 9, 6, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6729720830917358})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5912033319473267})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6188184022903442})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.635903000831604})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6183704733848572})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.56226875}
store['active_learning_steps'][130]['acquisition']={'indices': [8318, 539, 3536, 56176, 997], 'labels': [9, 8, 2, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7023656964302063})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6703909039497375})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6137133240699768})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7604724168777466})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.750568687915802})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7497295141220093})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.5907109375}
store['active_learning_steps'][131]['acquisition']={'indices': [21124, 45877, 31775, 10417, 45416], 'labels': [-1, 8, 3, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6548567414283752})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6370554566383362})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6179482936859131})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6764049530029297})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6801699995994568})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7497268915176392})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.55529580078125}
store['active_learning_steps'][132]['acquisition']={'indices': [29794, 20810, 39828, 35712, 16120], 'labels': [-1, -1, 1, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6693623065948486})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6016006469726562})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.624222457408905})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6042172908782959})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6735614538192749})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.558738818359375}
store['active_learning_steps'][133]['acquisition']={'indices': [50851, 58616, 51792, 53579, 59285], 'labels': [9, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6952806711196899})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5976811647415161})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5988456606864929})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6249315738677979})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6839069128036499})
store['active_learning_steps'][134]['training']['best_epoch']=2
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.5687220703125}
store['active_learning_steps'][134]['acquisition']={'indices': [49580, 57398, 15085, 24225, 15737], 'labels': [2, 2, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6983808279037476})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6097004413604736})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.591881513595581})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.600605845451355})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6184249520301819})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6315701007843018})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.543991650390625}
store['active_learning_steps'][135]['acquisition']={'indices': [7129, 21921, 43863, 7842, 4032], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7282403707504272})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6376008987426758})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6575565338134766})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7199040651321411})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6745095252990723})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.55880029296875}
store['active_learning_steps'][136]['acquisition']={'indices': [25351, 25571, 15289, 6216, 730], 'labels': [-1, 2, 8, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6774770021438599})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6058844327926636})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6029865741729736})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.600297212600708})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6513006091117859})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6018052101135254})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.600857138633728})
store['active_learning_steps'][137]['training']['best_epoch']=4
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.576174658203125}
store['active_learning_steps'][137]['acquisition']={'indices': [52501, 35859, 471, 16038, 50989], 'labels': [2, 3, 9, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6124115586280823})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.572041928768158})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5693105459213257})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.558742880821228})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.655931830406189})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5637303590774536})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6331830024719238})
store['active_learning_steps'][138]['training']['best_epoch']=4
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.503170703125}
store['active_learning_steps'][138]['acquisition']={'indices': [22039, 49810, 30677, 40144, 44402], 'labels': [-1, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6405993700027466})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6136438846588135})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6162087917327881})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.587756335735321})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6238030195236206})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6347374320030212})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6398063898086548})
store['active_learning_steps'][139]['training']['best_epoch']=4
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9262, 'crossentropy': 0.53447333984375}
store['active_learning_steps'][139]['acquisition']={'indices': [10652, 9245, 315, 13087, 56591], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7770425081253052})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.591385006904602})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6182806491851807})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6119088530540466})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6738032102584839})
store['active_learning_steps'][140]['training']['best_epoch']=2
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.533080859375}
store['active_learning_steps'][140]['acquisition']={'indices': [15468, 20380, 53233, 12776, 11143], 'labels': [7, 7, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7340830564498901})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5626627802848816})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6192643642425537})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6345754265785217})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6264553070068359})
store['active_learning_steps'][141]['training']['best_epoch']=2
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.53182939453125}
store['active_learning_steps'][141]['acquisition']={'indices': [51759, 29333, 19350, 6857, 14777], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6927807331085205})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5601393580436707})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5703525543212891})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6126489043235779})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6780720353126526})
store['active_learning_steps'][142]['training']['best_epoch']=2
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.53849013671875}
store['active_learning_steps'][142]['acquisition']={'indices': [47221, 39018, 3425, 35838, 34303], 'labels': [7, 1, -1, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6548749208450317})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5732547044754028})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5740699768066406})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5648378133773804})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6539418697357178})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5944143533706665})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7077355980873108})
store['active_learning_steps'][143]['training']['best_epoch']=4
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.5245576171875}
store['active_learning_steps'][143]['acquisition']={'indices': [59951, 25907, 25023, 21181, 41775], 'labels': [4, 2, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6584962606430054})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6026513576507568})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5842098593711853})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5856363773345947})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.612237811088562})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6196300387382507})
store['active_learning_steps'][144]['training']['best_epoch']=3
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.51332841796875}
store['active_learning_steps'][144]['acquisition']={'indices': [33578, 48843, 39459, 59584, 13022], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7059118151664734})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5926337838172913})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5677399039268494})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6286602020263672})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6162530183792114})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6550236940383911})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.5092890625}
store['active_learning_steps'][145]['acquisition']={'indices': [43388, 39563, 3637, 18100, 43102], 'labels': [8, 4, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6912156939506531})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6564178466796875})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5694320201873779})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6381570100784302})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6619451642036438})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6458483934402466})
store['active_learning_steps'][146]['training']['best_epoch']=3
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.510464599609375}
store['active_learning_steps'][146]['acquisition']={'indices': [30159, 6672, 42901, 40169, 49345], 'labels': [-1, 4, -1, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6769428849220276})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.622483491897583})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6425881385803223})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6097878813743591})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6270381212234497})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6700760126113892})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6674993634223938})
store['active_learning_steps'][147]['training']['best_epoch']=4
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.544443798828125}
store['active_learning_steps'][147]['acquisition']={'indices': [11333, 16110, 15395, 5132, 21388], 'labels': [9, -1, 9, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7166557312011719})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5894675850868225})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5805666446685791})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5877317190170288})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7178686261177063})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6268842816352844})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.5552314453125}
store['active_learning_steps'][148]['acquisition']={'indices': [43201, 33897, 58219, 59738, 14016], 'labels': [8, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.665733814239502})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5794891119003296})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5409002304077148})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6162662506103516})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.610556960105896})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5750664472579956})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.48325673828125}
store['active_learning_steps'][149]['acquisition']={'indices': [38959, 1617, 47501, 38851, 37141], 'labels': [-1, 6, 1, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7128838300704956})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5598657131195068})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5126201510429382})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6096205115318298})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5737636685371399})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6309590339660645})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.5032671875}
store['active_learning_steps'][150]['acquisition']={'indices': [52906, 40951, 31007, 25410, 54297], 'labels': [-1, 2, 5, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6356756687164307})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5845975875854492})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6869499683380127})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5642163753509521})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6223945617675781})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.663374662399292})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6719496250152588})
store['active_learning_steps'][151]['training']['best_epoch']=4
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.4937154296875}
store['active_learning_steps'][151]['acquisition']={'indices': [56401, 10916, 23344, 17657, 14855], 'labels': [9, 0, 3, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6718909740447998})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5610888004302979})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.526281476020813})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6113991141319275})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5690218210220337})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5807846784591675})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.51340263671875}
store['active_learning_steps'][152]['acquisition']={'indices': [23476, 24772, 45588, 10497, 17359], 'labels': [6, 3, 1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7180298566818237})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5409263968467712})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5257283449172974})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5811804533004761})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5732911825180054})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6033003330230713})
store['active_learning_steps'][153]['training']['best_epoch']=3
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.519517138671875}
store['active_learning_steps'][153]['acquisition']={'indices': [39799, 37393, 6923, 33251, 33728], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7463283538818359})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6057004928588867})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5595636367797852})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.56450355052948})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5932755470275879})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6468753814697266})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.529856640625}
store['active_learning_steps'][154]['acquisition']={'indices': [19875, 51912, 25490, 42048, 27273], 'labels': [4, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6585177183151245})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5840803980827332})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5642555952072144})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5912628173828125})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.583859920501709})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6224388480186462})
store['active_learning_steps'][155]['training']['best_epoch']=3
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.5316369140625}
store['active_learning_steps'][155]['acquisition']={'indices': [21948, 56078, 56487, 46654, 27395], 'labels': [-1, -1, 9, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7146583795547485})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5626220703125})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5597736239433289})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6164625883102417})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6396034955978394})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6585561037063599})
store['active_learning_steps'][156]['training']['best_epoch']=3
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.507419677734375}
store['active_learning_steps'][156]['acquisition']={'indices': [51994, 44714, 45362, 59847, 56267], 'labels': [5, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6671836972236633})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.568189263343811})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5577725172042847})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5847845077514648})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6103287935256958})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6560722589492798})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.48090966796875}
store['active_learning_steps'][157]['acquisition']={'indices': [59054, 27211, 41333, 37385, 29439], 'labels': [3, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6887738704681396})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6366749405860901})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6337112188339233})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6223370432853699})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6289573907852173})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.622673511505127})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6305152177810669})
store['active_learning_steps'][158]['training']['best_epoch']=4
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9206, 'crossentropy': 0.55268212890625}
store['active_learning_steps'][158]['acquisition']={'indices': [8877, 920, 28612, 28842, 47304], 'labels': [0, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6765722036361694})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5389273762702942})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5848637819290161})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5376359224319458})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7051714062690735})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5978183746337891})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6298891305923462})
store['active_learning_steps'][159]['training']['best_epoch']=4
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.47920859375}
store['active_learning_steps'][159]['acquisition']={'indices': [54367, 25237, 46474, 23855, 22028], 'labels': [-1, -1, 9, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6538597345352173})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5908901691436768})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5608357787132263})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5782945156097412})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6685572862625122})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6489638090133667})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.493326904296875}
store['active_learning_steps'][160]['acquisition']={'indices': [17846, 33756, 22182, 52442, 13184], 'labels': [-1, 9, 3, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6943294405937195})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5128414630889893})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5224485397338867})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4892699718475342})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6099165678024292})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5131477117538452})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5535407066345215})
store['active_learning_steps'][161]['training']['best_epoch']=4
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.485647802734375}
store['active_learning_steps'][161]['acquisition']={'indices': [50475, 2653, 10904, 42366, 22104], 'labels': [-1, 7, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.666535496711731})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.554664671421051})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6044223308563232})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5694755911827087})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5497977137565613})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6226586103439331})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6008884906768799})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6323223114013672})
store['active_learning_steps'][162]['training']['best_epoch']=5
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.4961556640625}
store['active_learning_steps'][162]['acquisition']={'indices': [49799, 48769, 38241, 54402, 44665], 'labels': [7, -1, 3, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6841365098953247})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5593149065971375})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5535664558410645})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5675033926963806})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5906550884246826})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5683879852294922})
store['active_learning_steps'][163]['training']['best_epoch']=3
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.49480146484375}
store['active_learning_steps'][163]['acquisition']={'indices': [44822, 12407, 22932, 19377, 34688], 'labels': [-1, 1, 0, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6886757612228394})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6634749174118042})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5760809183120728})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5780828595161438})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5097720623016357})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5897477269172668})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6510573625564575})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6436747312545776})
store['active_learning_steps'][164]['training']['best_epoch']=5
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9322, 'crossentropy': 0.472799462890625}
store['active_learning_steps'][164]['acquisition']={'indices': [28402, 44787, 10582, 701, 33764], 'labels': [0, -1, 2, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6937591433525085})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5651043653488159})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5560228228569031})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4942685663700104})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5846564769744873})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5946433544158936})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.59232497215271})
store['active_learning_steps'][165]['training']['best_epoch']=4
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.47176396484375}
store['active_learning_steps'][165]['acquisition']={'indices': [34395, 12723, 56709, 25236, 295], 'labels': [-1, 0, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6886757016181946})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.622473418712616})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5505461692810059})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5534399151802063})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5819544792175293})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5902267098426819})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9285, 'crossentropy': 0.47004482421875}
store['active_learning_steps'][166]['acquisition']={'indices': [52542, 7441, 29076, 37139, 6339], 'labels': [6, 8, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7014334201812744})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.567345142364502})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5490859150886536})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5601582527160645})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5883864164352417})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.531617283821106})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5668255090713501})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5415797829627991})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5943901538848877})
store['active_learning_steps'][167]['training']['best_epoch']=6
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9353, 'crossentropy': 0.505966455078125}
store['active_learning_steps'][167]['acquisition']={'indices': [4385, 46569, 8097, 8630, 32972], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6485013365745544})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5646255016326904})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5637500882148743})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5065075159072876})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5808782577514648})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5632501840591431})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6062889099121094})
store['active_learning_steps'][168]['training']['best_epoch']=4
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.470949462890625}
store['active_learning_steps'][168]['acquisition']={'indices': [31686, 24346, 52871, 31409, 33720], 'labels': [-1, 0, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6749114990234375})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5440171957015991})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5201199054718018})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5160250663757324})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5861341953277588})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.556404709815979})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5678977966308594})
store['active_learning_steps'][169]['training']['best_epoch']=4
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9344, 'crossentropy': 0.45086318359375}
store['active_learning_steps'][169]['acquisition']={'indices': [29892, 21703, 58153, 11824, 1727], 'labels': [5, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6747434139251709})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5740269422531128})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5095615386962891})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5314317941665649})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5179624557495117})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5325839519500732})
store['active_learning_steps'][170]['training']['best_epoch']=3
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.4543412109375}
store['active_learning_steps'][170]['acquisition']={'indices': [42539, 29619, 39015, 1786, 20941], 'labels': [-1, 2, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6515844464302063})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4803890585899353})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4745995104312897})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5049077868461609})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5050036907196045})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5163583159446716})
store['active_learning_steps'][171]['training']['best_epoch']=3
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.447392529296875}
store['active_learning_steps'][171]['acquisition']={'indices': [44172, 39366, 29227, 2527, 262], 'labels': [8, 3, 1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6525964736938477})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5349485278129578})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4736728370189667})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4950658082962036})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5060234069824219})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49344581365585327})
store['active_learning_steps'][172]['training']['best_epoch']=3
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.426270068359375}
store['active_learning_steps'][172]['acquisition']={'indices': [38975, 55165, 9, 47456, 51870], 'labels': [1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6709734201431274})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5329906940460205})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.554500937461853})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5548520088195801})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49764567613601685})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5760181546211243})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5260286331176758})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5154999494552612})
store['active_learning_steps'][173]['training']['best_epoch']=5
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.450327099609375}
store['active_learning_steps'][173]['acquisition']={'indices': [27565, 53438, 48643, 34166, 29335], 'labels': [9, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6778342723846436})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5341485738754272})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5226907730102539})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4931562840938568})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5613058805465698})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5569635033607483})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6123802661895752})
store['active_learning_steps'][174]['training']['best_epoch']=4
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.459095166015625}
store['active_learning_steps'][174]['acquisition']={'indices': [40962, 28508, 37631, 24924, 51456], 'labels': [-1, 6, 2, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6887354850769043})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5569925308227539})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5443192720413208})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.514075517654419})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.558493971824646})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5522677898406982})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5376488566398621})
store['active_learning_steps'][175]['training']['best_epoch']=4
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.445190966796875}
store['active_learning_steps'][175]['acquisition']={'indices': [30989, 44812, 38520, 28956, 46993], 'labels': [-1, 8, 3, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][176]['training']={}
store['active_learning_steps'][176]['training']['epochs']=[]
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.639218807220459})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5417034029960632})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5039774775505066})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4813346266746521})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5173780918121338})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48361510038375854})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6003979444503784})
store['active_learning_steps'][176]['training']['best_epoch']=4
store['active_learning_steps'][176]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.4351412109375}
