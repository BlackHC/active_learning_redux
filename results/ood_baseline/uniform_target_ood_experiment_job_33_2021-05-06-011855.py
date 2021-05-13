store = {}
store['timestamp']=1620260335
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=33']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=33
store['worker_id']=33
store['num_workers']=40
store['config']={'seed': 46, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
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
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 39745], ['id', 37380], ['id', 37980], ['ood', 9202], ['id', 13704]], 'labels': [5, 5, 0, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7383661270141602})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.130923271179199})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7245218753814697})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5440914630889893})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.686, 'crossentropy': 1.487103125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 47531], ['ood', 11001], ['id', 53946], ['ood', 45655], ['id', 6417]], 'labels': [2, 2, 5, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5918529033660889})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.0128140449523926})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.0682497024536133})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.2751271724700928})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6739, 'crossentropy': 1.51698759765625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 51576], ['id', 47118], ['ood', 1160], ['id', 44692], ['id', 19662]], 'labels': [1, 1, 4, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3933203220367432})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.6167675256729126})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.661159873008728})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7674152851104736})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7401, 'crossentropy': 1.21271943359375}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 44276], ['id', 58667], ['ood', 4522], ['id', 14308], ['id', 47053]], 'labels': [2, 3, 2, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4264535903930664})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.7427480220794678})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6915677785873413})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.9673850536346436})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6966, 'crossentropy': 1.2699310546875}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 51550], ['id', 40225], ['ood', 26806], ['id', 55000], ['ood', 47753]], 'labels': [6, 4, 9, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4031388759613037})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4363657236099243})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7444096803665161})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.8750585317611694})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7464, 'crossentropy': 1.1406892578125}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 46252], ['ood', 19090], ['ood', 46483], ['ood', 5497], ['id', 1706]], 'labels': [7, 8, 9, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1341133117675781})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3360166549682617})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.610260009765625})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.6102612018585205})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7699, 'crossentropy': 1.0005453125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 26908], ['id', 14367], ['id', 10673], ['ood', 54866], ['id', 11941]], 'labels': [8, 3, 2, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2702221870422363})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.460619568824768})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.4824280738830566})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.0130274295806885})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7332, 'crossentropy': 1.1740263671875}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 2138], ['id', 45706], ['ood', 30234], ['ood', 34993], ['id', 9255]], 'labels': [0, 8, 9, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2765744924545288})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5103263854980469})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6713166236877441})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.7842650413513184})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7208, 'crossentropy': 1.19117587890625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 40616], ['ood', 50724], ['id', 25684], ['ood', 24604], ['ood', 51693]], 'labels': [6, 5, 6, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2881226539611816})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.343116044998169})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4993423223495483})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.5144106149673462})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7245, 'crossentropy': 1.1298083984375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 9773], ['ood', 27721], ['ood', 30886], ['id', 9163], ['ood', 43023]], 'labels': [0, 3, 5, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0528061389923096})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.2140289545059204})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.3169028759002686})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.4114608764648438})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7891, 'crossentropy': 0.9502345703125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 25828], ['id', 2154], ['ood', 16589], ['id', 44753], ['id', 47832]], 'labels': [9, 1, 7, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.279599666595459})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.461956262588501})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4085208177566528})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6032321453094482})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7183, 'crossentropy': 1.18816494140625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 8416], ['ood', 35304], ['id', 59426], ['ood', 22107], ['id', 28487]], 'labels': [9, 2, 5, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.2095723152160645})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3831877708435059})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.565845251083374})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.6090240478515625})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7429, 'crossentropy': 1.1318927734375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 43726], ['ood', 25434], ['ood', 51348], ['id', 40710], ['ood', 32364]], 'labels': [6, 0, 1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.046966314315796})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.1817494630813599})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1311501264572144})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2949583530426025})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7831, 'crossentropy': 0.9457333984375}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 44586], ['id', 55316], ['id', 20832], ['ood', 2951], ['id', 17214]], 'labels': [8, 2, 2, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.0750148296356201})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2018455266952515})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2865464687347412})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2943730354309082})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7898, 'crossentropy': 0.95994873046875}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 22132], ['id', 54159], ['id', 22248], ['id', 50916], ['ood', 46769]], 'labels': [1, 5, 1, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.1408588886260986})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.2213892936706543})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.3025965690612793})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4230163097381592})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7741, 'crossentropy': 1.01747958984375}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 47698], ['id', 24291], ['id', 25497], ['id', 15229], ['ood', 9084]], 'labels': [1, 7, 0, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0823023319244385})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0902397632598877})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2777760028839111})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2561410665512085})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7978, 'crossentropy': 0.91866494140625}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 21311], ['ood', 30316], ['ood', 5315], ['id', 58679], ['id', 34671]], 'labels': [3, 0, 5, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0404002666473389})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2369961738586426})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.3118404150009155})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3075954914093018})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7999, 'crossentropy': 0.93048330078125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 58443], ['ood', 47299], ['id', 34801], ['id', 25245], ['ood', 33415]], 'labels': [6, 4, 9, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.045345664024353})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9867987632751465})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2340933084487915})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1970036029815674})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.222137689590454})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8155, 'crossentropy': 0.88534912109375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 14657], ['ood', 39838], ['id', 51973], ['ood', 55038], ['id', 45290]], 'labels': [4, 5, 5, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9907737374305725})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9998818635940552})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.129594326019287})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0988836288452148})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7987, 'crossentropy': 0.9155564453125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 40530], ['ood', 10960], ['id', 43323], ['id', 6603], ['ood', 4488]], 'labels': [5, 9, 1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9858289957046509})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0460176467895508})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1683180332183838})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2533609867095947})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8071, 'crossentropy': 0.9101515625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 54266], ['id', 8384], ['ood', 30186], ['id', 14348], ['ood', 40776]], 'labels': [9, 6, 5, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9124819040298462})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0738009214401245})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0680757761001587})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9951270818710327})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8236, 'crossentropy': 0.82798447265625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 58353], ['ood', 38656], ['id', 49085], ['ood', 51092], ['id', 20005]], 'labels': [0, 4, 0, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9251341223716736})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9458342790603638})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0187275409698486})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1846826076507568})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8247, 'crossentropy': 0.82230673828125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 51506], ['ood', 6119], ['ood', 38741], ['id', 8551], ['id', 56867]], 'labels': [2, 9, 3, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0114330053329468})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9853832721710205})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9377760887145996})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1234242916107178})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9839178323745728})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0659153461456299})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8424, 'crossentropy': 0.84572705078125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 17767], ['ood', 50862], ['id', 30271], ['id', 27315], ['id', 17251]], 'labels': [6, 7, 7, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9025639295578003})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9074532389640808})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9544954299926758})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0271010398864746})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8311, 'crossentropy': 0.7859880859375}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 1728], ['ood', 37809], ['ood', 8181], ['ood', 32647], ['id', 18712]], 'labels': [5, 7, 8, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9341007471084595})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.926120936870575})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9823899269104004})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.020108699798584})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1375466585159302})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8277, 'crossentropy': 0.79411767578125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 43354], ['ood', 13118], ['ood', 25159], ['id', 46019], ['ood', 32426]], 'labels': [2, 4, 6, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.887370765209198})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8617815971374512})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.944896936416626})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0279104709625244})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0854142904281616})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8326, 'crossentropy': 0.78476865234375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 22906], ['ood', 32909], ['id', 49268], ['id', 3681], ['ood', 34218]], 'labels': [3, 2, 0, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9053915739059448})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9057133197784424})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9731394052505493})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0028696060180664})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8261, 'crossentropy': 0.814845263671875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 58277], ['id', 12459], ['id', 40605], ['ood', 44008], ['ood', 54449]], 'labels': [2, 1, 1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8836081027984619})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9248459339141846})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9647567272186279})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9473762512207031})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8331, 'crossentropy': 0.8210837890625}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 7582], ['id', 50326], ['id', 52028], ['ood', 34320], ['ood', 34991]], 'labels': [2, 1, 0, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9114825129508972})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9430093169212341})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9442379474639893})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.053929090499878})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8167, 'crossentropy': 0.85383056640625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 40199], ['id', 39699], ['id', 40655], ['ood', 28540], ['id', 5095]], 'labels': [0, 1, 3, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8469686508178711})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8536220788955688})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8958919048309326})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9253077507019043})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8284, 'crossentropy': 0.78875849609375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 19047], ['id', 25910], ['id', 50160], ['id', 1989], ['ood', 620]], 'labels': [9, 1, 6, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.875095784664154})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8594168424606323})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9492059350013733})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9643550515174866})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0200647115707397})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8319, 'crossentropy': 0.796036181640625}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 30708], ['ood', 41272], ['ood', 35293], ['ood', 23470], ['id', 1027]], 'labels': [1, 8, 4, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8550969362258911})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8881163597106934})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8829350471496582})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0240321159362793})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8219, 'crossentropy': 0.819322265625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 38213], ['ood', 32011], ['id', 7457], ['id', 55625], ['ood', 3310]], 'labels': [7, 3, 5, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9383255243301392})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0044078826904297})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0543642044067383})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.024287223815918})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8081, 'crossentropy': 0.875768359375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 3553], ['ood', 27387], ['id', 13212], ['id', 52051], ['id', 42897]], 'labels': [2, 2, 3, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.939184844493866})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9252699613571167})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.037149429321289})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0136651992797852})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1622707843780518})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8306, 'crossentropy': 0.78937373046875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 47010], ['ood', 52186], ['ood', 33408], ['ood', 47484], ['ood', 4791]], 'labels': [9, 1, 5, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8550518751144409})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9090468883514404})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9135873317718506})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0383331775665283})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8205, 'crossentropy': 0.82691611328125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 33431], ['id', 19726], ['id', 59954], ['ood', 33443], ['ood', 29369]], 'labels': [7, 0, 1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9302971959114075})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.920261025428772})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9032232165336609})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9784944653511047})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0689239501953125})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.135987639427185})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 0.758514453125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 48448], ['ood', 58984], ['id', 44361], ['ood', 1738], ['ood', 41322]], 'labels': [4, 9, 9, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9644020795822144})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9362587928771973})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0024363994598389})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9042942523956299})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1071338653564453})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0616064071655273})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.240065336227417})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8532, 'crossentropy': 0.8350873046875}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 33500], ['ood', 10861], ['id', 16013], ['ood', 14870], ['id', 50243]], 'labels': [0, 5, 3, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9084585905075073})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8733597993850708})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.846524715423584})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0017540454864502})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9657719135284424})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1239345073699951})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8519, 'crossentropy': 0.745168408203125}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 6448], ['ood', 58231], ['id', 5851], ['ood', 29147], ['id', 43275]], 'labels': [4, 2, 7, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8697335124015808})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7700183391571045})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9683771133422852})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9164679646492004})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0581587553024292})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8646, 'crossentropy': 0.671035302734375}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 46956], ['ood', 9654], ['ood', 31428], ['ood', 27938], ['id', 33892]], 'labels': [2, 8, 5, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9040629863739014})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7918521761894226})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7916296720504761})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8877521753311157})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.847419023513794})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9482027888298035})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8639, 'crossentropy': 0.71418408203125}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 12868], ['ood', 39024], ['id', 4087], ['ood', 16184], ['id', 42440]], 'labels': [3, 9, 6, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7960042953491211})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7641266584396362})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7982639074325562})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7990515232086182})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8666948676109314})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8578, 'crossentropy': 0.691799072265625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 30996], ['id', 7707], ['ood', 16848], ['ood', 43676], ['ood', 29573]], 'labels': [1, 0, 8, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.927919864654541})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.929030179977417})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9343875646591187})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8873022794723511})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9238756895065308})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1657816171646118})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0702342987060547})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8582, 'crossentropy': 0.7760314453125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 58815], ['id', 21775], ['ood', 35079], ['id', 8393], ['ood', 14025]], 'labels': [6, 3, 8, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9100264310836792})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8484344482421875})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8467896580696106})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8447935581207275})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9421201944351196})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.945679783821106})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8699084520339966})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8503, 'crossentropy': 0.7810314453125}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 43424], ['ood', 12745], ['ood', 9828], ['ood', 49910], ['id', 59640]], 'labels': [6, 6, 3, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8737870454788208})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8074217438697815})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.759463906288147})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8568027019500732})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8878410458564758})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0774224996566772})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8579, 'crossentropy': 0.69818974609375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 8070], ['ood', 2714], ['ood', 38624], ['id', 55593], ['ood', 3931]], 'labels': [1, 4, 9, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8686873912811279})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7734442949295044})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8450993895530701})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0210130214691162})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0585711002349854})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8501, 'crossentropy': 0.703053515625}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 19616], ['id', 11221], ['id', 48937], ['id', 28588], ['ood', 33886]], 'labels': [9, 3, 4, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.89399254322052})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8053115606307983})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9239243865013123})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8380812406539917})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8447035551071167})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8496, 'crossentropy': 0.713672900390625}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 5094], ['ood', 57594], ['ood', 59731], ['ood', 36606], ['ood', 36744]], 'labels': [2, 1, 3, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.8510135412216187})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7925788760185242})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8031433820724487})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7898755073547363})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9379944801330566})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9445805549621582})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0204572677612305})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8669, 'crossentropy': 0.6868876953125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 32125], ['ood', 9813], ['id', 19121], ['id', 26935], ['ood', 46744]], 'labels': [1, 9, 4, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8641121983528137})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7903240919113159})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8199964761734009})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8098258972167969})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8831285238265991})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8485, 'crossentropy': 0.701181103515625}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 47427], ['ood', 51899], ['ood', 39649], ['id', 21566], ['ood', 11308]], 'labels': [2, 0, 1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8772928714752197})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7789592146873474})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8079230785369873})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8005222678184509})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8380433320999146})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.855, 'crossentropy': 0.704717529296875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 27890], ['ood', 15118], ['ood', 40921], ['id', 44738], ['id', 1132]], 'labels': [6, 3, 8, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.934794545173645})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8041338324546814})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7885503768920898})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8420416116714478})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8471088409423828})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.820493221282959})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8567, 'crossentropy': 0.716047900390625}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 57665], ['id', 33071], ['id', 17949], ['id', 36332], ['ood', 47323]], 'labels': [8, 5, 4, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.958130955696106})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8054335117340088})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7915761470794678})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7816861867904663})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8817956447601318})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9535291194915771})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8804446458816528})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8616, 'crossentropy': 0.71583349609375}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 30864], ['ood', 23091], ['ood', 52755], ['id', 6001], ['id', 26838]], 'labels': [4, 9, 1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9055243134498596})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.731941282749176})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8020318150520325})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8351680040359497})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8075735569000244})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8717, 'crossentropy': 0.6407080078125}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 40189], ['ood', 55041], ['ood', 55938], ['ood', 58144], ['ood', 7624]], 'labels': [6, 7, 4, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8429174423217773})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7739050388336182})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7646337747573853})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7683215737342834})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9059779047966003})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8850061893463135})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8672, 'crossentropy': 0.672332861328125}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 58634], ['id', 26049], ['id', 21153], ['id', 55960], ['id', 10799]], 'labels': [1, 7, 3, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8320306539535522})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7323013544082642})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7637926340103149})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7537692189216614})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8588272333145142})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8655, 'crossentropy': 0.619600830078125}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 13608], ['id', 1982], ['ood', 45380], ['id', 49109], ['id', 13435]], 'labels': [8, 7, 8, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8010849952697754})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.754653811454773})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7324327826499939})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7733405828475952})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7947224974632263})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9248987436294556})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8706, 'crossentropy': 0.648972119140625}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 4884], ['id', 48058], ['ood', 48867], ['ood', 7074], ['ood', 15967]], 'labels': [0, 5, 2, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.913709819316864})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7785172462463379})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7489076852798462})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.744831919670105})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7782876491546631})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9362134337425232})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9018573760986328})
store['active_learning_steps'][56]['training']['best_epoch']=4
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.6461916015625}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 30071], ['ood', 18347], ['id', 48298], ['id', 18800], ['ood', 36537]], 'labels': [2, 4, 7, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8629882335662842})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7400294542312622})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7451581358909607})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7527399063110352})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7512542009353638})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8614, 'crossentropy': 0.671891796875}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 55390], ['ood', 4359], ['id', 43865], ['id', 42817], ['id', 17432]], 'labels': [6, 7, 3, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8535201549530029})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7436678409576416})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7244142889976501})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7952476143836975})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8841845989227295})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8575867414474487})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8706, 'crossentropy': 0.66204892578125}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 20185], ['ood', 54407], ['ood', 37086], ['id', 12644], ['ood', 22608]], 'labels': [5, 1, 7, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8474454879760742})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7332319617271423})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7194653749465942})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.73850417137146})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7988711595535278})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8511802554130554})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8826, 'crossentropy': 0.5999587890625}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 12465], ['ood', 424], ['ood', 8915], ['ood', 5667], ['ood', 20129]], 'labels': [7, 9, 3, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8527340888977051})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7079956531524658})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.777725338935852})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7822580337524414})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8095663189888})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8739, 'crossentropy': 0.634214697265625}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 43337], ['id', 34559], ['id', 24093], ['ood', 52339], ['id', 12260]], 'labels': [7, 2, 5, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8694987297058105})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7712420225143433})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7325522899627686})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7902710437774658})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8649729490280151})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8363651037216187})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8728, 'crossentropy': 0.630625439453125}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 15028], ['ood', 56052], ['ood', 54125], ['ood', 14864], ['id', 14238]], 'labels': [3, 2, 4, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9099267721176147})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7266771793365479})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8167572021484375})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8133136034011841})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.797201931476593})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8621, 'crossentropy': 0.6751111328125}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 25498], ['ood', 38892], ['ood', 4220], ['id', 12249], ['ood', 42169]], 'labels': [4, 9, 6, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9156613349914551})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7710476517677307})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7129886150360107})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8197845220565796})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8496188521385193})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7695645689964294})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8643, 'crossentropy': 0.655866552734375}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 306], ['id', 58280], ['id', 16780], ['id', 13695], ['ood', 49354]], 'labels': [6, 5, 5, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9181873798370361})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7406232953071594})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7953249216079712})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7444359660148621})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8624522686004639})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.864, 'crossentropy': 0.64126279296875}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 35778], ['ood', 39785], ['id', 45334], ['id', 28206], ['id', 14530]], 'labels': [0, 0, 5, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8876292705535889})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7064679861068726})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7262020707130432})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.72813880443573})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8137112855911255})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8624, 'crossentropy': 0.6399662109375}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 54993], ['id', 17470], ['ood', 42706], ['id', 57881], ['ood', 23721]], 'labels': [9, 3, 8, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.843000054359436})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6729525327682495})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6657222509384155})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6844420433044434})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7357900142669678})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6913211345672607})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8847, 'crossentropy': 0.555261181640625}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 12463], ['id', 44783], ['ood', 40243], ['id', 30292], ['ood', 16053]], 'labels': [3, 5, 5, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8151464462280273})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7396448850631714})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6559752821922302})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8058552742004395})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7314085960388184})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7322434186935425})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.886, 'crossentropy': 0.5680521484375}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 2071], ['ood', 34264], ['id', 15067], ['ood', 44203], ['ood', 13317]], 'labels': [1, 0, 2, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8489325642585754})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7481104135513306})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7142528295516968})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7362754940986633})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6864254474639893})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7886722087860107})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.896775484085083})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.885779857635498})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.576605810546875}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 42891], ['id', 45960], ['id', 18537], ['id', 765], ['ood', 30037]], 'labels': [4, 0, 7, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8285349011421204})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7183438539505005})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6571820974349976})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7874587774276733})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8585690259933472})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8085592985153198})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.564872265625}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 31488], ['id', 23415], ['id', 49794], ['ood', 38068], ['id', 53853]], 'labels': [2, 6, 5, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8557332754135132})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6433241963386536})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6793564558029175})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.715336799621582})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.742081880569458})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.889, 'crossentropy': 0.557868896484375}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 27504], ['ood', 57848], ['id', 26880], ['ood', 51856], ['ood', 26069]], 'labels': [1, 5, 3, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8153285384178162})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6573736071586609})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6871182918548584})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7166780233383179})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7283378839492798})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8829, 'crossentropy': 0.58005234375}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 29787], ['id', 9019], ['id', 17103], ['id', 30321], ['ood', 34617]], 'labels': [5, 8, 3, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9212735891342163})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.639724612236023})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7431752681732178})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7029434442520142})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7355436086654663})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.583242822265625}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 2105], ['ood', 19023], ['ood', 26549], ['id', 26379], ['id', 58817]], 'labels': [2, 6, 8, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8009965419769287})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6657201051712036})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6476938724517822})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6264498829841614})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7369300127029419})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7418636083602905})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7458416223526001})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9015, 'crossentropy': 0.537025}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 40839], ['ood', 48263], ['ood', 50723], ['ood', 40610], ['id', 15436]], 'labels': [9, 7, 5, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8763432502746582})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.660507321357727})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6753267049789429})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6867433190345764})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7219692468643188})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8803, 'crossentropy': 0.585430859375}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 54625], ['id', 34558], ['ood', 23879], ['id', 44443], ['ood', 24516]], 'labels': [8, 2, 1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8652185201644897})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6854259967803955})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6688798666000366})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6883206367492676})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7564558982849121})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7024098038673401})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.892, 'crossentropy': 0.53209931640625}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 43798], ['ood', 32398], ['id', 58422], ['id', 23037], ['ood', 14187]], 'labels': [5, 4, 9, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8405129909515381})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6011683940887451})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6238646507263184})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.666536808013916})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7033318877220154})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.534142529296875}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 35523], ['id', 30570], ['id', 7641], ['id', 27694], ['ood', 38175]], 'labels': [9, 2, 6, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8093677163124084})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6232819557189941})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6017414331436157})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6451010704040527})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6287519931793213})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7223616242408752})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8983, 'crossentropy': 0.51262353515625}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 28667], ['ood', 10540], ['id', 32189], ['id', 22142], ['id', 29420]], 'labels': [0, 1, 1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8134034872055054})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6250014901161194})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6729813814163208})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6528580188751221})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7925176620483398})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8927, 'crossentropy': 0.557611083984375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 51407], ['id', 24670], ['id', 22935], ['id', 19475], ['ood', 24281]], 'labels': [6, 7, 5, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8469556570053101})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6196931600570679})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6145035028457642})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6518411040306091})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6874287128448486})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6577157974243164})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.511411328125}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 40248], ['ood', 56636], ['ood', 54369], ['id', 38854], ['ood', 15644]], 'labels': [3, 0, 8, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9138663411140442})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6743452548980713})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6363528966903687})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6253174543380737})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7576582431793213})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6481964588165283})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.763752281665802})
store['active_learning_steps'][80]['training']['best_epoch']=4
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.5296421875}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 18181], ['id', 19271], ['id', 9012], ['id', 8958], ['ood', 40739]], 'labels': [6, 2, 1, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8397322297096252})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6383851170539856})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6238527297973633})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6850724220275879})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7024909853935242})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6304425597190857})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9023, 'crossentropy': 0.518166162109375}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 5885], ['ood', 34764], ['ood', 50577], ['id', 15751], ['ood', 50715]], 'labels': [2, 2, 7, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8265689611434937})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7048724889755249})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5758780241012573})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6143812537193298})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6739822626113892})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6637393236160278})
store['active_learning_steps'][82]['training']['best_epoch']=3
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.515115283203125}
store['active_learning_steps'][82]['acquisition']={'indices': [['ood', 43460], ['id', 6201], ['id', 12323], ['id', 3379], ['ood', 48708]], 'labels': [8, 6, 1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7882958650588989})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6194338798522949})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6203652620315552})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6320559978485107})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6653250455856323})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.885, 'crossentropy': 0.565763623046875}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 55734], ['id', 30712], ['ood', 21895], ['id', 14389], ['id', 47583]], 'labels': [1, 9, 3, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7802506685256958})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5626437664031982})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6162975430488586})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.632856011390686})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6300625801086426})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.5058505859375}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 24318], ['ood', 46478], ['id', 25694], ['ood', 27919], ['id', 23213]], 'labels': [5, 3, 0, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8374456763267517})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6408799290657043})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6212708353996277})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6337101459503174})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6853715181350708})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6592525243759155})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.529944775390625}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 47159], ['id', 10826], ['id', 14840], ['ood', 45450], ['id', 55690]], 'labels': [4, 3, 0, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8466404676437378})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6400249004364014})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6007088422775269})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6441582441329956})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6677780151367188})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7388221025466919})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8993, 'crossentropy': 0.517530810546875}
