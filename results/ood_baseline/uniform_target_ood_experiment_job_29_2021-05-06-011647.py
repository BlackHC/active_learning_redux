store = {}
store['timestamp']=1620260207
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=29']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=29
store['worker_id']=29
store['num_workers']=40
store['config']={'seed': 38, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.15743350982666})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.6802871227264404})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5976855754852295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7688896656036377})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6785, 'crossentropy': 1.9545232421875}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 37294], ['id', 15269], ['ood', 7946], ['id', 3518], ['id', 32826]], 'labels': [9, 6, 6, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9275163412094116})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1856324672698975})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.5479321479797363})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.558042287826538})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6568, 'crossentropy': 1.6807220703125}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 59770], ['id', 30], ['id', 51121], ['ood', 30275], ['id', 23945]], 'labels': [0, 3, 0, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.375373363494873})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.5373125076293945})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.850367546081543})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.9624428749084473})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7068, 'crossentropy': 1.307884375}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 41821], ['ood', 41597], ['id', 13130], ['id', 53721], ['id', 58882]], 'labels': [5, 3, 9, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5060254335403442})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.6736620664596558})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.8953659534454346})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.91908597946167})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7023, 'crossentropy': 1.42737744140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 29786], ['ood', 54712], ['ood', 59087], ['ood', 32948], ['id', 39387]], 'labels': [7, 8, 1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5164015293121338})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8854862451553345})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.7316460609436035})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2686595916748047})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6864, 'crossentropy': 1.5324541015625}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 21128], ['id', 27407], ['ood', 37382], ['ood', 26339], ['id', 26012]], 'labels': [2, 0, 2, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.236565113067627})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5284488201141357})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.468725323677063})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6734352111816406})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7181, 'crossentropy': 1.22133115234375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 54237], ['id', 24673], ['ood', 55644], ['ood', 58679], ['id', 31099]], 'labels': [6, 6, 4, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3541183471679688})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5065360069274902})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.5434881448745728})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5991857051849365})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7178, 'crossentropy': 1.24493037109375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 2597], ['id', 3665], ['ood', 55588], ['ood', 25414], ['id', 44867]], 'labels': [0, 8, 2, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2304292917251587})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.5049461126327515})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.7227221727371216})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7316250801086426})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7256, 'crossentropy': 1.21132822265625}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 40008], ['ood', 12657], ['id', 9230], ['ood', 10977], ['id', 8476]], 'labels': [0, 2, 3, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.201157569885254})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2684869766235352})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5194151401519775})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5976438522338867})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7346, 'crossentropy': 1.18001513671875}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 49101], ['ood', 8049], ['id', 3829], ['id', 41232], ['ood', 16975]], 'labels': [4, 6, 0, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1878478527069092})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.2618184089660645})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4539546966552734})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.758782982826233})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.743, 'crossentropy': 1.14375458984375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 44160], ['ood', 58570], ['id', 35062], ['ood', 4379], ['id', 25812]], 'labels': [7, 9, 5, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1127697229385376})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2221133708953857})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2216359376907349})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.510779619216919})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7441, 'crossentropy': 1.07257666015625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 12697], ['ood', 56315], ['ood', 36613], ['id', 5716], ['id', 29116]], 'labels': [5, 9, 1, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2798676490783691})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.2735841274261475})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4368096590042114})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.5410630702972412})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.5214056968688965})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7447, 'crossentropy': 1.29344111328125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 25410], ['id', 3262], ['ood', 22310], ['id', 11486], ['ood', 36611]], 'labels': [2, 0, 5, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1835002899169922})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.0847735404968262})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.195934534072876})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1781996488571167})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.318359613418579})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.763, 'crossentropy': 1.07504169921875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 58915], ['id', 6245], ['ood', 26397], ['ood', 5261], ['ood', 22758]], 'labels': [8, 0, 4, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1048802137374878})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1402841806411743})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.285714864730835})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2228765487670898})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7539, 'crossentropy': 1.08122421875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 43328], ['id', 43227], ['id', 49589], ['ood', 29163], ['ood', 13901]], 'labels': [5, 1, 3, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.112182378768921})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.03065824508667})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1039574146270752})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0554022789001465})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.252360463142395})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7959, 'crossentropy': 0.9871982421875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 7724], ['id', 16147], ['ood', 34665], ['id', 40025], ['ood', 31055]], 'labels': [6, 9, 4, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9150230884552002})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8913670778274536})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9494746923446655})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0378140211105347})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.083643913269043})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8162, 'crossentropy': 0.86522607421875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 52658], ['ood', 49804], ['ood', 27924], ['ood', 49520], ['ood', 19266]], 'labels': [4, 0, 7, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9999983310699463})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8718122243881226})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9038463830947876})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9788521528244019})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8849458694458008})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8396, 'crossentropy': 0.7822841796875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 5129], ['id', 58614], ['id', 34165], ['ood', 31975], ['ood', 53867]], 'labels': [2, 7, 8, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9640657901763916})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8808330297470093})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.067240595817566})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9816974401473999})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.02030348777771})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8293, 'crossentropy': 0.8353623046875}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 2471], ['ood', 21968], ['ood', 36711], ['id', 47378], ['ood', 46755]], 'labels': [0, 3, 3, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9412859082221985})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.838528037071228})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9096239805221558})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8900184631347656})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9121146202087402})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8435, 'crossentropy': 0.7769427734375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 35087], ['id', 38543], ['ood', 1325], ['id', 33102], ['ood', 45128]], 'labels': [6, 0, 0, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9648537635803223})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.981294572353363})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9811317324638367})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.118467926979065})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.812, 'crossentropy': 0.9087248046875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 58540], ['ood', 49974], ['id', 32287], ['id', 31645], ['id', 7098]], 'labels': [5, 7, 5, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8957071304321289})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8815571069717407})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9285886287689209})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9482227563858032})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0509953498840332})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8166, 'crossentropy': 0.8490068359375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 11349], ['id', 51513], ['ood', 31597], ['ood', 36440], ['id', 17092]], 'labels': [7, 8, 7, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.961747407913208})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.975085437297821})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.961089015007019})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0635415315628052})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.096282720565796})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8877562284469604})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1267955303192139})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0759947299957275})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1637552976608276})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8486, 'crossentropy': 0.83777734375}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 23088], ['id', 22224], ['id', 44596], ['ood', 28361], ['ood', 26564]], 'labels': [0, 0, 3, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.0333338975906372})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9467024207115173})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8987427949905396})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9447543025016785})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0373344421386719})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1477115154266357})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8241, 'crossentropy': 0.8719126953125}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 21650], ['ood', 24974], ['ood', 8787], ['ood', 24210], ['ood', 46607]], 'labels': [9, 9, 4, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9755624532699585})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9350099563598633})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8929019570350647})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9314666986465454})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1413993835449219})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9948921203613281})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8204, 'crossentropy': 0.92802060546875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 32907], ['ood', 17954], ['ood', 30293], ['ood', 10270], ['ood', 28761]], 'labels': [8, 3, 8, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0385124683380127})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.855352520942688})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9073432087898254})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0177947282791138})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0291905403137207})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8108, 'crossentropy': 0.83242490234375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 37940], ['id', 29513], ['id', 50151], ['id', 18588], ['ood', 27170]], 'labels': [3, 9, 0, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9239615201950073})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8031546473503113})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8460764288902283})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9529609084129333})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.97039794921875})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8368, 'crossentropy': 0.759562158203125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 21146], ['ood', 18681], ['id', 49755], ['ood', 38359], ['id', 36562]], 'labels': [1, 3, 7, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0219571590423584})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8449792861938477})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9377317428588867})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9773102402687073})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0857131481170654})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8207, 'crossentropy': 0.80357548828125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 50729], ['id', 1315], ['id', 36760], ['ood', 57590], ['id', 15452]], 'labels': [0, 3, 7, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0280952453613281})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8415661454200745})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8831110000610352})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9998030662536621})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0870258808135986})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8145, 'crossentropy': 0.885578125}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 53729], ['ood', 49067], ['ood', 53055], ['ood', 54288], ['ood', 10106]], 'labels': [2, 1, 1, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.9982587695121765})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7641486525535583})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8176939487457275})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9687149524688721})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9679704904556274})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8472, 'crossentropy': 0.741274072265625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 5733], ['ood', 23326], ['id', 24157], ['id', 48574], ['ood', 52243]], 'labels': [2, 4, 6, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9777384400367737})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9060360193252563})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9151018261909485})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9567934274673462})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9449907541275024})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8399, 'crossentropy': 0.798716259765625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 4719], ['ood', 10320], ['ood', 17984], ['id', 8392], ['ood', 50026]], 'labels': [3, 2, 1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9185066223144531})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7687788009643555})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.812370777130127})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9243559241294861})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7982514500617981})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8455, 'crossentropy': 0.710413330078125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 3584], ['id', 32496], ['ood', 43898], ['ood', 34826], ['ood', 22422]], 'labels': [8, 1, 6, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9604963064193726})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8702753186225891})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7594937086105347})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8013575673103333})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9169059991836548})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9372357130050659})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8524, 'crossentropy': 0.736671826171875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 25469], ['ood', 701], ['id', 55141], ['ood', 53636], ['ood', 46937]], 'labels': [7, 3, 4, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9423872232437134})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7774093747138977})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7393256425857544})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7435131072998047})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9024292230606079})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8979324102401733})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8692, 'crossentropy': 0.697071728515625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 7843], ['ood', 24838], ['id', 41777], ['ood', 16564], ['ood', 47513]], 'labels': [4, 5, 1, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9067034721374512})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7582550048828125})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8016481399536133})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7924423217773438})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8551880121231079})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8683, 'crossentropy': 0.67358369140625}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 37166], ['id', 31420], ['id', 32378], ['id', 23370], ['ood', 4782]], 'labels': [8, 1, 1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9340095520019531})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7652713060379028})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7969595193862915})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8114072680473328})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7661558389663696})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8503, 'crossentropy': 0.726184619140625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 3534], ['id', 41518], ['id', 45065], ['ood', 42519], ['ood', 26034]], 'labels': [0, 1, 9, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9377480745315552})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7239131331443787})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7761027812957764})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8652865886688232})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8643874526023865})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8636, 'crossentropy': 0.72055732421875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 16247], ['id', 8144], ['ood', 59838], ['id', 20949], ['id', 51017]], 'labels': [7, 7, 8, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9391366839408875})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7560254335403442})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7599194049835205})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7524173259735107})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7893834710121155})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8209774494171143})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8316384553909302})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8725, 'crossentropy': 0.691419873046875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 45412], ['ood', 53135], ['id', 53151], ['ood', 30558], ['ood', 23154]], 'labels': [2, 3, 9, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8735363483428955})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7554999589920044})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7385290265083313})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7711485028266907})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9079011678695679})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.846321702003479})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8753, 'crossentropy': 0.66287265625}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 28364], ['id', 46003], ['id', 20128], ['id', 43818], ['id', 1016]], 'labels': [1, 6, 0, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8624207377433777})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7417620420455933})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7367473244667053})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7384204864501953})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7849925756454468})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7956202030181885})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8572, 'crossentropy': 0.7142673828125}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 15283], ['ood', 29160], ['ood', 12423], ['ood', 22082], ['id', 39690]], 'labels': [0, 0, 3, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9125181436538696})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7109017372131348})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7153847813606262})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7763533592224121})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8087500929832458})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8685, 'crossentropy': 0.71579326171875}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 6751], ['ood', 17036], ['id', 44551], ['ood', 30686], ['ood', 8026]], 'labels': [0, 9, 0, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8726210594177246})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6931402683258057})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6671143174171448})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7181328535079956})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8063300251960754})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8155571222305298})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8795, 'crossentropy': 0.628860107421875}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 49061], ['ood', 26646], ['ood', 58468], ['id', 35307], ['ood', 45144]], 'labels': [2, 6, 7, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8739067912101746})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7477383613586426})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7902196645736694})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7882455587387085})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7390123605728149})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7503492832183838})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7847504615783691})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8040830492973328})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.885, 'crossentropy': 0.7336751953125}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 26051], ['id', 29193], ['id', 45347], ['id', 58987], ['ood', 584]], 'labels': [6, 4, 2, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8905987739562988})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6996209025382996})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6688446998596191})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7460107207298279})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7898106575012207})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7834832072257996})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8908, 'crossentropy': 0.6119541015625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 8452], ['id', 24998], ['id', 48978], ['id', 58051], ['ood', 9205]], 'labels': [1, 9, 3, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8200329542160034})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6913888454437256})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6525455117225647})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7195717096328735})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7575911283493042})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7378954887390137})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.89, 'crossentropy': 0.606616259765625}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 6221], ['id', 777], ['id', 40265], ['ood', 11629], ['id', 19273]], 'labels': [7, 8, 8, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8962012529373169})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6493920087814331})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.674148440361023})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6760300397872925})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6724528670310974})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.61988564453125}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 12922], ['id', 7401], ['id', 23266], ['ood', 460], ['ood', 49041]], 'labels': [3, 6, 9, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.894206702709198})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6938855051994324})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6583684682846069})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6686010360717773})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.70704185962677})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7943931818008423})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8894, 'crossentropy': 0.61464599609375}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 58535], ['ood', 5449], ['id', 40392], ['ood', 35681], ['id', 53095]], 'labels': [5, 2, 4, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8349837064743042})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6420747637748718})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6661068201065063})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.635430097579956})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6631115078926086})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6190899610519409})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6699499487876892})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6772568225860596})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7775108814239502})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.619821923828125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 31371], ['id', 56301], ['id', 26465], ['id', 22323], ['id', 15833]], 'labels': [6, 2, 4, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8474396467208862})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6270455718040466})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6491284966468811})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6456592082977295})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6702024936676025})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8924, 'crossentropy': 0.603809130859375}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 5889], ['id', 45840], ['ood', 15249], ['id', 36669], ['ood', 2256]], 'labels': [6, 0, 2, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8376350402832031})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6641734838485718})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6704577207565308})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6288225650787354})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.742607831954956})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.726137101650238})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7037076950073242})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.58806279296875}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 30554], ['id', 43821], ['id', 46177], ['ood', 35399], ['id', 42395]], 'labels': [4, 7, 6, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8995238542556763})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5656615495681763})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5851262807846069})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6228177547454834})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6397094130516052})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.579793505859375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 4393], ['id', 21229], ['ood', 4761], ['id', 33022], ['ood', 11535]], 'labels': [7, 2, 9, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7644345760345459})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5804161429405212})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6134885549545288})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6391907930374146})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6600141525268555})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8895, 'crossentropy': 0.57190419921875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 3606], ['ood', 48075], ['ood', 57635], ['ood', 48066], ['ood', 38424]], 'labels': [3, 3, 7, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8301993608474731})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7158607244491577})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7602347135543823})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6581127643585205})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.698707103729248})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6903491616249084})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6614564657211304})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8924, 'crossentropy': 0.629505908203125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 59716], ['ood', 4372], ['ood', 54770], ['id', 50631], ['id', 51308]], 'labels': [4, 4, 5, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8214336633682251})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6063799858093262})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6424422264099121})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6702103614807129})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6351141929626465})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.559932470703125}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 54193], ['ood', 55246], ['id', 1731], ['ood', 44286], ['ood', 53615]], 'labels': [9, 2, 6, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7925461530685425})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6066712141036987})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.621086061000824})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6669901609420776})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6507641673088074})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8862, 'crossentropy': 0.591594287109375}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 47858], ['id', 14828], ['ood', 55489], ['id', 54772], ['ood', 53001]], 'labels': [7, 5, 7, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8441377282142639})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6438156366348267})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6118485927581787})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6473221182823181})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6466110348701477})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6616266965866089})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.56993388671875}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 38949], ['ood', 18456], ['id', 42231], ['id', 29763], ['ood', 35173]], 'labels': [0, 0, 9, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8871103525161743})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6009471416473389})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5720082521438599})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6315382122993469})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6317640542984009})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6740583181381226})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9027, 'crossentropy': 0.54409970703125}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 39176], ['id', 48767], ['id', 53835], ['id', 51745], ['ood', 22585]], 'labels': [5, 2, 2, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8344651460647583})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.683359682559967})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5881191492080688})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.651792049407959})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6438041925430298})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6461158990859985})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.57635771484375}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 34307], ['ood', 14932], ['ood', 24719], ['id', 16721], ['id', 1687]], 'labels': [7, 5, 7, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8484488725662231})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6187894344329834})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.559667706489563})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5722345113754272})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5581914186477661})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5747889280319214})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5568608045578003})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6177284121513367})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5985437631607056})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7114459276199341})
store['active_learning_steps'][57]['training']['best_epoch']=7
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.521232080078125}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 23937], ['id', 38948], ['ood', 6623], ['id', 821], ['ood', 11295]], 'labels': [1, 8, 0, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7760570645332336})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5943523645401001})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5875831246376038})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6458086967468262})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5982506275177002})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6342754364013672})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.541763818359375}
store['active_learning_steps'][58]['acquisition']={'indices': [['ood', 52781], ['id', 26787], ['ood', 49603], ['id', 52879], ['ood', 31261]], 'labels': [6, 5, 0, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8632996678352356})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6247084736824036})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5982222557067871})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5711709856987})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5327916145324707})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6187617182731628})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6170008778572083})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6581069827079773})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.529316259765625}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 24770], ['ood', 9541], ['id', 22440], ['ood', 28329], ['id', 21183]], 'labels': [4, 0, 0, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7954138517379761})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6690876483917236})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5901680588722229})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.597404420375824})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5879678130149841})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5903774499893188})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5751087665557861})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6124635338783264})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5547899603843689})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6003174185752869})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6304304003715515})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.665587306022644})
store['active_learning_steps'][60]['training']['best_epoch']=9
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.51569345703125}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 24788], ['ood', 11488], ['id', 57274], ['ood', 36874], ['ood', 11726]], 'labels': [7, 0, 9, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8557516932487488})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.610828697681427})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5677015781402588})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6223210096359253})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5652897357940674})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5977015495300293})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6675055623054504})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7162163257598877})
store['active_learning_steps'][61]['training']['best_epoch']=5
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9081, 'crossentropy': 0.528202880859375}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 53580], ['ood', 32402], ['id', 53117], ['id', 20600], ['id', 1478]], 'labels': [8, 5, 0, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8123664855957031})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6006834506988525})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.61455237865448})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6052309274673462})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6005700826644897})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6555772423744202})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6286571025848389})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6248826384544373})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.53980849609375}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 38272], ['id', 41990], ['ood', 52274], ['id', 26785], ['id', 49501]], 'labels': [2, 4, 9, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8454432487487793})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6434455513954163})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6089401841163635})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6723417639732361})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7135373950004578})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6881229877471924})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.540296337890625}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 35732], ['id', 58144], ['ood', 24603], ['ood', 3761], ['id', 16628]], 'labels': [9, 3, 1, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8441123962402344})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6202208995819092})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.602047324180603})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6013178825378418})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6369714736938477})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5633163452148438})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6146341562271118})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6137330532073975})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6593458652496338})
store['active_learning_steps'][64]['training']['best_epoch']=6
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.510544921875}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 52739], ['id', 15653], ['ood', 21401], ['ood', 41699], ['id', 13174]], 'labels': [4, 9, 7, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8229013681411743})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6221902966499329})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6016618609428406})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5057226419448853})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.645126223564148})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6101343631744385})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6400259733200073})
store['active_learning_steps'][65]['training']['best_epoch']=4
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.4839626953125}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 49814], ['ood', 48635], ['id', 50580], ['ood', 50799], ['id', 25169]], 'labels': [0, 5, 6, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8416642546653748})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6145224571228027})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5916717052459717})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.57610023021698})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6404664516448975})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6517763137817383})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6094355583190918})
store['active_learning_steps'][66]['training']['best_epoch']=4
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.534032373046875}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 53514], ['ood', 5762], ['ood', 59519], ['ood', 24759], ['ood', 36075]], 'labels': [3, 1, 0, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8290241956710815})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6260286569595337})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6549715995788574})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5571443438529968})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6104557514190674})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6195453405380249})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6173721551895142})
store['active_learning_steps'][67]['training']['best_epoch']=4
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.487949365234375}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 38787], ['id', 41377], ['id', 14618], ['id', 32539], ['id', 49092]], 'labels': [1, 9, 6, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7962648272514343})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5740531086921692})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5495566129684448})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5802395343780518})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5892003774642944})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6612869501113892})
store['active_learning_steps'][68]['training']['best_epoch']=3
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.49193427734375}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 33033], ['ood', 8273], ['ood', 59151], ['ood', 4499], ['ood', 48498]], 'labels': [1, 0, 1, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8578792810440063})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6247299313545227})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5609833002090454})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5598649978637695})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.623052716255188})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.639367938041687})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6065489053726196})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.50251708984375}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 44339], ['id', 47884], ['id', 31274], ['id', 45396], ['id', 46731]], 'labels': [5, 4, 3, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8671058416366577})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5811228156089783})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5873650908470154})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6161715984344482})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6254035234451294})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9065, 'crossentropy': 0.55340283203125}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 383], ['ood', 40628], ['id', 22872], ['id', 21835], ['ood', 1276]], 'labels': [0, 5, 6, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8019982576370239})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5654959678649902})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6147139668464661})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6747699975967407})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.625197172164917})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.5261814453125}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 14644], ['id', 47936], ['id', 14587], ['ood', 49395], ['ood', 26801]], 'labels': [1, 8, 4, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8426084518432617})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5907521843910217})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5654475688934326})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6369508504867554})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5929796695709229})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6016475558280945})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.902, 'crossentropy': 0.555995849609375}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 46603], ['id', 32024], ['id', 32849], ['ood', 40420], ['id', 39995]], 'labels': [8, 2, 7, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8169018030166626})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5755367279052734})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5293020009994507})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5282082557678223})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5182651281356812})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5604069828987122})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5714510083198547})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5575507879257202})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.468463330078125}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 37524], ['id', 50792], ['id', 8959], ['ood', 9849], ['id', 167]], 'labels': [3, 7, 7, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8177978992462158})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6411727666854858})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5569953322410583})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.563589334487915})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5242931842803955})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5281767845153809})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5133895874023438})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5777058601379395})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5681939125061035})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.602320671081543})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.4789265625}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 14375], ['id', 15940], ['ood', 9494], ['id', 17979], ['id', 45929]], 'labels': [1, 1, 5, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8276921510696411})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.580024242401123})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5714823603630066})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5814416408538818})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5649724006652832})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.605904757976532})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6372731328010559})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6345044374465942})
store['active_learning_steps'][75]['training']['best_epoch']=5
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.500856103515625}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 31318], ['id', 20054], ['ood', 59798], ['ood', 52030], ['id', 4187]], 'labels': [7, 9, 8, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8960422873497009})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5870423913002014})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5802391767501831})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5872893333435059})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5430020093917847})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6336849927902222})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5688204765319824})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6037948727607727})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.486140869140625}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 21005], ['id', 15896], ['id', 53333], ['ood', 56952], ['id', 57924]], 'labels': [5, 6, 7, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7808506488800049})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.563359260559082})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5781563520431519})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.537976861000061})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5601100325584412})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.536723256111145})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5550842881202698})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6026334166526794})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5959228277206421})
store['active_learning_steps'][77]['training']['best_epoch']=6
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.48534443359375}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 18386], ['ood', 31183], ['id', 25209], ['ood', 15187], ['ood', 14192]], 'labels': [2, 7, 3, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7957003712654114})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5606375932693481})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.557600736618042})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5430543422698975})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5410845875740051})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5688199996948242})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6478259563446045})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6162906289100647})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.46517197265625}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 12353], ['ood', 16452], ['ood', 6945], ['id', 38898], ['ood', 21915]], 'labels': [3, 3, 8, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8512622714042664})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6163648366928101})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5786405801773071})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5898730754852295})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.564697265625})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5888994932174683})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5704095363616943})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5863059759140015})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.472918896484375}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 10184], ['id', 50875], ['id', 17583], ['id', 59972], ['id', 26337]], 'labels': [8, 2, 5, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8866579532623291})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6859055757522583})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5821428298950195})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5927834510803223})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6347602605819702})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6114593744277954})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.514100390625}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 58140], ['id', 27076], ['ood', 59139], ['ood', 3686], ['id', 41459]], 'labels': [7, 8, 8, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7857632637023926})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5400421619415283})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5292873382568359})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5278527140617371})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.580763578414917})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5960740447044373})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.564049482345581})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.4533703125}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 3507], ['id', 49298], ['ood', 19945], ['ood', 42460], ['ood', 34108]], 'labels': [1, 9, 2, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9050028324127197})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.596969723701477})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5550775527954102})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5342680215835571})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.580359697341919})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5632786750793457})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.613136887550354})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.46541279296875}
store['active_learning_steps'][82]['acquisition']={'indices': [['ood', 2808], ['id', 9246], ['id', 46467], ['ood', 12648], ['ood', 5966]], 'labels': [1, 2, 4, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8606995344161987})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5483766198158264})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.515746533870697})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4882742464542389})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5653609037399292})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5295888185501099})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5608891248703003})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.446591064453125}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 56633], ['id', 49507], ['id', 58952], ['id', 48904], ['id', 20826]], 'labels': [1, 7, 0, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8572514057159424})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5752627849578857})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5209062099456787})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5106899738311768})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5710306167602539})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6029821634292603})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5482521057128906})
store['active_learning_steps'][84]['training']['best_epoch']=4
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.463576953125}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 32146], ['id', 20250], ['id', 57585], ['ood', 18095], ['ood', 13605]], 'labels': [1, 4, 4, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.822711706161499})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.587865948677063})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5978858470916748})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5920401811599731})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5450625419616699})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6557937860488892})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6634410619735718})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6094138622283936})
store['active_learning_steps'][85]['training']['best_epoch']=5
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.509066455078125}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 4155], ['id', 11842], ['ood', 22892], ['ood', 37525], ['id', 6946]], 'labels': [6, 5, 0, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7523871660232544})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5667483806610107})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5346754789352417})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.511814534664154})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.529532790184021})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5196407437324524})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5229598879814148})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.444741259765625}
