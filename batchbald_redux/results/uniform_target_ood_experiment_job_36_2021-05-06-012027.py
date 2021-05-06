store = {}
store['timestamp']=1620260427
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=36']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=36
store['worker_id']=36
store['num_workers']=40
store['config']={'seed': 52, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.382150173187256})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.741635799407959})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.7662415504455566})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0805437564849854})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.659, 'crossentropy': 2.160066796875}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 7154], ['ood', 8318], ['id', 57627], ['id', 22055], ['ood', 6975]], 'labels': [5, 1, 9, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.6736454963684082})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.8215196132659912})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.0466554164886475})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.122790813446045})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6712, 'crossentropy': 1.49641455078125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 2223], ['ood', 24693], ['ood', 49134], ['ood', 12308], ['id', 1283]], 'labels': [7, 9, 6, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.515214443206787})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.5581974983215332})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7758443355560303})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8276262283325195})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6848, 'crossentropy': 1.381147265625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 43409], ['ood', 24809], ['ood', 47810], ['id', 48020], ['ood', 39210]], 'labels': [5, 2, 6, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3848285675048828})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4549012184143066})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6606965065002441})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.706589698791504})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7194, 'crossentropy': 1.2078162109375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 24876], ['ood', 50445], ['ood', 1770], ['ood', 40572], ['id', 26548]], 'labels': [2, 1, 4, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4430220127105713})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6012341976165771})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6750802993774414})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.7364943027496338})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7003, 'crossentropy': 1.33499208984375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49165], ['id', 2796], ['ood', 53406], ['id', 35588], ['ood', 3891]], 'labels': [8, 3, 9, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2350904941558838})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.256842017173767})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4169963598251343})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.3939802646636963})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7501, 'crossentropy': 1.10477001953125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 26662], ['id', 13783], ['id', 49460], ['id', 40014], ['id', 35032]], 'labels': [3, 5, 5, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2915009260177612})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2752290964126587})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.451695203781128})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.52951979637146})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.5983984470367432})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7507, 'crossentropy': 1.22284736328125}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 54004], ['ood', 22133], ['ood', 17456], ['ood', 5301], ['ood', 31380]], 'labels': [4, 4, 6, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2069387435913086})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.3025046586990356})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.3244478702545166})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.575703501701355})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7505, 'crossentropy': 1.0511396484375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 54005], ['id', 20715], ['id', 57015], ['ood', 8738], ['ood', 6339]], 'labels': [1, 2, 6, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9861608743667603})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.151079773902893})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1494064331054688})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.3150043487548828})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8068, 'crossentropy': 0.89290400390625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 11348], ['ood', 33520], ['ood', 36628], ['ood', 32652], ['ood', 24769]], 'labels': [6, 2, 5, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9714522361755371})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0923707485198975})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.110223650932312})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.112283706665039})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7885, 'crossentropy': 0.90029951171875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 16648], ['ood', 9473], ['ood', 8729], ['ood', 37701], ['ood', 36683]], 'labels': [6, 1, 0, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.146471619606018})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0772714614868164})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2384324073791504})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1713809967041016})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.283231258392334})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7638, 'crossentropy': 1.068122265625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 51695], ['id', 44447], ['ood', 227], ['ood', 50644], ['id', 24067]], 'labels': [3, 4, 5, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0142494440078735})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0307049751281738})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0711991786956787})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1762559413909912})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7815, 'crossentropy': 0.94727880859375}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 31717], ['id', 42172], ['id', 38818], ['id', 1912], ['id', 56445]], 'labels': [1, 6, 5, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9322733879089355})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9512519836425781})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9785912036895752})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.201822280883789})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8, 'crossentropy': 0.9171060546875}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 15166], ['id', 18951], ['ood', 53642], ['ood', 4130], ['ood', 40125]], 'labels': [1, 7, 5, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0849705934524536})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9741175174713135})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0141100883483887})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0666402578353882})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0962917804718018})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.814, 'crossentropy': 0.83648154296875}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 50555], ['ood', 22840], ['ood', 31009], ['ood', 25950], ['ood', 29535]], 'labels': [5, 7, 1, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0294830799102783})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.098081111907959})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9895621538162231})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0946687459945679})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0194047689437866})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0825130939483643})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8296, 'crossentropy': 0.89662392578125}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 37342], ['id', 56668], ['ood', 512], ['ood', 13956], ['ood', 56399]], 'labels': [1, 1, 7, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9649982452392578})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9082071781158447})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0121111869812012})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9701517224311829})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.061333179473877})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8028, 'crossentropy': 0.85778271484375}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 59402], ['ood', 44121], ['id', 38285], ['ood', 56380], ['ood', 45958]], 'labels': [3, 2, 5, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9844774007797241})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9348039627075195})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9456651210784912})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9344858527183533})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0385518074035645})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0394651889801025})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1238529682159424})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8289, 'crossentropy': 0.92728486328125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 8323], ['id', 12524], ['id', 32575], ['ood', 53719], ['id', 49788]], 'labels': [0, 7, 0, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0188018083572388})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9654561281204224})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9616488218307495})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1037006378173828})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1021013259887695})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1150825023651123})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8339, 'crossentropy': 0.8736955078125}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 16757], ['id', 999], ['id', 39766], ['id', 5201], ['id', 52322]], 'labels': [7, 6, 6, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9812384843826294})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9418102502822876})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9312805533409119})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0185514688491821})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9472389221191406})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0616836547851562})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8362, 'crossentropy': 0.80156611328125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 14687], ['ood', 27469], ['ood', 8665], ['ood', 38132], ['ood', 32835]], 'labels': [9, 0, 2, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0756711959838867})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9168102145195007})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9926637411117554})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0301389694213867})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9698913097381592})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.826, 'crossentropy': 0.804654345703125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 15517], ['ood', 24197], ['id', 56880], ['id', 52575], ['ood', 1632]], 'labels': [9, 5, 7, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9237782955169678})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.840965747833252})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9777615070343018})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9156278967857361})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9747165441513062})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8394, 'crossentropy': 0.7389685546875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 46665], ['id', 28512], ['id', 43794], ['id', 38922], ['ood', 49948]], 'labels': [5, 5, 2, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0117896795272827})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.05203378200531})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9518723487854004})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9939080476760864})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0826525688171387})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0542287826538086})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8343, 'crossentropy': 0.82546455078125}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 17076], ['id', 30855], ['id', 5261], ['id', 16312], ['id', 50234]], 'labels': [8, 6, 9, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.941213071346283})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8592352271080017})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9682033061981201})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.913738489151001})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9837510585784912})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8362, 'crossentropy': 0.77975224609375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 19687], ['ood', 23668], ['id', 21137], ['ood', 58099], ['id', 33158]], 'labels': [9, 3, 0, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0154292583465576})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.864810585975647})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9541805982589722})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9747576713562012})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9665209650993347})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8322, 'crossentropy': 0.78630185546875}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 52873], ['ood', 39197], ['id', 26586], ['ood', 7378], ['ood', 27484]], 'labels': [4, 1, 9, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9469276666641235})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9293526411056519})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.002719759941101})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0732371807098389})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0881152153015137})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8297, 'crossentropy': 0.83139970703125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 56008], ['ood', 9225], ['ood', 26528], ['ood', 12100], ['id', 22847]], 'labels': [3, 6, 3, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8893419504165649})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8283360004425049})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9016075134277344})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8820453882217407})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9039528369903564})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8498, 'crossentropy': 0.72439453125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 41950], ['id', 22972], ['ood', 34119], ['ood', 41252], ['ood', 22510]], 'labels': [4, 1, 4, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9432714581489563})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8505470752716064})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9632099866867065})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9670614004135132})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9056321382522583})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.848, 'crossentropy': 0.7407482421875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 26624], ['id', 16514], ['id', 2302], ['ood', 4713], ['id', 29755]], 'labels': [2, 7, 8, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0009148120880127})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8704720735549927})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8163950443267822})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8659487962722778})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8582950830459595})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8503138422966003})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8682, 'crossentropy': 0.69540087890625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 13106], ['id', 3815], ['id', 51388], ['ood', 46015], ['ood', 29249]], 'labels': [1, 3, 3, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.919467568397522})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7574520111083984})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8018358945846558})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8030669689178467})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9204232692718506})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8664, 'crossentropy': 0.664085888671875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 1007], ['ood', 49337], ['id', 13531], ['id', 22029], ['ood', 27403]], 'labels': [3, 7, 3, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9148721694946289})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7742785215377808})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7661997079849243})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8360741138458252})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7969687581062317})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8833687901496887})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8649, 'crossentropy': 0.69969326171875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 2335], ['ood', 24083], ['ood', 59533], ['id', 29434], ['ood', 10792]], 'labels': [5, 9, 0, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9682846665382385})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8741995096206665})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8607970476150513})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.879592776298523})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8496785163879395})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.938543438911438})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8940021991729736})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9105405807495117})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8769, 'crossentropy': 0.709841943359375}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 12224], ['id', 15915], ['id', 1093], ['ood', 36544], ['id', 45080]], 'labels': [0, 5, 0, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9353890419006348})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7750585079193115})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8454758524894714})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7761263251304626})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9170940518379211})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8713, 'crossentropy': 0.6717265625}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 41265], ['ood', 665], ['id', 50533], ['ood', 12411], ['id', 50856]], 'labels': [3, 0, 5, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.896048903465271})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8141562342643738})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8566104769706726})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8524119853973389})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8953276872634888})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8634, 'crossentropy': 0.6797734375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 3027], ['ood', 2496], ['id', 37], ['id', 33043], ['ood', 44304]], 'labels': [4, 6, 0, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9684615135192871})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8421348333358765})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8564172983169556})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8753060102462769})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9218669533729553})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8442, 'crossentropy': 0.76931923828125}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 791], ['id', 39961], ['id', 4913], ['ood', 18302], ['ood', 5708]], 'labels': [0, 3, 1, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8967537879943848})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7783602476119995})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.816853940486908})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8500347137451172})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7907721996307373})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.70536796875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49737], ['ood', 27539], ['id', 33618], ['ood', 48727], ['id', 50905]], 'labels': [0, 6, 7, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9639113545417786})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8345129489898682})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7891031503677368})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8513021469116211})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.901989221572876})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8666002154350281})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8674, 'crossentropy': 0.68207744140625}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 48536], ['id', 4856], ['ood', 37364], ['ood', 23662], ['id', 2578]], 'labels': [7, 2, 5, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0449273586273193})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8323361873626709})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8973245024681091})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.912639856338501})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9200342893600464})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8557, 'crossentropy': 0.73369208984375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 23670], ['ood', 34112], ['ood', 57789], ['id', 35334], ['ood', 9141]], 'labels': [7, 8, 5, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0002341270446777})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7866719365119934})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8186527490615845})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8554998636245728})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8522974252700806})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8695, 'crossentropy': 0.673799072265625}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 48073], ['ood', 1588], ['id', 33458], ['id', 41172], ['ood', 14623]], 'labels': [9, 2, 1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0350933074951172})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8478960990905762})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8659236431121826})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8457227945327759})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8284257650375366})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.906446635723114})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9346258044242859})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8475134968757629})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8638, 'crossentropy': 0.770280908203125}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 41386], ['id', 6600], ['ood', 58475], ['id', 56688], ['id', 23443]], 'labels': [8, 7, 6, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8989729881286621})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7709981203079224})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7679443359375})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7759534120559692})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8360755443572998})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8889257907867432})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.87, 'crossentropy': 0.675871044921875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 8061], ['id', 12664], ['id', 37478], ['id', 1631], ['ood', 45059]], 'labels': [4, 1, 3, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.962836503982544})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8343033790588379})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8361996412277222})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.767755389213562})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7817358374595642})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8656033277511597})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7950425744056702})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8779, 'crossentropy': 0.667556591796875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 8909], ['ood', 22579], ['id', 38867], ['ood', 2024], ['id', 23354]], 'labels': [5, 0, 3, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9768629670143127})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.838133692741394})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7999944090843201})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8982394933700562})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8289067149162292})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9126524925231934})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8577, 'crossentropy': 0.737920751953125}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 52564], ['id', 8458], ['ood', 18756], ['ood', 55871], ['id', 2625]], 'labels': [4, 4, 9, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9852525591850281})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7661008834838867})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7591648101806641})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7883143424987793})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8409600257873535})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9235596656799316})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8602, 'crossentropy': 0.70495966796875}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 2393], ['id', 8350], ['ood', 43492], ['id', 12488], ['id', 9535]], 'labels': [8, 3, 4, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9328219890594482})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7149665355682373})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8017001152038574})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7354780435562134})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8601618409156799})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8517, 'crossentropy': 0.6954892578125}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 41151], ['ood', 7034], ['id', 41973], ['ood', 10107], ['id', 35960]], 'labels': [7, 4, 8, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9685540199279785})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7910588979721069})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7721115350723267})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7211080193519592})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7794429063796997})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8089197874069214})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8183218836784363})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8719, 'crossentropy': 0.673707568359375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 33447], ['ood', 48368], ['id', 39182], ['id', 18925], ['ood', 18042]], 'labels': [8, 2, 4, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9444762468338013})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7628538608551025})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.749565601348877})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7560106515884399})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7118188142776489})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.777082085609436})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.752509355545044})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8307968378067017})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8814, 'crossentropy': 0.65229951171875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 47840], ['ood', 31802], ['ood', 43579], ['id', 1614], ['ood', 21782]], 'labels': [6, 1, 7, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8655266761779785})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7275524139404297})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.724723219871521})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7762434482574463})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7759115695953369})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7654767036437988})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8738, 'crossentropy': 0.636573876953125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 52644], ['id', 45341], ['id', 32255], ['ood', 40223], ['ood', 21874]], 'labels': [7, 2, 6, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9192594289779663})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8018887042999268})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.650179386138916})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7212967872619629})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6906099915504456})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7852513194084167})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8864, 'crossentropy': 0.58499765625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 40443], ['id', 56462], ['id', 12392], ['id', 40633], ['id', 36261]], 'labels': [1, 7, 3, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9556334018707275})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7501026391983032})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8070405721664429})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7678351402282715})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.774077296257019})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8644, 'crossentropy': 0.64918056640625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 42436], ['ood', 10833], ['ood', 49471], ['id', 50036], ['id', 46918]], 'labels': [5, 0, 9, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8590874075889587})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.686072826385498})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6692859530448914})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6689410209655762})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6519219279289246})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6466772556304932})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7529773712158203})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7021082639694214})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.779941201210022})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.55357138671875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 5288], ['id', 30272], ['id', 17873], ['ood', 16755], ['id', 55826]], 'labels': [7, 4, 2, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.885603666305542})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6616055965423584})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6571876406669617})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7875244617462158})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7090659737586975})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.717534065246582})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8914, 'crossentropy': 0.62291416015625}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 10453], ['id', 10941], ['id', 46979], ['ood', 20571], ['id', 27444]], 'labels': [9, 2, 3, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9317823648452759})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6843839287757874})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.73587566614151})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7427887320518494})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7397512197494507})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8869, 'crossentropy': 0.605937841796875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 49769], ['ood', 53834], ['ood', 18814], ['id', 51535], ['ood', 50156]], 'labels': [0, 0, 3, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.947214663028717})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6769053936004639})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6721154451370239})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6939067840576172})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6619398593902588})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.814831554889679})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8150426745414734})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7354059815406799})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.593992333984375}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 6341], ['ood', 50055], ['id', 3338], ['id', 58480], ['ood', 1413]], 'labels': [7, 2, 8, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9334985017776489})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7242488265037537})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7051175236701965})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.73136305809021})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7217411994934082})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7414082288742065})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8859, 'crossentropy': 0.6050412109375}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 2219], ['id', 10006], ['id', 55982], ['ood', 15849], ['id', 12602]], 'labels': [9, 1, 2, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8342186808586121})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6781339645385742})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6552003622055054})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6791841983795166})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.695116400718689})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6883805990219116})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8958, 'crossentropy': 0.5867005859375}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 7278], ['id', 56243], ['id', 4964], ['id', 34627], ['id', 56300]], 'labels': [2, 2, 7, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8798772692680359})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6695682406425476})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6761096715927124})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6493653655052185})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.599908709526062})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6891335248947144})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6607828736305237})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7320057153701782})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.546791845703125}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 7099], ['id', 19415], ['id', 23624], ['id', 16198], ['id', 6092]], 'labels': [3, 2, 9, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8735860586166382})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6794646978378296})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6434564590454102})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6649491786956787})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7422595024108887})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6530084609985352})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.582577734375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 47620], ['id', 39553], ['ood', 39829], ['ood', 11746], ['id', 49193]], 'labels': [8, 3, 9, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8756554126739502})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6506200432777405})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6675215363502502})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6465426087379456})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7112008333206177})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6410486698150635})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7187097072601318})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.638727068901062})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6572698354721069})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6671617031097412})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.66145920753479})
store['active_learning_steps'][57]['training']['best_epoch']=8
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.5865564453125}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 50922], ['ood', 47507], ['id', 18440], ['id', 58693], ['id', 44727]], 'labels': [8, 7, 5, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8724915981292725})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6720579862594604})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6053307056427002})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6334491968154907})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.626150369644165})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6033042073249817})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6898654699325562})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6389424800872803})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7731514573097229})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.573078662109375}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 22919], ['id', 44026], ['ood', 32089], ['ood', 41653], ['ood', 5364]], 'labels': [8, 9, 5, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7987205386161804})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6142629981040955})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.550946831703186})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5578458309173584})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5797082185745239})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6356408596038818})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.5015515625}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 23618], ['id', 600], ['id', 21171], ['id', 29983], ['id', 4264]], 'labels': [4, 9, 1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8368297815322876})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6135212182998657})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6193457245826721})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.603541374206543})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5601697564125061})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5616946220397949})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6192511916160583})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6580448150634766})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.51582451171875}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 3792], ['ood', 47485], ['ood', 7763], ['id', 19482], ['id', 24964]], 'labels': [8, 3, 3, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8664378523826599})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6574254035949707})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.614716649055481})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5889389514923096})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6629889011383057})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5877360105514526})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6912180185317993})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6635971069335938})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6090182065963745})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9041, 'crossentropy': 0.58554248046875}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 45462], ['id', 3473], ['id', 47066], ['id', 904], ['ood', 44073]], 'labels': [2, 1, 8, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.792473554611206})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6028344631195068})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.620108425617218})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5758694410324097})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6404457092285156})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6263296008110046})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7070299386978149})
store['active_learning_steps'][62]['training']['best_epoch']=4
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.524917578125}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 27033], ['ood', 29569], ['ood', 51243], ['ood', 50774], ['ood', 51675]], 'labels': [2, 4, 6, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8139286041259766})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5987685918807983})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5695163607597351})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.549052357673645})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5772430896759033})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5927231311798096})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6201815605163574})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.5117109375}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 9602], ['id', 4542], ['ood', 21868], ['ood', 38506], ['id', 19456]], 'labels': [3, 2, 6, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9036008715629578})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.652631938457489})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6408256888389587})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6429437398910522})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7214069366455078})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.717361569404602})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8963, 'crossentropy': 0.580649609375}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 36879], ['id', 45927], ['ood', 29824], ['ood', 1356], ['id', 6243]], 'labels': [2, 1, 3, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8159664869308472})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.604665994644165})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5590003728866577})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5434952974319458})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5961712002754211})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6048523187637329})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5945829153060913})
store['active_learning_steps'][65]['training']['best_epoch']=4
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.503964794921875}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 31498], ['id', 9626], ['ood', 39755], ['id', 35879], ['id', 27292]], 'labels': [1, 4, 3, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8587263822555542})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6511719226837158})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5892390608787537})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.567751407623291})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6275907754898071})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5922161340713501})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5939594507217407})
store['active_learning_steps'][66]['training']['best_epoch']=4
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9152, 'crossentropy': 0.490391552734375}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 26655], ['id', 22255], ['ood', 49322], ['ood', 23768], ['id', 9412]], 'labels': [2, 5, 4, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8042433261871338})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5918372273445129})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5796202421188354})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5629876852035522})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5805284976959229})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5964988470077515})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6525450944900513})
store['active_learning_steps'][67]['training']['best_epoch']=4
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.504375634765625}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 40814], ['id', 11621], ['id', 8088], ['id', 35686], ['id', 56443]], 'labels': [8, 2, 0, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8304575681686401})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5994985103607178})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5654947757720947})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5858727693557739})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5609391331672668})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6041462421417236})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5825214385986328})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6488344669342041})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.49990361328125}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 45127], ['id', 5408], ['id', 37965], ['ood', 44691], ['id', 58684]], 'labels': [8, 3, 9, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8774843215942383})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6211268901824951})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6005443930625916})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5727837681770325})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5945943593978882})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5904394388198853})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6355712413787842})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.500685693359375}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 35319], ['ood', 52248], ['id', 27572], ['ood', 34876], ['ood', 41060]], 'labels': [9, 8, 1, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8616570234298706})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6198979020118713})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5823049545288086})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5613818168640137})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5635369420051575})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.586317777633667})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.588767945766449})
store['active_learning_steps'][70]['training']['best_epoch']=4
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.504552734375}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 890], ['ood', 37936], ['ood', 43787], ['id', 31208], ['ood', 33065]], 'labels': [3, 4, 8, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8134539127349854})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6020524501800537})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5439071655273438})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5454850196838379})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.533076286315918})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5975019335746765})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5912662744522095})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5939891338348389})
store['active_learning_steps'][71]['training']['best_epoch']=5
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.480616455078125}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 36948], ['id', 3851], ['ood', 55137], ['ood', 30285], ['id', 55008]], 'labels': [0, 1, 1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8046560287475586})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6151819229125977})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6099551916122437})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5790344476699829})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6544231176376343})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6457228660583496})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5589206218719482})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6626729965209961})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6263119578361511})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6323072910308838})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.535410791015625}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 57174], ['ood', 35329], ['ood', 2775], ['id', 54758], ['id', 40821]], 'labels': [8, 9, 6, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8172269463539124})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6194853782653809})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5764603614807129})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5712978839874268})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5477359890937805})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5511707067489624})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5672260522842407})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5574394464492798})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.467788916015625}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 28721], ['ood', 7169], ['ood', 39467], ['id', 40088], ['id', 23688]], 'labels': [6, 3, 9, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8000357151031494})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6254962682723999})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5662102699279785})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5769416093826294})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5895366668701172})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5544455051422119})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5670239925384521})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5844810009002686})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5683971047401428})
store['active_learning_steps'][74]['training']['best_epoch']=6
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.506159423828125}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 18579], ['ood', 24639], ['ood', 40995], ['ood', 3343], ['id', 3801]], 'labels': [9, 9, 7, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7913593649864197})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5548728704452515})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5477825403213501})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5470767021179199})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5713163614273071})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5419856309890747})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5375165343284607})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5951387882232666})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5756601095199585})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6018360257148743})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.472895263671875}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 37903], ['id', 19193], ['id', 33079], ['ood', 43095], ['id', 13122]], 'labels': [0, 7, 0, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7645437717437744})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.612825334072113})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5421507358551025})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5839014649391174})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5249173045158386})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5126563906669617})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5485680103302002})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5392972230911255})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5477697849273682})
store['active_learning_steps'][76]['training']['best_epoch']=6
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.462904833984375}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 34352], ['ood', 7376], ['id', 43721], ['ood', 41526], ['id', 50747]], 'labels': [0, 0, 4, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8308984041213989})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5748602151870728})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5481252074241638})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4917754530906677})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5078084468841553})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5399026870727539})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5196794271469116})
store['active_learning_steps'][77]['training']['best_epoch']=4
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.4680298828125}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 57444], ['ood', 58970], ['id', 55736], ['id', 41815], ['ood', 52553]], 'labels': [9, 0, 4, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8115189075469971})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5695862770080566})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5371860265731812})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5134872198104858})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5933358669281006})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5650742053985596})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5630861520767212})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.473552294921875}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 13202], ['ood', 58174], ['ood', 49456], ['id', 51883], ['id', 54009]], 'labels': [2, 6, 9, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8451793193817139})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6572860479354858})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5459651947021484})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5315145254135132})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5595378875732422})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5479179620742798})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5669088363647461})
store['active_learning_steps'][79]['training']['best_epoch']=4
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.508949462890625}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 44492], ['id', 540], ['id', 52742], ['id', 328], ['ood', 16335]], 'labels': [3, 3, 6, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8119455575942993})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5468177199363708})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5391395688056946})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5480678081512451})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5186061859130859})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5252596139907837})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5871812105178833})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5647317171096802})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.495525}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 43629], ['id', 910], ['id', 52230], ['ood', 24680], ['id', 50736]], 'labels': [0, 6, 9, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7796688079833984})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5609588623046875})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.525037944316864})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5398479700088501})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5404341816902161})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5910418033599854})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.466363623046875}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 37879], ['id', 44735], ['ood', 9463], ['ood', 58934], ['id', 369]], 'labels': [7, 6, 6, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.765937328338623})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5831190347671509})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5386334657669067})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5035440325737})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5481791496276855})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5559015274047852})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5675069689750671})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.464362451171875}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 8300], ['ood', 42420], ['ood', 1817], ['ood', 48165], ['id', 49291]], 'labels': [8, 3, 8, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8756357431411743})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5719422698020935})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5831243991851807})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5385414361953735})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5646994113922119})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5444642901420593})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5967414379119873})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.4649759765625}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 59928], ['ood', 40040], ['id', 6766], ['ood', 57363], ['ood', 4652]], 'labels': [3, 7, 3, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.813320517539978})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5754989385604858})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5739172697067261})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5605403780937195})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.568584680557251})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6071746349334717})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.516149640083313})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6076374053955078})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6684526205062866})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.609679102897644})
store['active_learning_steps'][84]['training']['best_epoch']=7
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.46418515625}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 43183], ['id', 48788], ['id', 16276], ['ood', 42480], ['id', 25025]], 'labels': [9, 3, 5, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8024924993515015})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5468636751174927})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.547256588935852})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5708814859390259})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5245018005371094})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6305439472198486})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5946995615959167})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5302362442016602})
store['active_learning_steps'][85]['training']['best_epoch']=5
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.465772216796875}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 45382], ['ood', 18346], ['ood', 49017], ['id', 55586], ['ood', 462]], 'labels': [7, 9, 5, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8059724569320679})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6057205200195312})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5704917907714844})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5490700006484985})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6136247515678406})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5604640245437622})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.563877522945404})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.466579541015625}
