store = {}
store['timestamp']=1620260394
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=35']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=35
store['worker_id']=35
store['num_workers']=40
store['config']={'seed': 50, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.14080810546875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.355956554412842})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.795259475708008})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.943040132522583})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6872, 'crossentropy': 1.85677421875}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 23347], ['id', 19309], ['ood', 53048], ['ood', 42256], ['ood', 31567]], 'labels': [9, 6, 7, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4210416078567505})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5781852006912231})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8249045610427856})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9227290153503418})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6952, 'crossentropy': 1.34523076171875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 39652], ['ood', 24802], ['ood', 45972], ['id', 53601], ['id', 9810]], 'labels': [1, 0, 5, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4246788024902344})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.6238048076629639})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7961264848709106})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.811547875404358})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6866, 'crossentropy': 1.38876318359375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 2991], ['ood', 32606], ['id', 41270], ['id', 33249], ['id', 6991]], 'labels': [8, 4, 9, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4950525760650635})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.4890058040618896})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.7233794927597046})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0686421394348145})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.1723644733428955})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.716, 'crossentropy': 1.530057421875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 56625], ['ood', 41788], ['ood', 11032], ['ood', 8732], ['ood', 41271]], 'labels': [8, 0, 0, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4035687446594238})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.809224009513855})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9694252014160156})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9842368364334106})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6734, 'crossentropy': 1.39745009765625}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 51123], ['id', 44750], ['id', 1097], ['id', 10825], ['id', 33929]], 'labels': [9, 0, 3, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3391928672790527})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4434912204742432})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5528502464294434})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6135330200195312})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.697, 'crossentropy': 1.295353515625}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 48194], ['ood', 24884], ['ood', 49251], ['ood', 29214], ['id', 2025]], 'labels': [5, 7, 6, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3267130851745605})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5097986459732056})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7035959959030151})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5441522598266602})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7047, 'crossentropy': 1.32428408203125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 4376], ['ood', 41367], ['id', 58556], ['ood', 17497], ['ood', 15811]], 'labels': [5, 3, 8, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1488797664642334})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.301672339439392})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.3189563751220703})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.290102243423462})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7277, 'crossentropy': 1.17404189453125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 57226], ['id', 59368], ['ood', 34888], ['id', 47054], ['id', 41612]], 'labels': [6, 5, 9, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.2314465045928955})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.3048733472824097})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.4730565547943115})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7192933559417725})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7434, 'crossentropy': 1.16981875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 6059], ['ood', 51634], ['ood', 28278], ['ood', 37498], ['ood', 38251]], 'labels': [3, 3, 8, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2492423057556152})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2065931558609009})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.376328945159912})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.5653233528137207})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.4265918731689453})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7498, 'crossentropy': 1.28552275390625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 14009], ['ood', 18561], ['id', 22331], ['ood', 25616], ['ood', 54268]], 'labels': [5, 0, 4, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9646579027175903})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9498479962348938})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0347535610198975})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2940239906311035})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1602469682693481})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8181, 'crossentropy': 0.94546923828125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 33556], ['id', 20344], ['id', 3481], ['ood', 52859], ['id', 31589]], 'labels': [1, 3, 9, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1256146430969238})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0919725894927979})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2049460411071777})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1988694667816162})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.264871597290039})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7819, 'crossentropy': 1.078741015625}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 37684], ['ood', 2019], ['id', 22631], ['id', 14014], ['id', 33658]], 'labels': [5, 8, 3, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0337283611297607})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0424164533615112})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1485483646392822})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2822860479354858})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7866, 'crossentropy': 0.980106640625}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 30677], ['id', 9177], ['ood', 12041], ['ood', 1731], ['id', 42474]], 'labels': [2, 6, 4, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.9436426162719727})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0037777423858643})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2105882167816162})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2523274421691895})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7842, 'crossentropy': 0.92958251953125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 25935], ['id', 46311], ['ood', 53905], ['id', 22124], ['ood', 7833]], 'labels': [4, 7, 8, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9935051202774048})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9970706701278687})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0264288187026978})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1368590593338013})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7798, 'crossentropy': 0.93944677734375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 9715], ['ood', 4146], ['id', 11642], ['ood', 50366], ['id', 2695]], 'labels': [2, 7, 7, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9243654608726501})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9904294013977051})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0413274765014648})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0525414943695068})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8025, 'crossentropy': 0.89572568359375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 13457], ['ood', 51989], ['ood', 4876], ['ood', 30250], ['id', 15261]], 'labels': [5, 4, 7, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.0403828620910645})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0321193933486938})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0150399208068848})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1368029117584229})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.119493007659912})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1745787858963013})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8094, 'crossentropy': 0.98262333984375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 58494], ['id', 5976], ['id', 40058], ['id', 37325], ['ood', 10923]], 'labels': [2, 7, 1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.966971755027771})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9885859489440918})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0893769264221191})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1527429819107056})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7646, 'crossentropy': 0.9676083984375}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 32141], ['id', 7358], ['id', 57329], ['id', 37296], ['id', 42133]], 'labels': [0, 0, 8, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9834858179092407})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9036678075790405})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0151926279067993})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0743038654327393})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0723018646240234})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8246, 'crossentropy': 0.83170859375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 29034], ['ood', 41001], ['id', 39265], ['id', 6846], ['id', 52510]], 'labels': [7, 5, 1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0241649150848389})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9914205074310303})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9547670483589172})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0002650022506714})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1524503231048584})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2382447719573975})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8171, 'crossentropy': 0.91260048828125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 42764], ['id', 31115], ['id', 58143], ['ood', 46350], ['ood', 40559]], 'labels': [1, 9, 7, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.0728089809417725})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9347066879272461})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0052967071533203})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1709554195404053})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0595283508300781})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.791, 'crossentropy': 0.9721748046875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 56186], ['ood', 6750], ['id', 22957], ['ood', 13690], ['ood', 41465]], 'labels': [3, 4, 3, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0608184337615967})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0402082204818726})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0952913761138916})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.2596843242645264})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.3517177104949951})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7856, 'crossentropy': 0.96146962890625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 29287], ['id', 8846], ['ood', 30771], ['ood', 59742], ['ood', 39259]], 'labels': [0, 6, 8, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.9830573797225952})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9598512649536133})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0500539541244507})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1507396697998047})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.239192008972168})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7929, 'crossentropy': 0.9188919921875}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 38891], ['ood', 28067], ['id', 14920], ['ood', 41674], ['id', 18907]], 'labels': [8, 4, 7, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9803483486175537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9608266353607178})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0477440357208252})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1592588424682617})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2849599123001099})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7988, 'crossentropy': 0.89479609375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 58994], ['id', 34574], ['id', 53791], ['id', 20687], ['ood', 21575]], 'labels': [4, 8, 1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0011749267578125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8245353698730469})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9266928434371948})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9894001483917236})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1095634698867798})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8249, 'crossentropy': 0.799234033203125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4763], ['id', 44409], ['id', 11668], ['id', 55375], ['ood', 3096]], 'labels': [1, 7, 9, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9519276022911072})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8721300363540649})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9039938449859619})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0113091468811035})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9827470779418945})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8203, 'crossentropy': 0.80651015625}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 14635], ['ood', 48157], ['ood', 7035], ['ood', 34153], ['id', 21704]], 'labels': [2, 9, 2, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.9450014233589172})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9004529714584351})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8617702722549438})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8763530254364014})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8981810808181763})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9584980010986328})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8354, 'crossentropy': 0.8151501953125}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 35282], ['ood', 36902], ['ood', 19276], ['ood', 28991], ['ood', 52063]], 'labels': [8, 7, 9, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9943361878395081})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8268401622772217})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8826277852058411})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9010112285614014})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0629792213439941})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8192, 'crossentropy': 0.81816044921875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 35639], ['ood', 35571], ['id', 47958], ['id', 28113], ['ood', 37201]], 'labels': [0, 6, 9, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.0055714845657349})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8711510300636292})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0574047565460205})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0517046451568604})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1920092105865479})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8113, 'crossentropy': 0.872541796875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 9611], ['id', 35936], ['id', 57738], ['id', 52263], ['id', 4901]], 'labels': [2, 0, 1, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.9715872406959534})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9849079847335815})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9147351980209351})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0137827396392822})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0198605060577393})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1176073551177979})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8171, 'crossentropy': 0.8926779296875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 5566], ['ood', 24409], ['id', 12697], ['id', 52260], ['ood', 29341]], 'labels': [7, 2, 5, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9396936297416687})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8353855609893799})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8599871397018433})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.869097888469696})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9228684902191162})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8323, 'crossentropy': 0.78781494140625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 12018], ['id', 10192], ['ood', 52950], ['ood', 40900], ['id', 37083]], 'labels': [7, 5, 8, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8919714689254761})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8570026159286499})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8558204174041748})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8415665626525879})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.927916944026947})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0014491081237793})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9526552557945251})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8576, 'crossentropy': 0.80882451171875}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 50019], ['ood', 10596], ['id', 45600], ['ood', 44953], ['id', 33202]], 'labels': [8, 7, 7, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.953036904335022})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7669742107391357})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7647919654846191})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.742760419845581})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7919616103172302})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8510115146636963})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.909384548664093})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8827, 'crossentropy': 0.658333349609375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 1803], ['id', 7161], ['ood', 58858], ['id', 13262], ['id', 41212]], 'labels': [3, 2, 8, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9296482801437378})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7118340730667114})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7161720991134644})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7587772607803345})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8810509443283081})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8757, 'crossentropy': 0.666018359375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 1173], ['ood', 2404], ['id', 12172], ['ood', 9795], ['id', 49470]], 'labels': [9, 3, 9, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8741530179977417})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.787595272064209})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7420559525489807})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7642993330955505})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7987689971923828})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8053721189498901})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8715, 'crossentropy': 0.66173984375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 39987], ['ood', 15938], ['ood', 52241], ['id', 30326], ['ood', 51286]], 'labels': [6, 0, 2, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8347915410995483})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7364276051521301})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7008475065231323})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8465709686279297})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7523699998855591})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8144618272781372})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.872, 'crossentropy': 0.67429638671875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 455], ['id', 48612], ['id', 40523], ['id', 21656], ['id', 49411]], 'labels': [1, 0, 4, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.8776395916938782})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7248261570930481})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7123144865036011})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7582628726959229})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8279410600662231})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9716280698776245})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.883, 'crossentropy': 0.64673447265625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 6019], ['ood', 6284], ['id', 16284], ['id', 16363], ['id', 17869]], 'labels': [9, 0, 8, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.9094602465629578})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7721819281578064})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7652348279953003})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7395027875900269})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7081817388534546})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8659778833389282})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7919034957885742})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8588917255401611})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 0.6674546875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 48020], ['ood', 56577], ['id', 27647], ['ood', 50176], ['ood', 17251]], 'labels': [4, 2, 7, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8209394812583923})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6753226518630981})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7413535118103027})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7238596677780151})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7817264795303345})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.62103828125}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 59689], ['ood', 45631], ['ood', 17140], ['ood', 11894], ['id', 27020]], 'labels': [1, 5, 3, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8728872537612915})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6455659866333008})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7208328247070312})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7497163414955139})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6965984106063843})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.62675263671875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 38996], ['id', 59938], ['ood', 52697], ['id', 9078], ['ood', 24330]], 'labels': [6, 7, 8, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9221570491790771})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7835495471954346})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7805105447769165})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7831696271896362})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8978780508041382})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8336156010627747})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8761, 'crossentropy': 0.688205810546875}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 808], ['ood', 24903], ['ood', 5419], ['ood', 52853], ['id', 7098]], 'labels': [0, 4, 5, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9294431805610657})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7762844562530518})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7937747240066528})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.731846809387207})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7822666168212891})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.919947624206543})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7744568586349487})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8836, 'crossentropy': 0.694280126953125}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 44077], ['id', 2113], ['ood', 54478], ['ood', 42747], ['ood', 54835]], 'labels': [2, 6, 2, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8702629804611206})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7303366661071777})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6650861501693726})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6932045817375183})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7859941720962524})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7898073196411133})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8897, 'crossentropy': 0.6258189453125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 30922], ['ood', 43560], ['ood', 11052], ['ood', 52884], ['ood', 29744]], 'labels': [9, 8, 8, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.8708695769309998})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7096449136734009})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.710527241230011})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.716047465801239})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7366263270378113})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8656, 'crossentropy': 0.66563017578125}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 57642], ['id', 45122], ['ood', 9067], ['ood', 11290], ['id', 29317]], 'labels': [4, 8, 5, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0038156509399414})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7593357563018799})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7869027853012085})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8135170936584473})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8079813122749329})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8584, 'crossentropy': 0.7100845703125}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 44064], ['id', 42244], ['id', 5576], ['ood', 30518], ['id', 45196]], 'labels': [7, 5, 6, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8642348051071167})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7159416675567627})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7105751037597656})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7371947169303894})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7004891633987427})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6660499572753906})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.765670895576477})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7352250814437866})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.80080646276474})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8946, 'crossentropy': 0.63064990234375}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 51976], ['ood', 56689], ['id', 3537], ['id', 14702], ['ood', 33818]], 'labels': [2, 0, 6, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8804010152816772})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7613354325294495})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7072789669036865})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.826695442199707})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7257380485534668})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7297787666320801})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8858, 'crossentropy': 0.642849658203125}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 5572], ['id', 12499], ['ood', 47708], ['id', 2702], ['id', 10800]], 'labels': [6, 1, 5, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.930895209312439})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7092352509498596})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7041620016098022})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6723350882530212})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6962969899177551})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7800978422164917})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8164530992507935})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.6206759765625}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 46707], ['ood', 50690], ['ood', 53511], ['id', 56470], ['id', 46477]], 'labels': [3, 8, 2, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9219229817390442})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6996061205863953})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7368780374526978})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7555102109909058})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7553871870040894})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8701, 'crossentropy': 0.64060390625}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 7184], ['id', 14213], ['ood', 48634], ['id', 5988], ['ood', 40055]], 'labels': [3, 5, 7, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.9223300218582153})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7160899639129639})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6571162939071655})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6887449622154236})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7274887561798096})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7210457921028137})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.600847021484375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 11584], ['id', 34467], ['id', 44783], ['id', 18867], ['id', 39237]], 'labels': [0, 1, 5, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.9032313823699951})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7058601975440979})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7227973937988281})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7068407535552979})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6744862794876099})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7486002445220947})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8410944938659668})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8116881847381592})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.639128271484375}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 54831], ['id', 43518], ['id', 9724], ['id', 5233], ['ood', 26968]], 'labels': [9, 6, 7, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8654907941818237})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.628244161605835})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6472607851028442})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.732695996761322})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.665973424911499})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.600824853515625}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 49457], ['ood', 56607], ['id', 35844], ['id', 22945], ['ood', 24636]], 'labels': [8, 6, 6, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8101969361305237})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6447783708572388})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6148145794868469})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6185034513473511})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7803994417190552})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.648176372051239})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.564812939453125}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 54022], ['id', 58224], ['ood', 57357], ['id', 55276], ['ood', 23485]], 'labels': [7, 6, 5, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8623428344726562})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.674293041229248})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7535033226013184})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6346698999404907})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7061301469802856})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7046157121658325})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7946755886077881})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8968, 'crossentropy': 0.60719306640625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 20946], ['id', 6420], ['ood', 59232], ['ood', 49709], ['ood', 11921]], 'labels': [3, 3, 0, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.914867639541626})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6434013843536377})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6944469213485718})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7464635372161865})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7394896745681763})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.59067841796875}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 12964], ['id', 42642], ['id', 41586], ['id', 53074], ['ood', 13693]], 'labels': [4, 9, 6, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.8525822162628174})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6685925126075745})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7234717607498169})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7472230195999146})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.676160454750061})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.881, 'crossentropy': 0.612980908203125}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 57140], ['id', 24298], ['ood', 18768], ['id', 8918], ['ood', 33208]], 'labels': [6, 4, 7, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7817786931991577})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6400971412658691})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6719865798950195})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6999852061271667})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6379748582839966})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7343551516532898})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7312232255935669})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7256081104278564})
store['active_learning_steps'][56]['training']['best_epoch']=5
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.60972568359375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 6409], ['ood', 13512], ['id', 17241], ['id', 29072], ['ood', 24108]], 'labels': [9, 8, 2, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8571994304656982})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7132664918899536})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6520000696182251})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6712777614593506})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.700771152973175})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7926273345947266})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8903, 'crossentropy': 0.5859138671875}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 56443], ['id', 4454], ['id', 25328], ['ood', 53363], ['id', 16508]], 'labels': [2, 4, 3, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.8861209750175476})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7189927101135254})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6804972887039185})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7004374265670776})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6965359449386597})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6910288333892822})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8912, 'crossentropy': 0.585337548828125}
store['active_learning_steps'][58]['acquisition']={'indices': [['ood', 9197], ['id', 142], ['id', 7424], ['ood', 30931], ['id', 38247]], 'labels': [0, 4, 1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8933447599411011})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6598944664001465})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6388510465621948})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7147910594940186})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6707768440246582})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6577474474906921})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9024, 'crossentropy': 0.57188349609375}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 23288], ['id', 22526], ['id', 1455], ['ood', 36417], ['ood', 10917]], 'labels': [8, 8, 9, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.888614296913147})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6532965898513794})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6298454999923706})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.612486720085144})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6797935962677002})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6968689560890198})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7081518173217773})
store['active_learning_steps'][60]['training']['best_epoch']=4
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.529002685546875}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 14019], ['ood', 44796], ['ood', 41866], ['id', 39152], ['id', 47122]], 'labels': [5, 4, 7, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.846386194229126})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6304551959037781})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5949966907501221})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6387653350830078})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6120216846466064})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6778134703636169})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.561742138671875}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 30338], ['ood', 21749], ['ood', 38428], ['ood', 42064], ['ood', 18568]], 'labels': [6, 8, 5, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9454017877578735})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7429104447364807})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6254841685295105})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6250821948051453})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6073222160339355})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6225372552871704})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5745154619216919})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.751293420791626})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6771739721298218})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7265352606773376})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.560243798828125}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 26716], ['ood', 2921], ['id', 44327], ['ood', 32211], ['ood', 10933]], 'labels': [9, 9, 1, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8168728351593018})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6121521592140198})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6138255596160889})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6099384427070618})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6270575523376465})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6876744031906128})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6689127087593079})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.559015625}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 31339], ['id', 42206], ['ood', 28807], ['id', 50529], ['ood', 42737]], 'labels': [6, 2, 9, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9055674076080322})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.685695469379425})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.64286208152771})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5863626003265381})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6289781332015991})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6574137210845947})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6747119426727295})
store['active_learning_steps'][64]['training']['best_epoch']=4
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8976, 'crossentropy': 0.57085263671875}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 54789], ['id', 31607], ['ood', 9347], ['id', 11193], ['id', 42039]], 'labels': [7, 8, 6, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8372526168823242})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6246048212051392})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6249058246612549})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6422716379165649})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6537033319473267})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8893, 'crossentropy': 0.57876201171875}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 33582], ['id', 39779], ['ood', 58841], ['id', 46071], ['ood', 9289]], 'labels': [1, 8, 8, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8606216907501221})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6320055723190308})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6147251129150391})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6592482328414917})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6045160293579102})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6196308135986328})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6298933029174805})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6366521120071411})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.5746888671875}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 24427], ['ood', 27928], ['id', 50982], ['id', 13516], ['ood', 26659]], 'labels': [7, 6, 3, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.8882057666778564})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6519510746002197})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6033626794815063})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5817845463752747})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5928276181221008})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.638888418674469})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.690326452255249})
store['active_learning_steps'][67]['training']['best_epoch']=4
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.5577798828125}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 1984], ['ood', 29518], ['id', 50750], ['ood', 27595], ['id', 19129]], 'labels': [9, 6, 0, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8858110904693604})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6776702404022217})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6433804631233215})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6947668790817261})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.594460129737854})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6398850679397583})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6679941415786743})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6309430599212646})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.552832666015625}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 16613], ['id', 36827], ['id', 34902], ['ood', 42207], ['ood', 22372]], 'labels': [9, 9, 2, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9612381458282471})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6022144556045532})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5661875009536743})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.610285222530365})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6189843416213989})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5887113809585571})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.53506875}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 57217], ['ood', 57000], ['id', 41323], ['ood', 19475], ['id', 49756]], 'labels': [1, 3, 6, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.8656520843505859})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6257156133651733})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6294757127761841})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6388046741485596})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6245315074920654})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.619377613067627})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7271323204040527})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.599140465259552})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6268007755279541})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7101471424102783})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7542637586593628})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.5907783203125}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 34897], ['id', 54111], ['ood', 617], ['ood', 36299], ['ood', 16924]], 'labels': [6, 5, 2, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8726353645324707})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6083841323852539})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5700322389602661})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6160933971405029})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6731154322624207})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6491585969924927})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.553943017578125}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 54901], ['id', 8370], ['id', 14126], ['id', 49680], ['ood', 26706]], 'labels': [1, 4, 1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7793275713920593})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6343305110931396})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.603792667388916})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6507282257080078})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6406245827674866})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6222189664840698})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.54746357421875}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 21122], ['ood', 30459], ['id', 22423], ['ood', 42996], ['id', 53761]], 'labels': [9, 5, 9, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9282625317573547})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6127934455871582})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5753371119499207})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6028867363929749})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5643031001091003})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6121249198913574})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5858047008514404})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6010006666183472})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.520608056640625}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 12565], ['id', 43169], ['ood', 59698], ['id', 26758], ['ood', 25303]], 'labels': [0, 0, 7, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9182475209236145})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6575140953063965})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5800880193710327})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6017763614654541})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.607177734375})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5738839507102966})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6783517599105835})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5992132425308228})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6280013918876648})
store['active_learning_steps'][74]['training']['best_epoch']=6
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9074, 'crossentropy': 0.54268896484375}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 16575], ['ood', 52113], ['id', 5894], ['id', 39165], ['id', 6851]], 'labels': [9, 7, 8, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9521808624267578})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6244643330574036})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5381467342376709})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5460028052330017})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6379513144493103})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.563370406627655})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.48480009765625}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 25083], ['id', 30377], ['ood', 22593], ['ood', 46106], ['ood', 11346]], 'labels': [9, 3, 2, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9167386293411255})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6628230214118958})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5824722647666931})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5648176670074463})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5601152181625366})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6086463332176208})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5809482336044312})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6112219095230103})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.51645498046875}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 15585], ['ood', 3799], ['ood', 12344], ['ood', 16378], ['ood', 46824]], 'labels': [6, 1, 0, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8490611910820007})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.620769202709198})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5516589879989624})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5652532577514648})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6215436458587646})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5810600519180298})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.5062501953125}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 9463], ['ood', 7454], ['ood', 2091], ['id', 46464], ['id', 58643]], 'labels': [6, 3, 9, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8711910247802734})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.650336503982544})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5913856029510498})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5890616178512573})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6472558975219727})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6243955492973328})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5986257195472717})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.510194677734375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 8899], ['ood', 24718], ['ood', 59165], ['id', 23224], ['ood', 19824]], 'labels': [9, 9, 8, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8538488149642944})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6361217498779297})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6306284666061401})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5812206268310547})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6263346672058105})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5392955541610718})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5865073204040527})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6173558235168457})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5949466228485107})
store['active_learning_steps'][79]['training']['best_epoch']=6
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.5174775390625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 42633], ['id', 26082], ['ood', 29058], ['ood', 19616], ['ood', 14969]], 'labels': [2, 9, 3, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9077054262161255})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6604564189910889})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6374903917312622})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.544529914855957})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5800641775131226})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5827873349189758})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7099279165267944})
store['active_learning_steps'][80]['training']['best_epoch']=4
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9043, 'crossentropy': 0.524043017578125}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 19412], ['id', 47503], ['ood', 7181], ['ood', 8284], ['ood', 18379]], 'labels': [8, 5, 6, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8808561563491821})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6318002939224243})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5279784202575684})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.49852150678634644})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5318499207496643})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5517185926437378})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5275012850761414})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.477132568359375}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 18093], ['ood', 46595], ['ood', 59118], ['ood', 27811], ['ood', 34567]], 'labels': [8, 2, 8, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8555636405944824})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.650107204914093})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6283218860626221})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5845828056335449})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5914525985717773})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6882058382034302})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6135631203651428})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.5293015625}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 45481], ['ood', 46717], ['id', 57258], ['ood', 26930], ['ood', 30230]], 'labels': [8, 0, 9, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8481731414794922})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6455905437469482})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6276243925094604})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6289329528808594})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6031825542449951})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6093798875808716})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6165345907211304})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5890278816223145})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6108085513114929})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5838053226470947})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7896939516067505})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6599635481834412})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6083879470825195})
store['active_learning_steps'][83]['training']['best_epoch']=10
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.570638916015625}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 36100], ['ood', 58648], ['id', 13617], ['ood', 52500], ['ood', 7098]], 'labels': [2, 7, 1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.8698108196258545})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6149959564208984})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6178456544876099})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5782060027122498})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6290684938430786})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6429423093795776})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6304707527160645})
store['active_learning_steps'][84]['training']['best_epoch']=4
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.538388671875}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 13971], ['id', 17726], ['ood', 24307], ['ood', 2777], ['ood', 38784]], 'labels': [9, 0, 1, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.0207624435424805})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6962791085243225})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6011244058609009})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6155484914779663})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6130964159965515})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6362770795822144})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8997, 'crossentropy': 0.55823154296875}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 51831], ['ood', 25205], ['ood', 55573], ['ood', 57895], ['id', 24920]], 'labels': [5, 1, 4, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9700737595558167})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6528259515762329})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5901139974594116})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5767031908035278})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5826789140701294})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5994395017623901})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.561447262763977})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6562913060188293})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5691034197807312})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5955243110656738})
store['active_learning_steps'][86]['training']['best_epoch']=7
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.532185009765625}
