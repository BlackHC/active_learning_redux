store = {}
store['timestamp']=1620299239
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=31']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=31
store['worker_id']=31
store['num_workers']=40
store['config']={'seed': 42, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
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
store['active_learning_steps'][0]['acquisition']={'indices': [54579, 46800, 28350, 58654, 43078], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.346231460571289})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3795835971832275})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.991476535797119})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9502713680267334})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6893, 'crossentropy': 1.916367578125}
store['active_learning_steps'][1]['acquisition']={'indices': [37038, 54598, 37141, 50306, 22267], 'labels': [-1, 5, -1, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4546091556549072})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.685300350189209})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.44996976852417})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.814579963684082})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6805, 'crossentropy': 2.083644140625}
store['active_learning_steps'][2]['acquisition']={'indices': [22058, 40984, 2157, 6714, 13971], 'labels': [3, 9, 4, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8988796472549438})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4500784873962402})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.79679536819458})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.5125536918640137})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7178, 'crossentropy': 1.7555140625}
store['active_learning_steps'][3]['acquisition']={'indices': [53398, 15373, 6368, 1874, 35312], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0999176502227783})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.592585325241089})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.7721071243286133})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.877413511276245})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6994, 'crossentropy': 1.8821875}
store['active_learning_steps'][4]['acquisition']={'indices': [4983, 17735, 18167, 17070, 4231], 'labels': [9, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.9850459098815918})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.2156789302825928})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.369809627532959})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.738154411315918})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.705, 'crossentropy': 1.79625390625}
store['active_learning_steps'][5]['acquisition']={'indices': [59433, 49434, 8574, 31204, 47705], 'labels': [0, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.131767749786377})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.306708335876465})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.4467382431030273})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.5010929107666016})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7175, 'crossentropy': 1.73068203125}
store['active_learning_steps'][6]['acquisition']={'indices': [31297, 18456, 30505, 50147, 4677], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.6304973363876343})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.9864492416381836})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.0184221267700195})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.0049362182617188})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7507, 'crossentropy': 1.54159990234375}
store['active_learning_steps'][7]['acquisition']={'indices': [29304, 30261, 47478, 15026, 10312], 'labels': [3, -1, 8, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6702632904052734})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.200216770172119})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.6638269424438477})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4543755054473877})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7399, 'crossentropy': 1.5545576171875}
store['active_learning_steps'][8]['acquisition']={'indices': [44181, 10120, 29292, 16840, 40640], 'labels': [-1, -1, 9, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.608180284500122})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.9508967399597168})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.3788204193115234})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.538745641708374})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7407, 'crossentropy': 1.4204490234375}
store['active_learning_steps'][9]['acquisition']={'indices': [36403, 27186, 16172, 53955, 9548], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8583149909973145})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.222203016281128})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.1709954738616943})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.9477972984313965})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.72, 'crossentropy': 1.60201767578125}
store['active_learning_steps'][10]['acquisition']={'indices': [41528, 1090, 50780, 59449, 37982], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.6030099391937256})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.125063180923462})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.2476181983947754})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.361699342727661})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7425, 'crossentropy': 1.5135744140625}
store['active_learning_steps'][11]['acquisition']={'indices': [16678, 56340, 42643, 9377, 3915], 'labels': [-1, 2, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8260284662246704})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3360514640808105})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.435368537902832})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.852997303009033})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7079, 'crossentropy': 1.69583203125}
store['active_learning_steps'][12]['acquisition']={'indices': [55751, 2664, 9640, 39336, 5938], 'labels': [3, 2, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.507028579711914})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.9019438028335571})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.0601091384887695})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.132382392883301})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7617, 'crossentropy': 1.36267412109375}
store['active_learning_steps'][13]['acquisition']={'indices': [43857, 38548, 54847, 34063, 13682], 'labels': [6, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.6086889505386353})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.9678704738616943})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.0992586612701416})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.0547142028808594})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7665, 'crossentropy': 1.40010087890625}
store['active_learning_steps'][14]['acquisition']={'indices': [31360, 50023, 37579, 26252, 1377], 'labels': [-1, 1, 1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5437272787094116})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.550126314163208})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7225635051727295})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.743836522102356})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7328, 'crossentropy': 1.4382146484375}
store['active_learning_steps'][15]['acquisition']={'indices': [35967, 14225, 30241, 16990, 47178], 'labels': [8, 8, 3, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2419748306274414})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.471370816230774})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.6076984405517578})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.8371645212173462})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7906, 'crossentropy': 1.17237158203125}
store['active_learning_steps'][16]['acquisition']={'indices': [30045, 34339, 51585, 59715, 32109], 'labels': [-1, -1, 0, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3695143461227417})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4588496685028076})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.7822613716125488})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.8255901336669922})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.771, 'crossentropy': 1.27457490234375}
store['active_learning_steps'][17]['acquisition']={'indices': [30783, 1713, 54474, 28358, 8011], 'labels': [9, 8, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.37214994430542})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.552903413772583})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.8523097038269043})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6684095859527588})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7757, 'crossentropy': 1.32880283203125}
store['active_learning_steps'][18]['acquisition']={'indices': [33624, 20708, 45648, 22194, 14237], 'labels': [-1, 3, -1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2817437648773193})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.605342149734497})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.9547538757324219})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.678422451019287})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7828, 'crossentropy': 1.269180078125}
store['active_learning_steps'][19]['acquisition']={'indices': [51666, 58147, 55123, 2953, 59268], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.4609136581420898})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.653851866722107})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.8468254804611206})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 2.1313815116882324})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7769, 'crossentropy': 1.30680029296875}
store['active_learning_steps'][20]['acquisition']={'indices': [3907, 27472, 54947, 65, 28900], 'labels': [5, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2819390296936035})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.4800527095794678})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.7637109756469727})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.8633813858032227})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7959, 'crossentropy': 1.1275109375}
store['active_learning_steps'][21]['acquisition']={'indices': [37369, 15567, 32060, 10015, 58196], 'labels': [9, 0, -1, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1972384452819824})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.502933382987976})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.849320888519287})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.6421598196029663})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7958, 'crossentropy': 1.09337294921875}
store['active_learning_steps'][22]['acquisition']={'indices': [12548, 1108, 31259, 17997, 23202], 'labels': [-1, -1, 8, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.196962833404541})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.511045217514038})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5278747081756592})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4609973430633545})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7967, 'crossentropy': 1.120879296875}
store['active_learning_steps'][23]['acquisition']={'indices': [57864, 30295, 28983, 58248, 22774], 'labels': [-1, 6, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0980370044708252})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.397200584411621})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6034541130065918})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.53428053855896})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.815, 'crossentropy': 1.05022578125}
store['active_learning_steps'][24]['acquisition']={'indices': [39041, 50132, 56449, 32286, 26311], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1729989051818848})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3009657859802246})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.4632916450500488})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.6117815971374512})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7979, 'crossentropy': 1.0600671875}
store['active_learning_steps'][25]['acquisition']={'indices': [30275, 36447, 26150, 28428, 39014], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.3417960405349731})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3921250104904175})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.56195867061615})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.66206693649292})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7879, 'crossentropy': 1.22312099609375}
store['active_learning_steps'][26]['acquisition']={'indices': [1889, 23533, 13709, 4893, 37909], 'labels': [6, 6, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1366772651672363})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3423681259155273})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.474744200706482})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.6281741857528687})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8031, 'crossentropy': 1.08567744140625}
store['active_learning_steps'][27]['acquisition']={'indices': [18977, 43651, 37049, 31797, 15128], 'labels': [-1, 5, -1, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9787725210189819})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.272273302078247})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2339179515838623})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.4208636283874512})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8173, 'crossentropy': 0.99101015625}
store['active_learning_steps'][28]['acquisition']={'indices': [38832, 36934, 7634, 7095, 51018], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2254443168640137})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.215340256690979})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.4896185398101807})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.5491046905517578})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4373128414154053})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8212, 'crossentropy': 1.16237646484375}
store['active_learning_steps'][29]['acquisition']={'indices': [54528, 22987, 6199, 14050, 34517], 'labels': [5, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1062450408935547})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1889872550964355})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3235342502593994})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.3207612037658691})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8241, 'crossentropy': 1.05119638671875}
store['active_learning_steps'][30]['acquisition']={'indices': [20683, 30965, 49757, 11091, 4440], 'labels': [9, 0, 2, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.086400032043457})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2785711288452148})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3441627025604248})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5653742551803589})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8071, 'crossentropy': 1.0490841796875}
store['active_learning_steps'][31]['acquisition']={'indices': [22937, 55663, 34154, 40274, 33378], 'labels': [-1, -1, 8, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9836629033088684})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0794864892959595})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4075119495391846})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3220990896224976})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8267, 'crossentropy': 0.937750390625}
store['active_learning_steps'][32]['acquisition']={'indices': [25545, 45219, 16092, 1480, 11903], 'labels': [-1, 4, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.1605191230773926})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1416676044464111})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.5016474723815918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.5280115604400635})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.4412105083465576})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8356, 'crossentropy': 1.0952916015625}
store['active_learning_steps'][33]['acquisition']={'indices': [52819, 12741, 55496, 1968, 33844], 'labels': [1, 0, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.135488510131836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1614656448364258})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4116911888122559})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.267147183418274})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8001, 'crossentropy': 1.02098388671875}
store['active_learning_steps'][34]['acquisition']={'indices': [44886, 54795, 55526, 48376, 28393], 'labels': [1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.15358304977417})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3092178106307983})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4065675735473633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5289044380187988})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7904, 'crossentropy': 1.13987646484375}
store['active_learning_steps'][35]['acquisition']={'indices': [12204, 28902, 56799, 51298, 49214], 'labels': [2, 8, 4, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0232943296432495})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1138594150543213})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.161893606185913})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.34511137008667})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.815, 'crossentropy': 0.97312763671875}
store['active_learning_steps'][36]['acquisition']={'indices': [34005, 44522, 43787, 19133, 37186], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0617060661315918})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2396612167358398})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2540783882141113})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3678579330444336})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8217, 'crossentropy': 0.975176171875}
store['active_learning_steps'][37]['acquisition']={'indices': [32549, 39072, 50689, 25397, 23405], 'labels': [6, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9962745308876038})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2468725442886353})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2278130054473877})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.316594123840332})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8281, 'crossentropy': 0.90602822265625}
store['active_learning_steps'][38]['acquisition']={'indices': [6179, 54903, 48218, 1515, 13430], 'labels': [-1, -1, -1, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0085519552230835})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2674667835235596})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4253859519958496})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.3829190731048584})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8192, 'crossentropy': 0.98418076171875}
store['active_learning_steps'][39]['acquisition']={'indices': [28704, 45320, 40122, 8600, 48195], 'labels': [6, -1, -1, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0815577507019043})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0983068943023682})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.14019775390625})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3273537158966064})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.816, 'crossentropy': 0.9945173828125}
store['active_learning_steps'][40]['acquisition']={'indices': [14118, 18514, 29618, 14846, 2590], 'labels': [2, 2, 8, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9357649087905884})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9537680745124817})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9766964316368103})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.022343397140503})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8327, 'crossentropy': 0.86337314453125}
store['active_learning_steps'][41]['acquisition']={'indices': [23782, 28310, 11976, 8924, 16547], 'labels': [7, 4, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8721873164176941})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9626114964485168})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.015726923942566})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0757112503051758})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8389, 'crossentropy': 0.83285380859375}
store['active_learning_steps'][42]['acquisition']={'indices': [47896, 46685, 24194, 18314, 47886], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9767708778381348})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0399541854858398})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2905807495117188})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2650049924850464})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8264, 'crossentropy': 0.95300390625}
store['active_learning_steps'][43]['acquisition']={'indices': [23726, 18336, 17148, 9773, 21971], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8389970660209656})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8835617303848267})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9210044741630554})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0265089273452759})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8392, 'crossentropy': 0.801566748046875}
store['active_learning_steps'][44]['acquisition']={'indices': [55018, 7202, 49063, 29889, 20108], 'labels': [6, 6, 7, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8948861360549927})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9416237473487854})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9953494668006897})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0504891872406006})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8324, 'crossentropy': 0.87825849609375}
store['active_learning_steps'][45]['acquisition']={'indices': [52598, 21904, 51501, 29575, 57702], 'labels': [-1, 7, 8, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9434710741043091})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8758529424667358})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9282002449035645})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0450084209442139})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.263176441192627})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8631, 'crossentropy': 0.8306845703125}
store['active_learning_steps'][46]['acquisition']={'indices': [24753, 36166, 25175, 44786, 13707], 'labels': [-1, -1, 4, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8391573429107666})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9892621040344238})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9375578165054321})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.108794927597046})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8495, 'crossentropy': 0.763890087890625}
store['active_learning_steps'][47]['acquisition']={'indices': [12416, 11672, 33367, 5804, 635], 'labels': [3, 8, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8021100759506226})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8965309262275696})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0764336585998535})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9836448431015015})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8508, 'crossentropy': 0.751281689453125}
store['active_learning_steps'][48]['acquisition']={'indices': [44421, 29429, 44637, 46185, 55781], 'labels': [9, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8188557624816895})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8575659990310669})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9697548151016235})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.989943265914917})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.833, 'crossentropy': 0.7957810546875}
store['active_learning_steps'][49]['acquisition']={'indices': [43458, 53504, 38584, 36149, 39283], 'labels': [1, 2, -1, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8731189370155334})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9728583097457886})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9225123524665833})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.946926474571228})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8493, 'crossentropy': 0.80900439453125}
store['active_learning_steps'][50]['acquisition']={'indices': [55255, 10986, 58063, 54186, 22389], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8744574785232544})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8645070791244507})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8782827854156494})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9836760759353638})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0570175647735596})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8712, 'crossentropy': 0.7954478515625}
store['active_learning_steps'][51]['acquisition']={'indices': [10821, 39161, 19869, 8883, 22483], 'labels': [-1, -1, 7, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9338554739952087})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9263943433761597})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0705132484436035})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1061351299285889})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1720242500305176})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8528, 'crossentropy': 0.94674755859375}
store['active_learning_steps'][52]['acquisition']={'indices': [14524, 34892, 51810, 33021, 26829], 'labels': [6, 9, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9243055582046509})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8612834215164185})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9185352921485901})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9573281407356262})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.023797631263733})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8706, 'crossentropy': 0.8368748046875}
store['active_learning_steps'][53]['acquisition']={'indices': [35972, 17741, 19785, 32154, 48094], 'labels': [-1, -1, 9, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7918437123298645})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8690671920776367})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8809183835983276})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0198910236358643})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8648, 'crossentropy': 0.7684970703125}
store['active_learning_steps'][54]['acquisition']={'indices': [3406, 38230, 41903, 28444, 35828], 'labels': [1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7898812294006348})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8224645853042603})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9408261775970459})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9884505271911621})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8611, 'crossentropy': 0.734736572265625}
store['active_learning_steps'][55]['acquisition']={'indices': [48264, 48994, 7991, 15700, 31311], 'labels': [-1, 6, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8408025503158569})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9002118110656738})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9266633987426758})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0874087810516357})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8524, 'crossentropy': 0.778425927734375}
store['active_learning_steps'][56]['acquisition']={'indices': [48887, 11639, 52738, 23702, 56537], 'labels': [-1, 0, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8630712032318115})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8388698101043701})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9022290706634521})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0202053785324097})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.892093300819397})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8744, 'crossentropy': 0.786449609375}
store['active_learning_steps'][57]['acquisition']={'indices': [7007, 33814, 54829, 29901, 37512], 'labels': [1, -1, 3, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9087247848510742})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9002389311790466})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9949114322662354})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0422520637512207})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9735157489776611})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.873, 'crossentropy': 0.860842578125}
store['active_learning_steps'][58]['acquisition']={'indices': [6235, 12503, 3754, 34195, 8671], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8161681294441223})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8429340124130249})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0305808782577515})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0060548782348633})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8519, 'crossentropy': 0.7767892578125}
store['active_learning_steps'][59]['acquisition']={'indices': [1699, 49016, 19983, 45163, 27944], 'labels': [1, -1, 4, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8370040655136108})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9272379875183105})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9486409425735474})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.111313819885254})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8379, 'crossentropy': 0.791417236328125}
store['active_learning_steps'][60]['acquisition']={'indices': [38481, 24107, 32186, 28547, 27827], 'labels': [-1, 5, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7706186175346375})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8584579825401306})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9010279774665833})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9526610374450684})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8621, 'crossentropy': 0.724057958984375}
store['active_learning_steps'][61]['acquisition']={'indices': [17424, 42912, 58788, 1120, 42779], 'labels': [-1, 6, -1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7838845252990723})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9874948263168335})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9935864806175232})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0346856117248535})
store['active_learning_steps'][62]['training']['best_epoch']=1
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.857, 'crossentropy': 0.74686884765625}
store['active_learning_steps'][62]['acquisition']={'indices': [14769, 23364, 17711, 7582, 45405], 'labels': [4, -1, 1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8548262715339661})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8450672626495361})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9320065379142761})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9585086107254028})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.118173360824585})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8749, 'crossentropy': 0.818714501953125}
store['active_learning_steps'][63]['acquisition']={'indices': [46189, 3638, 14393, 768, 26785], 'labels': [6, -1, -1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7596539855003357})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7438631057739258})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.76317298412323})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0211390256881714})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0195205211639404})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8854, 'crossentropy': 0.663698828125}
store['active_learning_steps'][64]['acquisition']={'indices': [16019, 51322, 43274, 23105, 59561], 'labels': [3, 7, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7862955331802368})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7944461107254028})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8548994064331055})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9498080015182495})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8533, 'crossentropy': 0.761216650390625}
store['active_learning_steps'][65]['acquisition']={'indices': [18815, 58771, 46936, 52645, 49137], 'labels': [2, 2, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7331163883209229})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7872191667556763})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0072702169418335})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0089720487594604})
store['active_learning_steps'][66]['training']['best_epoch']=1
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8675, 'crossentropy': 0.700802294921875}
store['active_learning_steps'][66]['acquisition']={'indices': [28431, 17443, 5538, 47957, 40087], 'labels': [-1, 7, 9, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8003035187721252})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8505691885948181})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8363616466522217})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9368367791175842})
store['active_learning_steps'][67]['training']['best_epoch']=1
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 0.778939697265625}
store['active_learning_steps'][67]['acquisition']={'indices': [55579, 6262, 53051, 18495, 29029], 'labels': [3, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8242847919464111})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8960544466972351})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8772451877593994})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9791310429573059})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8432, 'crossentropy': 0.769131884765625}
store['active_learning_steps'][68]['acquisition']={'indices': [11749, 39764, 15024, 54430, 57613], 'labels': [8, 8, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7674705982208252})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8590133190155029})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8853682279586792})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8206510543823242})
store['active_learning_steps'][69]['training']['best_epoch']=1
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8676, 'crossentropy': 0.731479541015625}
store['active_learning_steps'][69]['acquisition']={'indices': [12072, 23200, 2892, 31751, 50418], 'labels': [-1, -1, 2, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7831457853317261})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.730239748954773})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8277636766433716})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9032802581787109})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.937056839466095})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8889, 'crossentropy': 0.67030615234375}
store['active_learning_steps'][70]['acquisition']={'indices': [20179, 10233, 38839, 51187, 49540], 'labels': [2, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7538778781890869})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.911851167678833})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8237069845199585})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8917700052261353})
store['active_learning_steps'][71]['training']['best_epoch']=1
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8752, 'crossentropy': 0.730909326171875}
store['active_learning_steps'][71]['acquisition']={'indices': [24610, 4149, 7720, 20815, 38769], 'labels': [3, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7421690225601196})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.785507082939148})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7918000221252441})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8658944368362427})
store['active_learning_steps'][72]['training']['best_epoch']=1
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8706, 'crossentropy': 0.7164517578125}
store['active_learning_steps'][72]['acquisition']={'indices': [11197, 19883, 48992, 49303, 51444], 'labels': [3, 3, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7610903978347778})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7278443574905396})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7538033723831177})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7854825258255005})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9307228326797485})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8887, 'crossentropy': 0.664033349609375}
store['active_learning_steps'][73]['acquisition']={'indices': [38401, 24786, 53870, 28727, 38428], 'labels': [2, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7600528001785278})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7991316318511963})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8667950630187988})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9413626194000244})
store['active_learning_steps'][74]['training']['best_epoch']=1
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8491, 'crossentropy': 0.739886279296875}
store['active_learning_steps'][74]['acquisition']={'indices': [57819, 23083, 7421, 58237, 22625], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7398029565811157})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8058570623397827})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8010372519493103})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8173070549964905})
store['active_learning_steps'][75]['training']['best_epoch']=1
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8678, 'crossentropy': 0.716029248046875}
store['active_learning_steps'][75]['acquisition']={'indices': [31755, 24325, 52606, 33004, 30128], 'labels': [-1, 7, 7, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8303280472755432})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8057664632797241})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8484787940979004})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8952570557594299})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9813565015792847})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8756, 'crossentropy': 0.709214111328125}
store['active_learning_steps'][76]['acquisition']={'indices': [54112, 55302, 25697, 5728, 15356], 'labels': [-1, 0, 1, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7373322248458862})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7240683436393738})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.72223961353302})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8029230833053589})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8310185670852661})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8418630361557007})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.65832958984375}
store['active_learning_steps'][77]['acquisition']={'indices': [18042, 52778, 8329, 21463, 48633], 'labels': [-1, 5, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7654737234115601})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7073915004730225})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7223354578018188})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7925564050674438})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8461251258850098})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8936, 'crossentropy': 0.64671376953125}
store['active_learning_steps'][78]['acquisition']={'indices': [17082, 41340, 13951, 40348, 56695], 'labels': [3, 2, 8, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.771053671836853})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7103226780891418})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7617168426513672})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7249791026115417})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8871408700942993})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8867, 'crossentropy': 0.67816171875}
store['active_learning_steps'][79]['acquisition']={'indices': [27318, 46226, 31418, 24107, 22341], 'labels': [-1, -1, 5, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.69718337059021})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6917128562927246})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6960912942886353})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8148379325866699})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7591809034347534})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8774, 'crossentropy': 0.682225244140625}
store['active_learning_steps'][80]['acquisition']={'indices': [41045, 20067, 52087, 33652, 35115], 'labels': [5, 7, 4, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7949135899543762})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6059407591819763})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7370027303695679})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7013472318649292})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.711633026599884})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.5831654296875}
store['active_learning_steps'][81]['acquisition']={'indices': [21254, 7590, 468, 12931, 35453], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7320952415466309})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6890230178833008})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7616158723831177})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7730536460876465})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8010580539703369})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8941, 'crossentropy': 0.630750439453125}
store['active_learning_steps'][82]['acquisition']={'indices': [30540, 38484, 22796, 2232, 26966], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8318244218826294})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7402279376983643})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8697183132171631})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8877748250961304})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8277374505996704})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8749, 'crossentropy': 0.674235986328125}
store['active_learning_steps'][83]['acquisition']={'indices': [9573, 47842, 43472, 41768, 42570], 'labels': [-1, -1, -1, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.781499981880188})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7245633602142334})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7169418334960938})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.904558539390564})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8598905801773071})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8319391012191772})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.897, 'crossentropy': 0.734975927734375}
store['active_learning_steps'][84]['acquisition']={'indices': [11048, 25443, 35548, 42133, 2608], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6800442934036255})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7227914333343506})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8052613139152527})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8315281867980957})
store['active_learning_steps'][85]['training']['best_epoch']=1
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8753, 'crossentropy': 0.6803673828125}
store['active_learning_steps'][85]['acquisition']={'indices': [42926, 16173, 39210, 15218, 38960], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8326687216758728})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7350895404815674})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.84234619140625})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7735331058502197})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8776849508285522})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.6994162109375}
store['active_learning_steps'][86]['acquisition']={'indices': [22762, 4662, 54095, 24093, 51205], 'labels': [9, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7784002423286438})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8067476749420166})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7794005870819092})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8533467650413513})
store['active_learning_steps'][87]['training']['best_epoch']=1
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8698, 'crossentropy': 0.7130998046875}
store['active_learning_steps'][87]['acquisition']={'indices': [14163, 55281, 36090, 25436, 11802], 'labels': [2, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7387865781784058})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6650437116622925})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7386782765388489})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7144755721092224})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7914963364601135})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.8885, 'crossentropy': 0.63027919921875}
store['active_learning_steps'][88]['acquisition']={'indices': [24188, 16332, 1909, 28923, 38551], 'labels': [-1, -1, 1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7371793985366821})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.671806275844574})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.679030179977417})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7463728189468384})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7504438161849976})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.8904, 'crossentropy': 0.64513740234375}
store['active_learning_steps'][89]['acquisition']={'indices': [40611, 20539, 12815, 51476, 47733], 'labels': [-1, -1, 2, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7136217951774597})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7455544471740723})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6984297633171082})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8390419483184814})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8969887495040894})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8195146322250366})
store['active_learning_steps'][90]['training']['best_epoch']=3
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9023, 'crossentropy': 0.66494814453125}
store['active_learning_steps'][90]['acquisition']={'indices': [41910, 45717, 50750, 8545, 40224], 'labels': [-1, -1, 0, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.794292688369751})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.66141676902771})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7472695112228394})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7786388397216797})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.873964786529541})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.8943, 'crossentropy': 0.621054443359375}
store['active_learning_steps'][91]['acquisition']={'indices': [1037, 26947, 37889, 39032, 22317], 'labels': [4, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7298692464828491})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7264412641525269})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7504328489303589})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7744777202606201})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8716435432434082})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.8864, 'crossentropy': 0.6732275390625}
store['active_learning_steps'][92]['acquisition']={'indices': [12575, 34569, 30598, 34321, 31245], 'labels': [0, -1, -1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8005012273788452})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7420176267623901})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8910889625549316})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7602770328521729})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8757283091545105})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.678922021484375}
store['active_learning_steps'][93]['acquisition']={'indices': [950, 58336, 952, 57686, 49193], 'labels': [-1, 3, 0, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7456760406494141})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.699637770652771})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7311841249465942})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8004506230354309})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8577808141708374})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.8897, 'crossentropy': 0.648700634765625}
store['active_learning_steps'][94]['acquisition']={'indices': [48981, 28447, 42369, 32538, 48436], 'labels': [3, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7146363258361816})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6642099022865295})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8313407897949219})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8772833347320557})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8044633269309998})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.627996630859375}
store['active_learning_steps'][95]['acquisition']={'indices': [43336, 53283, 47179, 51249, 3021], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7801027297973633})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7247374057769775})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7653558254241943})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7207387685775757})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8108429908752441})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.9102433919906616})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7682238817214966})
store['active_learning_steps'][96]['training']['best_epoch']=4
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.70600439453125}
store['active_learning_steps'][96]['acquisition']={'indices': [51834, 37408, 14133, 54591, 13736], 'labels': [0, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8487732410430908})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7639460563659668})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8411613702774048})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7787744998931885})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8860070705413818})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.878, 'crossentropy': 0.724114990234375}
store['active_learning_steps'][97]['acquisition']={'indices': [12384, 29293, 12913, 7826, 52846], 'labels': [4, -1, 3, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8434222936630249})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6828044652938843})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7310078144073486})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7408434152603149})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7624902725219727})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.651855224609375}
store['active_learning_steps'][98]['acquisition']={'indices': [39855, 8086, 10624, 24402, 34275], 'labels': [3, 4, 1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7530142068862915})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6771495342254639})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8346236944198608})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8918464183807373})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.865610659122467})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.8884, 'crossentropy': 0.672513037109375}
store['active_learning_steps'][99]['acquisition']={'indices': [7883, 41326, 18454, 45011, 35996], 'labels': [4, 9, 2, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7385692596435547})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.707379937171936})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7253780364990234})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7219771146774292})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7565054893493652})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.8955, 'crossentropy': 0.607813720703125}
store['active_learning_steps'][100]['acquisition']={'indices': [25724, 29778, 9258, 53629, 47775], 'labels': [1, 9, 2, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7491704225540161})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6907118558883667})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6836158037185669})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8028346300125122})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7772217988967896})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7325649261474609})
store['active_learning_steps'][101]['training']['best_epoch']=3
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9075, 'crossentropy': 0.60022783203125}
store['active_learning_steps'][101]['acquisition']={'indices': [25778, 54783, 3255, 22713, 3412], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7989391088485718})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6764861345291138})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7393994927406311})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7954182028770447})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8237127661705017})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.893, 'crossentropy': 0.63582001953125}
store['active_learning_steps'][102]['acquisition']={'indices': [13867, 56364, 47635, 22695, 49653], 'labels': [-1, 4, 8, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7371994256973267})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6611538529396057})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7527081370353699})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7833500504493713})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.741655707359314})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.61448076171875}
store['active_learning_steps'][103]['acquisition']={'indices': [977, 47249, 21102, 43977, 12328], 'labels': [-1, 2, 3, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.749616265296936})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6438415050506592})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6863676309585571})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6925786733627319})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7505612373352051})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.6047240234375}
store['active_learning_steps'][104]['acquisition']={'indices': [17688, 21996, 1980, 27298, 21425], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.796920895576477})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7231317758560181})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6353306770324707})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7670376300811768})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6906396150588989})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7852481603622437})
store['active_learning_steps'][105]['training']['best_epoch']=3
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.572721142578125}
store['active_learning_steps'][105]['acquisition']={'indices': [55663, 4663, 11783, 4710, 52316], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7416374683380127})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6538972854614258})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7458584308624268})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7469086647033691})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7055404186248779})
store['active_learning_steps'][106]['training']['best_epoch']=2
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.585980859375}
store['active_learning_steps'][106]['acquisition']={'indices': [51598, 43120, 48810, 58419, 19694], 'labels': [0, -1, -1, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6648794412612915})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6721469759941101})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6516857743263245})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6341878175735474})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6369962692260742})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7248144149780273})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7378859519958496})
store['active_learning_steps'][107]['training']['best_epoch']=4
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.567516064453125}
store['active_learning_steps'][107]['acquisition']={'indices': [30991, 27284, 4448, 12685, 8137], 'labels': [5, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6984682679176331})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6281446218490601})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.694720983505249})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6872135400772095})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7722718119621277})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.5636853515625}
store['active_learning_steps'][108]['acquisition']={'indices': [53460, 16441, 27607, 5862, 23649], 'labels': [0, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6999940872192383})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6535447835922241})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7353175282478333})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7736929059028625})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7138709425926208})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.5801029296875}
store['active_learning_steps'][109]['acquisition']={'indices': [32267, 8003, 15530, 9260, 26672], 'labels': [3, 0, 0, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.695336103439331})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5975075960159302})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6406328678131104})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.705073356628418})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7748662233352661})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.530541357421875}
store['active_learning_steps'][110]['acquisition']={'indices': [973, 10175, 3642, 42389, 13561], 'labels': [-1, 4, 2, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7693041563034058})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6905522346496582})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6370210647583008})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6506890058517456})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6509178280830383})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7208415269851685})
store['active_learning_steps'][111]['training']['best_epoch']=3
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.902, 'crossentropy': 0.628637744140625}
store['active_learning_steps'][111]['acquisition']={'indices': [8341, 2816, 7290, 7062, 43175], 'labels': [4, -1, 8, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7110499143600464})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6037040948867798})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6356865167617798})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7481898069381714})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6787319183349609})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.561605419921875}
store['active_learning_steps'][112]['acquisition']={'indices': [16323, 16028, 54132, 34850, 28706], 'labels': [-1, -1, 8, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7355761528015137})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6615855693817139})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.74155592918396})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7157830595970154})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7924483418464661})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.603961962890625}
store['active_learning_steps'][113]['acquisition']={'indices': [7169, 38183, 42186, 9548, 36041], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7006919384002686})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6771022081375122})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6725080013275146})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6729558706283569})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7149423360824585})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7380561828613281})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.59171865234375}
store['active_learning_steps'][114]['acquisition']={'indices': [52207, 1069, 6467, 39775, 677], 'labels': [-1, 1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7550487518310547})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6418042778968811})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6178106069564819})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6905162334442139})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7049041986465454})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.712143063545227})
store['active_learning_steps'][115]['training']['best_epoch']=3
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.53659970703125}
store['active_learning_steps'][115]['acquisition']={'indices': [36562, 12614, 48087, 28193, 406], 'labels': [0, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7451379895210266})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6477454900741577})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7409571409225464})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.691584587097168})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7679859399795532})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.566459326171875}
store['active_learning_steps'][116]['acquisition']={'indices': [41797, 18231, 1320, 17216, 11914], 'labels': [6, 2, 3, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7445250749588013})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6430380940437317})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7524499893188477})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6620736718177795})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7314325571060181})
store['active_learning_steps'][117]['training']['best_epoch']=2
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.8924, 'crossentropy': 0.608897802734375}
store['active_learning_steps'][117]['acquisition']={'indices': [9298, 57226, 14585, 25566, 13107], 'labels': [1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7275682687759399})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5871186852455139})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7412668466567993})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7409497499465942})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6212237477302551})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.53837607421875}
store['active_learning_steps'][118]['acquisition']={'indices': [26419, 14362, 15894, 24800, 26320], 'labels': [3, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7722786664962769})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6534721851348877})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6688354015350342})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7103787660598755})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7590380907058716})
store['active_learning_steps'][119]['training']['best_epoch']=2
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.8948, 'crossentropy': 0.627001171875}
store['active_learning_steps'][119]['acquisition']={'indices': [31958, 57962, 32490, 16727, 19186], 'labels': [2, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7336294651031494})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6624942421913147})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6943968534469604})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6734565496444702})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6759878396987915})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.8956, 'crossentropy': 0.601954345703125}
store['active_learning_steps'][120]['acquisition']={'indices': [58621, 13031, 34589, 56085, 31355], 'labels': [4, -1, 6, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7379416823387146})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6372114419937134})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6507502794265747})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6479097604751587})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6872491836547852})
store['active_learning_steps'][121]['training']['best_epoch']=2
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9027, 'crossentropy': 0.579702587890625}
store['active_learning_steps'][121]['acquisition']={'indices': [59551, 31473, 13755, 52588, 29573], 'labels': [-1, 5, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8210095763206482})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7095462083816528})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7786784172058105})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7056314945220947})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7601857781410217})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7897151708602905})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7797510623931885})
store['active_learning_steps'][122]['training']['best_epoch']=4
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.8982, 'crossentropy': 0.65673515625}
store['active_learning_steps'][122]['acquisition']={'indices': [28689, 50783, 43295, 50752, 28905], 'labels': [9, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7656058073043823})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.64983069896698})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6384942531585693})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.721683144569397})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7044934034347534})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7198320031166077})
store['active_learning_steps'][123]['training']['best_epoch']=3
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.564473974609375}
store['active_learning_steps'][123]['acquisition']={'indices': [46705, 38583, 29631, 11099, 34883], 'labels': [1, 4, 4, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6607137322425842})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5929145812988281})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6229590773582458})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6172188520431519})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6407626271247864})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9065, 'crossentropy': 0.555194970703125}
store['active_learning_steps'][124]['acquisition']={'indices': [38431, 3307, 918, 33508, 44358], 'labels': [-1, 2, 7, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7125368118286133})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6229084730148315})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6500293612480164})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6767212748527527})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.730617880821228})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9064, 'crossentropy': 0.59922578125}
store['active_learning_steps'][125]['acquisition']={'indices': [42111, 51686, 20276, 11056, 59728], 'labels': [-1, 3, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7277054786682129})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6283135414123535})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5816718339920044})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6246539354324341})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6638801097869873})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6765116453170776})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.54624140625}
store['active_learning_steps'][126]['acquisition']={'indices': [8545, 10463, 2928, 2962, 18036], 'labels': [0, 6, 5, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7762601375579834})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5935230851173401})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6450347304344177})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6163696050643921})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7031246423721313})
store['active_learning_steps'][127]['training']['best_epoch']=2
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.53224033203125}
store['active_learning_steps'][127]['acquisition']={'indices': [25729, 52628, 50371, 51210, 56741], 'labels': [-1, -1, -1, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7503327131271362})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5951697826385498})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5936498045921326})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6982540488243103})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.716100811958313})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6420806646347046})
store['active_learning_steps'][128]['training']['best_epoch']=3
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.50209462890625}
store['active_learning_steps'][128]['acquisition']={'indices': [45064, 2163, 4602, 44230, 146], 'labels': [4, 6, 1, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7257211804389954})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5920385122299194})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6447916626930237})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6375548839569092})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7378746271133423})
store['active_learning_steps'][129]['training']['best_epoch']=2
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.5219701171875}
store['active_learning_steps'][129]['acquisition']={'indices': [3418, 31135, 10602, 6884, 55288], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7188478708267212})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6572859287261963})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6408356428146362})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6085231304168701})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6101240515708923})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6847921013832092})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6993615627288818})
store['active_learning_steps'][130]['training']['best_epoch']=4
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.508489111328125}
store['active_learning_steps'][130]['acquisition']={'indices': [5439, 30395, 32092, 20266, 27813], 'labels': [1, 9, 0, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6738314628601074})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6130430698394775})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.561935544013977})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5652869939804077})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5809043645858765})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6446149945259094})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.528410693359375}
store['active_learning_steps'][131]['acquisition']={'indices': [57063, 59637, 17277, 51151, 43561], 'labels': [7, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7475427389144897})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6793845891952515})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7095733284950256})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6565728783607483})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6774527430534363})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.696593165397644})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6472837328910828})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8882174491882324})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9111084938049316})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7418628931045532})
store['active_learning_steps'][132]['training']['best_epoch']=7
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.599606689453125}
store['active_learning_steps'][132]['acquisition']={'indices': [57171, 24101, 23691, 4587, 222], 'labels': [-1, -1, 2, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6447405815124512})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6193251609802246})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5983141660690308})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6196737289428711})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6141943335533142})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5950326919555664})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6125810146331787})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6414620280265808})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6307234764099121})
store['active_learning_steps'][133]['training']['best_epoch']=6
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.54350537109375}
store['active_learning_steps'][133]['acquisition']={'indices': [26881, 38244, 9509, 24082, 14903], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7209287881851196})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6066412925720215})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5756289958953857})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.664055347442627})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6139880418777466})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6011946201324463})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.56449296875}
store['active_learning_steps'][134]['acquisition']={'indices': [4293, 10886, 38980, 55952, 7302], 'labels': [-1, 1, 6, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6793268918991089})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5941344499588013})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5877597332000732})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6361086368560791})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6256484985351562})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6142665147781372})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.4918564453125}
store['active_learning_steps'][135]['acquisition']={'indices': [21986, 58074, 6457, 27612, 48118], 'labels': [3, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6683241128921509})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6545497179031372})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6229162216186523})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6065024137496948})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6570055484771729})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7224615812301636})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6950920224189758})
store['active_learning_steps'][136]['training']['best_epoch']=4
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.5665603515625}
store['active_learning_steps'][136]['acquisition']={'indices': [3987, 30240, 40417, 4498, 33296], 'labels': [9, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7109878659248352})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5739649534225464})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5923810005187988})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6696237325668335})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6310924887657166})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.54115048828125}
store['active_learning_steps'][137]['acquisition']={'indices': [43090, 22745, 31019, 47900, 48267], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.660719633102417})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5818290710449219})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7416354417800903})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.597472071647644})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6443483829498291})
store['active_learning_steps'][138]['training']['best_epoch']=2
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.51260712890625}
store['active_learning_steps'][138]['acquisition']={'indices': [41674, 32482, 15181, 21039, 27717], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6816194653511047})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6077250242233276})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6112258434295654})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6653673648834229})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6388469338417053})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.521796533203125}
store['active_learning_steps'][139]['acquisition']={'indices': [32273, 29128, 33308, 1710, 34332], 'labels': [0, 0, 9, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7092727422714233})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6256222724914551})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6146589517593384})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6858289241790771})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7200801968574524})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7076972723007202})
store['active_learning_steps'][140]['training']['best_epoch']=3
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.5618603515625}
store['active_learning_steps'][140]['acquisition']={'indices': [11959, 10497, 7242, 37144, 43428], 'labels': [6, 2, -1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7294728755950928})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6665764451026917})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6577950716018677})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6864680051803589})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5542778968811035})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6508083343505859})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.743868350982666})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7250291705131531})
store['active_learning_steps'][141]['training']['best_epoch']=5
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.5025900390625}
store['active_learning_steps'][141]['acquisition']={'indices': [54906, 43282, 49279, 5360, 30432], 'labels': [4, 9, 8, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6946689486503601})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6782248020172119})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.641179084777832})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.633141279220581})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6842067241668701})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.655077338218689})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7298545837402344})
store['active_learning_steps'][142]['training']['best_epoch']=4
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.54349912109375}
store['active_learning_steps'][142]['acquisition']={'indices': [20211, 47022, 13217, 24140, 18008], 'labels': [-1, 1, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7596705555915833})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5750796794891357})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6807981729507446})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6429815292358398})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6204516887664795})
store['active_learning_steps'][143]['training']['best_epoch']=2
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.560447412109375}
store['active_learning_steps'][143]['acquisition']={'indices': [1218, 5483, 32841, 2930, 54632], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7581530213356018})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6137586236000061})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6192499995231628})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6695933938026428})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6727323532104492})
store['active_learning_steps'][144]['training']['best_epoch']=2
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.55122080078125}
store['active_learning_steps'][144]['acquisition']={'indices': [34988, 41753, 41132, 17853, 50574], 'labels': [4, 3, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6380118131637573})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5888446569442749})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6334253549575806})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6004968881607056})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6620128154754639})
store['active_learning_steps'][145]['training']['best_epoch']=2
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.54571884765625}
store['active_learning_steps'][145]['acquisition']={'indices': [52082, 3793, 26525, 4047, 46726], 'labels': [1, -1, 9, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7109553813934326})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5774198770523071})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5997867584228516})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6140581369400024})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6244344711303711})
store['active_learning_steps'][146]['training']['best_epoch']=2
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.55031298828125}
store['active_learning_steps'][146]['acquisition']={'indices': [10191, 33958, 28660, 9008, 57060], 'labels': [-1, -1, 1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7005656361579895})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6140397191047668})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6096913814544678})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5685548782348633})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5998222827911377})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7081602811813354})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7065674066543579})
store['active_learning_steps'][147]['training']['best_epoch']=4
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.5034765625}
store['active_learning_steps'][147]['acquisition']={'indices': [50634, 17651, 44828, 23114, 54757], 'labels': [8, -1, -1, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7022101879119873})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5684834718704224})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6243463754653931})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5617872476577759})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.638444185256958})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6793681383132935})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7067793607711792})
store['active_learning_steps'][148]['training']['best_epoch']=4
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.543922802734375}
store['active_learning_steps'][148]['acquisition']={'indices': [32956, 46494, 9586, 55506, 28554], 'labels': [7, -1, 4, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6685344576835632})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6072232127189636})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6229621767997742})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6241801977157593})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6290980577468872})
store['active_learning_steps'][149]['training']['best_epoch']=2
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.552284521484375}
store['active_learning_steps'][149]['acquisition']={'indices': [7561, 20762, 50584, 48090, 26876], 'labels': [-1, -1, 6, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6613250970840454})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6324093341827393})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5730360150337219})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5852221250534058})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5797581672668457})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6050155162811279})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.52203583984375}
store['active_learning_steps'][150]['acquisition']={'indices': [37884, 19254, 36000, 30523, 4183], 'labels': [-1, 9, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6430480480194092})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6251773834228516})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5682172775268555})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6119733452796936})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.604474663734436})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.615320086479187})
store['active_learning_steps'][151]['training']['best_epoch']=3
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.5056048828125}
store['active_learning_steps'][151]['acquisition']={'indices': [44089, 46467, 22698, 49454, 10084], 'labels': [1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7187992930412292})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5924219489097595})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6436924934387207})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6599860191345215})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6416692733764648})
store['active_learning_steps'][152]['training']['best_epoch']=2
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.5176853515625}
store['active_learning_steps'][152]['acquisition']={'indices': [43827, 7143, 51787, 31124, 4753], 'labels': [-1, 0, 2, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7756370306015015})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5829340815544128})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5968635082244873})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.609500527381897})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5884588956832886})
store['active_learning_steps'][153]['training']['best_epoch']=2
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.541925732421875}
store['active_learning_steps'][153]['acquisition']={'indices': [8777, 38563, 51747, 40136, 51448], 'labels': [6, 2, -1, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6821684837341309})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5604620575904846})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5414280891418457})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5615439414978027})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5308433771133423})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6399734616279602})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5540130138397217})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6330530643463135})
store['active_learning_steps'][154]['training']['best_epoch']=5
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.486401171875}
store['active_learning_steps'][154]['acquisition']={'indices': [35162, 42870, 7071, 24437, 51805], 'labels': [-1, 9, 9, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7509828805923462})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5959368348121643})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5392467379570007})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5805492997169495})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5985636711120605})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6196964979171753})
store['active_learning_steps'][155]['training']['best_epoch']=3
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.462725830078125}
store['active_learning_steps'][155]['acquisition']={'indices': [38952, 12777, 11282, 27206, 57290], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6886415481567383})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5553609728813171})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5221577286720276})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5091351270675659})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5937179923057556})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5420185327529907})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.583017885684967})
store['active_learning_steps'][156]['training']['best_epoch']=4
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.50393701171875}
store['active_learning_steps'][156]['acquisition']={'indices': [3760, 3981, 54608, 57225, 33434], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6894513964653015})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6161051988601685})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5714555382728577})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5516471862792969})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5108492374420166})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.652963399887085})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5700932741165161})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.607756495475769})
store['active_learning_steps'][157]['training']['best_epoch']=5
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.520078466796875}
store['active_learning_steps'][157]['acquisition']={'indices': [23407, 4944, 46521, 40606, 37595], 'labels': [5, -1, 6, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7287945747375488})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6245042681694031})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5754368305206299})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5757851600646973})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6021627187728882})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.60365891456604})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.519191552734375}
store['active_learning_steps'][158]['acquisition']={'indices': [37125, 49931, 981, 5279, 39467], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7462124228477478})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5800154805183411})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5540798902511597})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5420578718185425})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.584247887134552})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5995910167694092})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6013894081115723})
store['active_learning_steps'][159]['training']['best_epoch']=4
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9262, 'crossentropy': 0.502385302734375}
store['active_learning_steps'][159]['acquisition']={'indices': [43157, 23963, 19422, 59245, 49436], 'labels': [-1, 6, 5, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7474778294563293})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5788557529449463})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.588134765625})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5807507634162903})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6244626045227051})
store['active_learning_steps'][160]['training']['best_epoch']=2
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.533401318359375}
store['active_learning_steps'][160]['acquisition']={'indices': [36023, 46253, 2305, 28181, 42039], 'labels': [-1, 7, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7006505131721497})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5759755373001099})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5492162704467773})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5500590801239014})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5617727041244507})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6312487721443176})
store['active_learning_steps'][161]['training']['best_epoch']=3
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9268, 'crossentropy': 0.495109423828125}
store['active_learning_steps'][161]['acquisition']={'indices': [34959, 47463, 55051, 38562, 6900], 'labels': [7, 8, 3, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6821655035018921})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.541813850402832})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5605449676513672})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5630404949188232})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5313420295715332})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5470964908599854})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6475787162780762})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6503599882125854})
store['active_learning_steps'][162]['training']['best_epoch']=5
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.4875576171875}
store['active_learning_steps'][162]['acquisition']={'indices': [7101, 14004, 51726, 12887, 37305], 'labels': [8, -1, 2, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6771043539047241})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6020627021789551})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5212447643280029})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5666918158531189})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5870776176452637})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5504487752914429})
store['active_learning_steps'][163]['training']['best_epoch']=3
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.479851806640625}
store['active_learning_steps'][163]['acquisition']={'indices': [38845, 55183, 17660, 47944, 29703], 'labels': [-1, 2, 2, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6963511109352112})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5882389545440674})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6159976720809937})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5269757509231567})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5479391813278198})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6198940277099609})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6459711790084839})
store['active_learning_steps'][164]['training']['best_epoch']=4
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.499362060546875}
store['active_learning_steps'][164]['acquisition']={'indices': [32047, 44229, 52404, 14834, 51112], 'labels': [9, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7001392245292664})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5469497442245483})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5380829572677612})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5500431060791016})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.602555513381958})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5338536500930786})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5276257991790771})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5213626027107239})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6025756597518921})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5923573970794678})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5620896816253662})
store['active_learning_steps'][165]['training']['best_epoch']=8
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9324, 'crossentropy': 0.492555517578125}
store['active_learning_steps'][165]['acquisition']={'indices': [48292, 39247, 55338, 6666, 19845], 'labels': [2, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7161978483200073})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6199408769607544})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5779235363006592})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6033066511154175})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5908938646316528})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6117452383041382})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.51090693359375}
store['active_learning_steps'][166]['acquisition']={'indices': [32864, 25711, 12159, 2459, 18553], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6312412023544312})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.48597609996795654})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5151885747909546})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6266494393348694})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5565053224563599})
store['active_learning_steps'][167]['training']['best_epoch']=2
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.465899658203125}
store['active_learning_steps'][167]['acquisition']={'indices': [48901, 40918, 4518, 38013, 1330], 'labels': [3, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7020119428634644})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5058999061584473})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.525061845779419})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5327824354171753})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.54481041431427})
store['active_learning_steps'][168]['training']['best_epoch']=2
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.473925634765625}
store['active_learning_steps'][168]['acquisition']={'indices': [20980, 18797, 58919, 17937, 27723], 'labels': [7, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6320669651031494})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5158655643463135})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49157628417015076})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5369380116462708})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5022502541542053})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.562142550945282})
store['active_learning_steps'][169]['training']['best_epoch']=3
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.428997216796875}
store['active_learning_steps'][169]['acquisition']={'indices': [16611, 22060, 1411, 58401, 24406], 'labels': [8, 8, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6288361549377441})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6193743348121643})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5700688362121582})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5603644847869873})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5460464954376221})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.589522123336792})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5114718079566956})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.578707218170166})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.679466962814331})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6218884587287903})
store['active_learning_steps'][170]['training']['best_epoch']=7
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.5098232421875}
store['active_learning_steps'][170]['acquisition']={'indices': [19676, 25003, 56853, 21644, 18834], 'labels': [-1, 1, 4, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7401012182235718})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5420367121696472})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5523404479026794})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5580832958221436})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5645542144775391})
store['active_learning_steps'][171]['training']['best_epoch']=2
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.507081591796875}
