store = {}
store['timestamp']=1620299250
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=30']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=30
store['worker_id']=30
store['num_workers']=40
store['config']={'seed': 40, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4047458171844482})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.583082675933838})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6663312911987305})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.791015148162842})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6761, 'crossentropy': 2.0304546875}
store['active_learning_steps'][0]['acquisition']={'indices': [6510, 30964, 1224, 47506, 39307], 'labels': [7, 8, 6, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.033769369125366})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.3487257957458496})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.512845993041992})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.317762851715088})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7162, 'crossentropy': 1.830602734375}
store['active_learning_steps'][1]['acquisition']={'indices': [48324, 16350, 17084, 52276, 20798], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.0476737022399902})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4769039154052734})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5749130249023438})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6225388050079346})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7054, 'crossentropy': 1.7897125}
store['active_learning_steps'][2]['acquisition']={'indices': [2187, 44395, 37526, 9407, 55175], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.835754632949829})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.2449679374694824})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.0647544860839844})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5112504959106445})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7156, 'crossentropy': 1.713032421875}
store['active_learning_steps'][3]['acquisition']={'indices': [9051, 28292, 21926, 9727, 46830], 'labels': [-1, 1, -1, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.286677598953247})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.183058261871338})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.3521437644958496})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.296351909637451})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.816486358642578})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7297, 'crossentropy': 1.9480189453125}
store['active_learning_steps'][4]['acquisition']={'indices': [55525, 48512, 38315, 40947, 26602], 'labels': [-1, -1, -1, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.936422348022461})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.1636595726013184})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1971635818481445})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.517094612121582})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7159, 'crossentropy': 1.73453671875}
store['active_learning_steps'][5]['acquisition']={'indices': [10306, 8932, 41710, 3462, 55240], 'labels': [9, -1, 2, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8167741298675537})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.4292285442352295})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.9003517627716064})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.697134017944336})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7262, 'crossentropy': 1.6433255859375}
store['active_learning_steps'][6]['acquisition']={'indices': [18394, 45885, 24001, 54689, 41418], 'labels': [-1, -1, 5, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.6127903461456299})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.734776496887207})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.0466160774230957})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.310633659362793})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7561, 'crossentropy': 1.433624609375}
store['active_learning_steps'][7]['acquisition']={'indices': [32217, 40141, 54283, 45944, 11954], 'labels': [5, -1, -1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.1533167362213135})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.378492832183838})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.513845443725586})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.858938694000244})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6994, 'crossentropy': 1.9502234375}
store['active_learning_steps'][8]['acquisition']={'indices': [9871, 50265, 32185, 11362, 6603], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7827379703521729})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.8903241157531738})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2382636070251465})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.004390239715576})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7394, 'crossentropy': 1.3764595703125}
store['active_learning_steps'][9]['acquisition']={'indices': [24011, 41144, 7, 49645, 6668], 'labels': [0, -1, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8648710250854492})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.0245537757873535})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.327052593231201})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.2101540565490723})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7086, 'crossentropy': 1.68739140625}
store['active_learning_steps'][10]['acquisition']={'indices': [59167, 22413, 17555, 35651, 10446], 'labels': [2, -1, -1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.740269422531128})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2276930809020996})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.4414474964141846})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.437283992767334})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7241, 'crossentropy': 1.4662759765625}
store['active_learning_steps'][11]['acquisition']={'indices': [3729, 11385, 46736, 15371, 26762], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.7270443439483643})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.0439698696136475})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.253394842147827})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.480440616607666})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7327, 'crossentropy': 1.6200388671875}
store['active_learning_steps'][12]['acquisition']={'indices': [2981, 55623, 32643, 13551, 48472], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6637663841247559})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1714277267456055})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.182647943496704})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.2823445796966553})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7459, 'crossentropy': 1.46954990234375}
store['active_learning_steps'][13]['acquisition']={'indices': [31894, 10138, 10038, 39053, 25871], 'labels': [1, 2, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6267313957214355})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.9099695682525635})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.3189144134521484})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.6083192825317383})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7401, 'crossentropy': 1.41523203125}
store['active_learning_steps'][14]['acquisition']={'indices': [4707, 11442, 33515, 37740, 5141], 'labels': [4, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4834766387939453})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.8149454593658447})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.024489402770996})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.2649941444396973})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7621, 'crossentropy': 1.24087138671875}
store['active_learning_steps'][15]['acquisition']={'indices': [13948, 43517, 7182, 12273, 46541], 'labels': [-1, 3, 8, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5376050472259521})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.6599102020263672})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.6371883153915405})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.148212432861328})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7655, 'crossentropy': 1.26036025390625}
store['active_learning_steps'][16]['acquisition']={'indices': [4705, 50450, 53184, 43887, 14220], 'labels': [8, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.3273805379867554})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.454448938369751})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.5955469608306885})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.7691621780395508})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7832, 'crossentropy': 1.166736328125}
store['active_learning_steps'][17]['acquisition']={'indices': [33802, 58106, 50407, 54350, 39863], 'labels': [-1, 7, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.3696765899658203})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.4658195972442627})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.6199580430984497})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.7159035205841064})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7822, 'crossentropy': 1.184488671875}
store['active_learning_steps'][18]['acquisition']={'indices': [39057, 11860, 2127, 3662, 2247], 'labels': [1, 0, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3481791019439697})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.5939035415649414})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.6555094718933105})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9439384937286377})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7798, 'crossentropy': 1.20487626953125}
store['active_learning_steps'][19]['acquisition']={'indices': [52121, 13175, 5572, 46039, 10938], 'labels': [-1, 0, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1334178447723389})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2704976797103882})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.3689379692077637})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5102465152740479})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7967, 'crossentropy': 0.9684908203125}
store['active_learning_steps'][20]['acquisition']={'indices': [12083, 40883, 6223, 54894, 6155], 'labels': [-1, 3, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.4594539403915405})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.4767272472381592})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.865586280822754})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.7017734050750732})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7733, 'crossentropy': 1.23562587890625}
store['active_learning_steps'][21]['acquisition']={'indices': [7543, 26198, 29905, 57298, 51139], 'labels': [-1, 5, -1, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2980989217758179})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2873989343643188})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.453068494796753})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.5849971771240234})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6070771217346191})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8242, 'crossentropy': 1.1406033203125}
store['active_learning_steps'][22]['acquisition']={'indices': [40007, 16731, 53975, 53573, 53687], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0727556943893433})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2743561267852783})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.5975010395050049})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.621760606765747})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7775, 'crossentropy': 1.0519119140625}
store['active_learning_steps'][23]['acquisition']={'indices': [48115, 43011, 42691, 29936, 56440], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.078066110610962})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4697482585906982})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5546091794967651})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5432484149932861})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8091, 'crossentropy': 0.9537076171875}
store['active_learning_steps'][24]['acquisition']={'indices': [39859, 22116, 48579, 41442, 55191], 'labels': [-1, 9, 3, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0580790042877197})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3231329917907715})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.4336261749267578})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.5213851928710938})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.827, 'crossentropy': 0.9587216796875}
store['active_learning_steps'][25]['acquisition']={'indices': [4718, 36979, 26819, 47720, 52023], 'labels': [-1, 2, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1086130142211914})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3116079568862915})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.5317997932434082})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6431856155395508})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8063, 'crossentropy': 1.0572564453125}
store['active_learning_steps'][26]['acquisition']={'indices': [14061, 33755, 37756, 58926, 11547], 'labels': [1, 8, 3, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1825075149536133})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2679804563522339})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.4705003499984741})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5019867420196533})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7911, 'crossentropy': 1.09506220703125}
store['active_learning_steps'][27]['acquisition']={'indices': [54080, 38517, 34370, 29159, 24242], 'labels': [0, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.119277834892273})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.212282657623291})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2779055833816528})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3798781633377075})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.813, 'crossentropy': 0.92537021484375}
store['active_learning_steps'][28]['acquisition']={'indices': [36094, 11673, 30940, 4409, 18690], 'labels': [1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0952844619750977})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.193591833114624})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3137503862380981})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.434238076210022})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8025, 'crossentropy': 1.0559650390625}
store['active_learning_steps'][29]['acquisition']={'indices': [33273, 29645, 58679, 15767, 29132], 'labels': [8, 4, 8, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2012085914611816})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2039358615875244})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2552543878555298})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3939242362976074})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8047, 'crossentropy': 1.023095703125}
store['active_learning_steps'][30]['acquisition']={'indices': [12192, 56061, 13635, 47753, 37319], 'labels': [4, -1, 6, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9212250709533691})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0692912340164185})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.204747200012207})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2101027965545654})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.837, 'crossentropy': 0.89519375}
store['active_learning_steps'][31]['acquisition']={'indices': [37294, 2741, 37748, 20731, 1071], 'labels': [4, 6, 9, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7975903749465942})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8890776038169861})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9845014810562134})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0031731128692627})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8626, 'crossentropy': 0.759903076171875}
store['active_learning_steps'][32]['acquisition']={'indices': [18052, 22618, 17055, 44473, 57789], 'labels': [6, 6, 8, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9240408539772034})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9375743865966797})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0121517181396484})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1709084510803223})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8313, 'crossentropy': 0.87849228515625}
store['active_learning_steps'][33]['acquisition']={'indices': [34094, 51821, 30363, 11264, 42936], 'labels': [-1, -1, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9194334745407104})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9818867444992065})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.194428563117981})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0776571035385132})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8271, 'crossentropy': 0.9097880859375}
store['active_learning_steps'][34]['acquisition']={'indices': [33678, 33803, 4065, 4523, 52129], 'labels': [8, -1, 9, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8550676107406616})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9287455081939697})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0511119365692139})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0280382633209229})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8346, 'crossentropy': 0.83317763671875}
store['active_learning_steps'][35]['acquisition']={'indices': [22410, 18174, 17567, 53211, 7343], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8222217559814453})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9167897701263428})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9972774386405945})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.897668182849884})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8596, 'crossentropy': 0.743445068359375}
store['active_learning_steps'][36]['acquisition']={'indices': [20447, 28796, 2084, 26513, 38903], 'labels': [-1, 3, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9312130212783813})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9430327415466309})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.998051643371582})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0844964981079102})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8372, 'crossentropy': 0.84115517578125}
store['active_learning_steps'][37]['acquisition']={'indices': [19852, 22005, 25072, 53648, 46061], 'labels': [5, -1, 8, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8155683279037476})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7729880809783936})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9292204976081848})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8760713338851929})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0848721265792847})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8786, 'crossentropy': 0.73364404296875}
store['active_learning_steps'][38]['acquisition']={'indices': [26859, 5404, 43171, 24575, 9110], 'labels': [-1, 9, -1, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9079087972640991})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8382757306098938})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9074709415435791})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8800426721572876})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.020782232284546})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.889, 'crossentropy': 0.7251380859375}
store['active_learning_steps'][39]['acquisition']={'indices': [14663, 4517, 14140, 50998, 19305], 'labels': [7, 6, 8, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7947221994400024})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7894097566604614})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9315928816795349})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8289368152618408})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0008467435836792})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.873, 'crossentropy': 0.772512255859375}
store['active_learning_steps'][40]['acquisition']={'indices': [29188, 22041, 47317, 27689, 9681], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8228992223739624})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8111083507537842})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7957857847213745})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9129910469055176})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9534724950790405})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9682483673095703})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8928, 'crossentropy': 0.783885546875}
store['active_learning_steps'][41]['acquisition']={'indices': [13354, 28537, 11373, 40202, 48271], 'labels': [8, 2, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7982895374298096})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.824929416179657})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8929057121276855})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8209528923034668})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.847, 'crossentropy': 0.81014189453125}
store['active_learning_steps'][42]['acquisition']={'indices': [30439, 8590, 54140, 49657, 1413], 'labels': [-1, 6, -1, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7626001834869385})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7136236429214478})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9538829326629639})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9357012510299683})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.882152795791626})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8943, 'crossentropy': 0.652214453125}
store['active_learning_steps'][43]['acquisition']={'indices': [45500, 18931, 25630, 23168, 29190], 'labels': [2, 8, 3, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8399777412414551})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8397876024246216})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9342231750488281})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9863439202308655})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9437605738639832})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8849, 'crossentropy': 0.7589119140625}
store['active_learning_steps'][44]['acquisition']={'indices': [54624, 18426, 19466, 6108, 15989], 'labels': [8, 3, -1, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7672324776649475})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8441812992095947})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8334829807281494})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9343670606613159})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8616, 'crossentropy': 0.71680703125}
store['active_learning_steps'][45]['acquisition']={'indices': [31936, 12221, 47669, 11043, 48447], 'labels': [3, 1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7616468667984009})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7364599704742432})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8250459432601929})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8496006727218628})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9468718767166138})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9, 'crossentropy': 0.701903076171875}
store['active_learning_steps'][46]['acquisition']={'indices': [50896, 18971, 52855, 3187, 18237], 'labels': [9, -1, -1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8254437446594238})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.761978030204773})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7881977558135986})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8367422819137573})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8214113712310791})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8897, 'crossentropy': 0.70122646484375}
store['active_learning_steps'][47]['acquisition']={'indices': [37064, 2288, 54146, 27675, 14345], 'labels': [7, -1, 9, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9267282485961914})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7953087091445923})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7507053017616272})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8626745939254761})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8799437880516052})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8702547550201416})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.7034541015625}
store['active_learning_steps'][48]['acquisition']={'indices': [6891, 29936, 17115, 1376, 44823], 'labels': [8, 3, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8264516592025757})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8649418354034424})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.819779634475708})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8927592039108276})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0206948518753052})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8866900205612183})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.719492236328125}
store['active_learning_steps'][49]['acquisition']={'indices': [58726, 27404, 47857, 21231, 29943], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8540823459625244})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8232036828994751})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8019347190856934})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.852109432220459})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0134543180465698})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9461976289749146})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8932, 'crossentropy': 0.72296513671875}
store['active_learning_steps'][50]['acquisition']={'indices': [61, 33327, 21319, 42003, 23377], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7624406814575195})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7595288753509521})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8645727634429932})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9387335777282715})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9479712247848511})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8844, 'crossentropy': 0.68178896484375}
store['active_learning_steps'][51]['acquisition']={'indices': [7577, 35147, 47865, 24393, 10353], 'labels': [-1, 5, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7801594734191895})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6730663776397705})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7331795692443848})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7009325623512268})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9784703254699707})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.6492501953125}
store['active_learning_steps'][52]['acquisition']={'indices': [7147, 8581, 17216, 54100, 54993], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7269279360771179})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7355673909187317})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7985095977783203})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7990554571151733})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8619, 'crossentropy': 0.68112158203125}
store['active_learning_steps'][53]['acquisition']={'indices': [16407, 39252, 48087, 49192, 758], 'labels': [-1, 7, 4, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8321020603179932})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8529360890388489})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.800122857093811})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9255561828613281})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8750454187393188})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8110987544059753})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9023, 'crossentropy': 0.70943681640625}
store['active_learning_steps'][54]['acquisition']={'indices': [50972, 7104, 8546, 29938, 43099], 'labels': [-1, 6, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7984695434570312})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7394134998321533})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7789440155029297})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8010741472244263})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9356666803359985})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.664436865234375}
store['active_learning_steps'][55]['acquisition']={'indices': [32668, 33711, 31410, 16671, 45434], 'labels': [-1, 4, -1, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8590863943099976})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8013343811035156})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8988684415817261})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8474066853523254})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8261492252349854})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8896, 'crossentropy': 0.700619580078125}
store['active_learning_steps'][56]['acquisition']={'indices': [22591, 35851, 25655, 54498, 31409], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7633544206619263})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7660160660743713})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7388213872909546})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8604632616043091})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8406374454498291})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9495093822479248})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8948, 'crossentropy': 0.69472177734375}
store['active_learning_steps'][57]['acquisition']={'indices': [29010, 50691, 25689, 48970, 38346], 'labels': [9, 2, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7735726237297058})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7864626049995422})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7084600329399109})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7347792387008667})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7768957614898682})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8499218225479126})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9065, 'crossentropy': 0.660476611328125}
store['active_learning_steps'][58]['acquisition']={'indices': [9962, 39263, 10354, 52, 50915], 'labels': [-1, 0, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7853695154190063})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6750339269638062})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7401816248893738})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7588770985603333})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7863917350769043})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.89, 'crossentropy': 0.661778662109375}
store['active_learning_steps'][59]['acquisition']={'indices': [22284, 15880, 15687, 10699, 21439], 'labels': [-1, 5, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7127032279968262})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6980392932891846})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7090750932693481})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7683454751968384})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8519206047058105})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.628519140625}
store['active_learning_steps'][60]['acquisition']={'indices': [43361, 14614, 31411, 56770, 47717], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7526317834854126})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6440630555152893})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7106398344039917})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7834413647651672})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8116534948348999})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9018, 'crossentropy': 0.622327099609375}
store['active_learning_steps'][61]['acquisition']={'indices': [36625, 46152, 48949, 54596, 11345], 'labels': [-1, 5, -1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7787054777145386})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7808917760848999})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.731702983379364})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7889593839645386})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8125959634780884})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8287702202796936})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9015, 'crossentropy': 0.704374560546875}
store['active_learning_steps'][62]['acquisition']={'indices': [49773, 36471, 21014, 39237, 26817], 'labels': [2, 3, -1, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.839166522026062})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7270947098731995})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7898210287094116})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6911165118217468})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8417171239852905})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8459757566452026})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8581305742263794})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.65444033203125}
store['active_learning_steps'][63]['acquisition']={'indices': [45318, 50789, 16716, 39530, 5288], 'labels': [4, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7118339538574219})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6863292455673218})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7512704133987427})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7081987261772156})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7184408903121948})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9007, 'crossentropy': 0.603032421875}
store['active_learning_steps'][64]['acquisition']={'indices': [27535, 14778, 8746, 52455, 2931], 'labels': [2, 6, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.727131724357605})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6179041862487793})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6591577529907227})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7048540711402893})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7235065698623657})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.584675634765625}
store['active_learning_steps'][65]['acquisition']={'indices': [4410, 34896, 23315, 12271, 13487], 'labels': [-1, 6, 0, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7820531129837036})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7205065488815308})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7242065668106079})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7807751893997192})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8273743391036987})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.622774365234375}
store['active_learning_steps'][66]['acquisition']={'indices': [31662, 55508, 10241, 48012, 21376], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7788946628570557})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6942189335823059})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.678558349609375})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7571576833724976})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.752301037311554})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7921966314315796})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9064, 'crossentropy': 0.622539013671875}
store['active_learning_steps'][67]['acquisition']={'indices': [46985, 7990, 48855, 48491, 45928], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7795078158378601})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6836417317390442})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6219614148139954})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7150150537490845})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7941370010375977})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.79652339220047})
store['active_learning_steps'][68]['training']['best_epoch']=3
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.601433056640625}
store['active_learning_steps'][68]['acquisition']={'indices': [31532, 54978, 6551, 47179, 25146], 'labels': [-1, 2, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8070018291473389})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6846208572387695})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7257344126701355})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7423964738845825})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7645483016967773})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8995, 'crossentropy': 0.602231689453125}
store['active_learning_steps'][69]['acquisition']={'indices': [13785, 11217, 55905, 50407, 40592], 'labels': [1, 0, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7489319443702698})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7069347500801086})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6416710615158081})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8205199837684631})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7957969903945923})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7906283140182495})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.584929052734375}
store['active_learning_steps'][70]['acquisition']={'indices': [30325, 54885, 8120, 2482, 11148], 'labels': [8, 6, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7415292263031006})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7079086303710938})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6926237344741821})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8263672590255737})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7132457494735718})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7789143323898315})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.592212841796875}
store['active_learning_steps'][71]['acquisition']={'indices': [22385, 37506, 3548, 34782, 45589], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7657604813575745})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7287217378616333})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7807273864746094})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8580281138420105})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7390241622924805})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.611932568359375}
store['active_learning_steps'][72]['acquisition']={'indices': [12376, 37588, 7390, 50171, 47694], 'labels': [5, 2, 5, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7219291925430298})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5821570754051208})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.606165885925293})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6275360584259033})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7235609292984009})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.5351611328125}
store['active_learning_steps'][73]['acquisition']={'indices': [1473, 33990, 41552, 19534, 2556], 'labels': [4, -1, 3, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7630805969238281})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6134516000747681})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6499283313751221})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7794445157051086})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6406121253967285})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.553876123046875}
store['active_learning_steps'][74]['acquisition']={'indices': [14594, 2881, 58409, 49509, 14571], 'labels': [7, -1, -1, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7269030809402466})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6787015199661255})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6774932146072388})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6201596260070801})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7313218116760254})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7588822841644287})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7059732675552368})
store['active_learning_steps'][75]['training']['best_epoch']=4
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.551767626953125}
store['active_learning_steps'][75]['acquisition']={'indices': [54692, 33486, 39049, 38225, 21318], 'labels': [1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7828829884529114})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6657778024673462})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6416836977005005})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6484673023223877})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6401108503341675})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7361893653869629})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7358211278915405})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7399464249610901})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.5949751953125}
store['active_learning_steps'][76]['acquisition']={'indices': [23882, 17940, 11084, 59532, 21568], 'labels': [0, -1, 2, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7636289596557617})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6682322025299072})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7462607622146606})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6806964874267578})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8172444105148315})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.593391064453125}
store['active_learning_steps'][77]['acquisition']={'indices': [16783, 42430, 17611, 46208, 55991], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7043227553367615})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6574816107749939})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7122665643692017})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6894481182098389})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6701627969741821})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.5958650390625}
store['active_learning_steps'][78]['acquisition']={'indices': [8736, 43599, 12632, 34567, 33378], 'labels': [9, -1, 1, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7294497489929199})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6241271495819092})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6123754978179932})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6467899084091187})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6194521188735962})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6969165802001953})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.586965673828125}
store['active_learning_steps'][79]['acquisition']={'indices': [49338, 59465, 58355, 30604, 52793], 'labels': [-1, -1, 1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7555239796638489})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6165973544120789})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6450698375701904})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6707961559295654})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8363245725631714})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9043, 'crossentropy': 0.555676318359375}
store['active_learning_steps'][80]['acquisition']={'indices': [23121, 15562, 55430, 3848, 29295], 'labels': [4, 9, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.857133150100708})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6907131671905518})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6652534604072571})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6504297256469727})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7308043837547302})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7413365840911865})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8026020526885986})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.59296962890625}
store['active_learning_steps'][81]['acquisition']={'indices': [4258, 2586, 56721, 1497, 10263], 'labels': [-1, -1, -1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7345762252807617})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.734639048576355})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6945676207542419})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.667695164680481})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6486191749572754})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7568022012710571})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.826689600944519})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7030339241027832})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.6019087890625}
store['active_learning_steps'][82]['acquisition']={'indices': [48475, 5503, 34311, 21846, 26572], 'labels': [8, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6973520517349243})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.62062668800354})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6386853456497192})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6293342113494873})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7602207660675049})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.599460205078125}
store['active_learning_steps'][83]['acquisition']={'indices': [20140, 15513, 23371, 24482, 14355], 'labels': [5, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7651779055595398})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6370706558227539})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6353066563606262})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.641308069229126})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6759127378463745})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6805334091186523})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.56261845703125}
store['active_learning_steps'][84]['acquisition']={'indices': [34926, 30032, 26269, 46907, 32587], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.738702654838562})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6774044036865234})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6362824440002441})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6719675064086914})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7090466022491455})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7505252957344055})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.572811865234375}
store['active_learning_steps'][85]['acquisition']={'indices': [25585, 46504, 7884, 51684, 13469], 'labels': [-1, 8, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6434652805328369})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6133642196655273})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6103804707527161})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.583267092704773})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6147116422653198})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6877824664115906})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6523082852363586})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.555935009765625}
store['active_learning_steps'][86]['acquisition']={'indices': [57353, 958, 8777, 31594, 23899], 'labels': [-1, -1, 6, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7353644371032715})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6356572508811951})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6056560277938843})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6421947479248047})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6307567954063416})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7028430700302124})
store['active_learning_steps'][87]['training']['best_epoch']=3
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.913, 'crossentropy': 0.564914697265625}
store['active_learning_steps'][87]['acquisition']={'indices': [45889, 17786, 6252, 48658, 10667], 'labels': [-1, 2, 2, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.81809401512146})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5916606187820435})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6030715703964233})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7074227929115295})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6581809520721436})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.519149365234375}
store['active_learning_steps'][88]['acquisition']={'indices': [4262, 36563, 28882, 41259, 43681], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.70509272813797})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6154764890670776})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6160202026367188})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5731136798858643})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6429618000984192})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.670943021774292})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6252620220184326})
store['active_learning_steps'][89]['training']['best_epoch']=4
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.5501296875}
store['active_learning_steps'][89]['acquisition']={'indices': [15857, 32581, 39400, 50966, 20798], 'labels': [-1, -1, 5, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7326056957244873})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6143032312393188})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6075912714004517})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6159331202507019})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6438747644424438})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6723570823669434})
store['active_learning_steps'][90]['training']['best_epoch']=3
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.594250390625}
store['active_learning_steps'][90]['acquisition']={'indices': [9173, 59105, 27827, 12082, 15370], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6503218412399292})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5715051889419556})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5878114104270935})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.56569504737854})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5749245285987854})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.558013916015625})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.581619143486023})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6470282673835754})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6380844712257385})
store['active_learning_steps'][91]['training']['best_epoch']=6
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.55066494140625}
store['active_learning_steps'][91]['acquisition']={'indices': [20262, 37081, 57241, 11596, 29555], 'labels': [4, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7349605560302734})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6301561594009399})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5727131366729736})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6099380850791931})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6162052154541016})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6265389919281006})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.5616626953125}
store['active_learning_steps'][92]['acquisition']={'indices': [6311, 45888, 35439, 30236, 23561], 'labels': [1, 9, 6, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7345934510231018})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5778679251670837})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6818987131118774})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6699459552764893})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6430681347846985})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.913, 'crossentropy': 0.5511494140625}
store['active_learning_steps'][93]['acquisition']={'indices': [26302, 36697, 53506, 56117, 40422], 'labels': [9, 5, -1, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8175772428512573})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.593854546546936})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5639668703079224})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6183405518531799})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.644798994064331})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6389527320861816})
store['active_learning_steps'][94]['training']['best_epoch']=3
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.4930287109375}
store['active_learning_steps'][94]['acquisition']={'indices': [50177, 24767, 38964, 10111, 12026], 'labels': [-1, -1, 7, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6744135618209839})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5500534772872925})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6245356798171997})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6436833143234253})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6344680786132812})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.528236376953125}
store['active_learning_steps'][95]['acquisition']={'indices': [24727, 12972, 6016, 17890, 34558], 'labels': [7, 4, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6764618158340454})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6068345904350281})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5870416164398193})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5872637033462524})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5922144651412964})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5961948037147522})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.496316064453125}
store['active_learning_steps'][96]['acquisition']={'indices': [15589, 17908, 15018, 5174, 33081], 'labels': [-1, -1, 9, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7047340273857117})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6150226593017578})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5638355016708374})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5899101495742798})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5654268264770508})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6417369842529297})
store['active_learning_steps'][97]['training']['best_epoch']=3
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9168, 'crossentropy': 0.544780078125}
store['active_learning_steps'][97]['acquisition']={'indices': [58139, 44583, 15627, 1579, 57031], 'labels': [1, -1, 6, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7384166717529297})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6072137951850891})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6055712699890137})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6327050924301147})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6401483416557312})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6725044250488281})
store['active_learning_steps'][98]['training']['best_epoch']=3
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9182, 'crossentropy': 0.559549560546875}
store['active_learning_steps'][98]['acquisition']={'indices': [41460, 37446, 23877, 51135, 7261], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7189140319824219})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6515407562255859})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6096732020378113})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6642569303512573})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6795257329940796})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.697530210018158})
store['active_learning_steps'][99]['training']['best_epoch']=3
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.52746748046875}
store['active_learning_steps'][99]['acquisition']={'indices': [25800, 18077, 50958, 23327, 17033], 'labels': [1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6828280091285706})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5784628391265869})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6051611304283142})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6082524657249451})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6273570656776428})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9153, 'crossentropy': 0.513920361328125}
store['active_learning_steps'][100]['acquisition']={'indices': [41137, 54249, 48300, 47478, 43336], 'labels': [0, 3, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.755663275718689})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5869560837745667})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.600532054901123})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.588202714920044})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5878632068634033})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.56135361328125}
store['active_learning_steps'][101]['acquisition']={'indices': [32920, 22680, 11017, 16672, 16369], 'labels': [7, -1, 2, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7497552633285522})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5914314985275269})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5914127230644226})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5359861850738525})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5582292079925537})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6417255401611328})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6987817287445068})
store['active_learning_steps'][102]['training']['best_epoch']=4
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.487091064453125}
store['active_learning_steps'][102]['acquisition']={'indices': [52791, 1095, 32048, 11907, 49561], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.711379885673523})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5992644429206848})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.49613216519355774})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.585936427116394})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5507733821868896})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5342488884925842})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9209, 'crossentropy': 0.475371435546875}
store['active_learning_steps'][103]['acquisition']={'indices': [54594, 10886, 33919, 9074, 22406], 'labels': [8, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6479877233505249})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5607572197914124})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5769285559654236})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5161901116371155})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5812988877296448})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5402407050132751})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5552484393119812})
store['active_learning_steps'][104]['training']['best_epoch']=4
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.480928662109375}
store['active_learning_steps'][104]['acquisition']={'indices': [50537, 57037, 39121, 2115, 15104], 'labels': [-1, 1, -1, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6791247129440308})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5742270946502686})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.615725576877594})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6063065528869629})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6230341196060181})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.49770576171875}
store['active_learning_steps'][105]['acquisition']={'indices': [20489, 7706, 52036, 22309, 18475], 'labels': [6, -1, 0, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7168098092079163})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5995441675186157})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6118205785751343})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5758771896362305})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6637793779373169})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6040140390396118})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5879012942314148})
store['active_learning_steps'][106]['training']['best_epoch']=4
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.547512353515625}
store['active_learning_steps'][106]['acquisition']={'indices': [2861, 751, 32139, 115, 50982], 'labels': [5, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7156256437301636})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5418093204498291})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5344271659851074})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5876253843307495})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6107187271118164})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.638832151889801})
store['active_learning_steps'][107]['training']['best_epoch']=3
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.495454833984375}
store['active_learning_steps'][107]['acquisition']={'indices': [45114, 7753, 18153, 56360, 7797], 'labels': [-1, -1, 9, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6822383403778076})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5310438275337219})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5167461037635803})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5653284788131714})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5771572589874268})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5652364492416382})
store['active_learning_steps'][108]['training']['best_epoch']=3
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.49010537109375}
store['active_learning_steps'][108]['acquisition']={'indices': [19296, 55614, 24341, 23976, 37603], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8236599564552307})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6146793961524963})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6275687217712402})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6206809878349304})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6840510368347168})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.541912109375}
store['active_learning_steps'][109]['acquisition']={'indices': [18922, 54955, 19798, 12378, 56897], 'labels': [-1, 9, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7176463603973389})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5971826314926147})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.581369936466217})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.642498791217804})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5773618221282959})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5993592739105225})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5959082841873169})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.676790714263916})
store['active_learning_steps'][110]['training']['best_epoch']=5
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.538250537109375}
store['active_learning_steps'][110]['acquisition']={'indices': [39001, 21680, 37534, 31213, 27954], 'labels': [-1, 1, -1, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7233248353004456})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6016703844070435})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6398187875747681})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5868258476257324})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6181789636611938})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6274011731147766})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6144126653671265})
store['active_learning_steps'][111]['training']['best_epoch']=4
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.58614833984375}
store['active_learning_steps'][111]['acquisition']={'indices': [2144, 43771, 20304, 28861, 35202], 'labels': [0, -1, 7, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7139941453933716})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6092171669006348})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5735577344894409})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6232888102531433})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6509473323822021})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5783286094665527})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.51286826171875}
store['active_learning_steps'][112]['acquisition']={'indices': [22812, 2622, 18307, 57507, 26384], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7460737824440002})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.561562180519104})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5881919860839844})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6157417297363281})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5950541496276855})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.5009626953125}
store['active_learning_steps'][113]['acquisition']={'indices': [44349, 24427, 33357, 22420, 27338], 'labels': [-1, 2, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7255541086196899})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5404710173606873})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5783201456069946})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5421628952026367})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5657861232757568})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9047, 'crossentropy': 0.508877197265625}
store['active_learning_steps'][114]['acquisition']={'indices': [40623, 28846, 10057, 22599, 42774], 'labels': [5, -1, -1, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.721888542175293})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5477197170257568})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5932306051254272})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5406140685081482})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6021485328674316})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5781146287918091})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6520109176635742})
store['active_learning_steps'][115]['training']['best_epoch']=4
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.493922607421875}
store['active_learning_steps'][115]['acquisition']={'indices': [34730, 45748, 56573, 51317, 56727], 'labels': [-1, -1, 0, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6959230899810791})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6183575391769409})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5485899448394775})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5830080509185791})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5867078304290771})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5992012023925781})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.492684423828125}
store['active_learning_steps'][116]['acquisition']={'indices': [38481, 48110, 37528, 40280, 16969], 'labels': [-1, 8, 4, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6998240947723389})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.605411171913147})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.566186785697937})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5495631694793701})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.648571252822876})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6449551582336426})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6126115322113037})
store['active_learning_steps'][117]['training']['best_epoch']=4
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.472726171875}
store['active_learning_steps'][117]['acquisition']={'indices': [33242, 49779, 22770, 36878, 12798], 'labels': [-1, 6, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6885435581207275})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5542882680892944})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5558120608329773})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5564967393875122})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5646570920944214})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.502727734375}
store['active_learning_steps'][118]['acquisition']={'indices': [36566, 32449, 930, 17177, 7809], 'labels': [3, 1, -1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7293777465820312})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6002225875854492})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6097849011421204})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6987531185150146})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.679885983467102})
store['active_learning_steps'][119]['training']['best_epoch']=2
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.53291279296875}
store['active_learning_steps'][119]['acquisition']={'indices': [19462, 50369, 22630, 53614, 36714], 'labels': [-1, 3, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7164041996002197})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5910278558731079})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5389354825019836})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5860980749130249})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.522779643535614})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5191651582717896})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6011214256286621})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5844408273696899})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6970175504684448})
store['active_learning_steps'][120]['training']['best_epoch']=6
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9309, 'crossentropy': 0.5167001953125}
store['active_learning_steps'][120]['acquisition']={'indices': [34278, 41938, 38950, 49803, 50070], 'labels': [-1, -1, 9, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7065348625183105})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6004782319068909})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5389530658721924})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5741474628448486})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5445435047149658})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5837361812591553})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.498256640625}
store['active_learning_steps'][121]['acquisition']={'indices': [28584, 23110, 29311, 6216, 4684], 'labels': [-1, 6, -1, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6429060101509094})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5489085912704468})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4759030044078827})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5402942895889282})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5567132234573364})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5591129064559937})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.443808935546875}
store['active_learning_steps'][122]['acquisition']={'indices': [37736, 16652, 5121, 22246, 23214], 'labels': [4, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6721698045730591})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5494438409805298})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5435230731964111})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5784773826599121})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5557863712310791})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5733807682991028})
store['active_learning_steps'][123]['training']['best_epoch']=3
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.490265966796875}
store['active_learning_steps'][123]['acquisition']={'indices': [5180, 50293, 20097, 25933, 38996], 'labels': [4, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6496749520301819})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5390580892562866})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5773628950119019})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5346958637237549})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5900418758392334})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5912530422210693})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6035364866256714})
store['active_learning_steps'][124]['training']['best_epoch']=4
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.478167919921875}
store['active_learning_steps'][124]['acquisition']={'indices': [54836, 48747, 159, 57037, 58489], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6889351606369019})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5252408981323242})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5646291971206665})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.556036114692688})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5899977684020996})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.492493115234375}
store['active_learning_steps'][125]['acquisition']={'indices': [20692, 57728, 25936, 52602, 55086], 'labels': [9, 9, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6561964750289917})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4998539090156555})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.45954346656799316})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5190516114234924})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5467013716697693})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6071870923042297})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.446443994140625}
store['active_learning_steps'][126]['acquisition']={'indices': [24660, 23389, 35959, 31633, 40134], 'labels': [-1, 0, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6516355872154236})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5124659538269043})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5059276223182678})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49389904737472534})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5798376202583313})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5817456245422363})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.555765688419342})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.464473876953125}
store['active_learning_steps'][127]['acquisition']={'indices': [6569, 53122, 4780, 53344, 19836], 'labels': [5, 5, 4, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.716138482093811})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5805556178092957})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5164122581481934})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5345324277877808})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5384498834609985})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.546546220779419})
store['active_learning_steps'][128]['training']['best_epoch']=3
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.46435087890625}
store['active_learning_steps'][128]['acquisition']={'indices': [12332, 36125, 50212, 58535, 7060], 'labels': [4, 6, -1, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.658348023891449})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5285394191741943})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47596973180770874})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4701631963253021})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4609633684158325})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47969552874565125})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5120375156402588})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4752865135669708})
store['active_learning_steps'][129]['training']['best_epoch']=5
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.4453693359375}
store['active_learning_steps'][129]['acquisition']={'indices': [6298, 33439, 15425, 17140, 5244], 'labels': [3, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7238881587982178})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47688281536102295})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5314681529998779})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4851546287536621})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5345944166183472})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.441432373046875}
store['active_learning_steps'][130]['acquisition']={'indices': [7389, 25063, 904, 55722, 45704], 'labels': [6, -1, 7, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6666789054870605})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5237030982971191})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4969004690647125})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4379047155380249})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4976365566253662})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47816821932792664})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4628252387046814})
store['active_learning_steps'][131]['training']['best_epoch']=4
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.416625634765625}
store['active_learning_steps'][131]['acquisition']={'indices': [12456, 211, 32768, 35292, 59874], 'labels': [0, -1, 2, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6515549421310425})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5401612520217896})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4820074439048767})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4896968603134155})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46950653195381165})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4675629734992981})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5255688428878784})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4637763500213623})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4957253038883209})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5481340885162354})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5196399688720703})
store['active_learning_steps'][132]['training']['best_epoch']=8
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.429157958984375}
store['active_learning_steps'][132]['acquisition']={'indices': [46641, 6025, 43960, 33763, 44744], 'labels': [-1, 4, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6426148414611816})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.501482367515564})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4946315884590149})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4859001636505127})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49968722462654114})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45742589235305786})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5107869505882263})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5157003998756409})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6417420506477356})
store['active_learning_steps'][133]['training']['best_epoch']=6
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9423, 'crossentropy': 0.414240771484375}
store['active_learning_steps'][133]['acquisition']={'indices': [36407, 19560, 419, 54204, 4762], 'labels': [5, -1, 9, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6795101165771484})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5353356003761292})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4428674578666687})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4945180416107178})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5581689476966858})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49638187885284424})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.403388330078125}
store['active_learning_steps'][134]['acquisition']={'indices': [31650, 30392, 17765, 9123, 39025], 'labels': [-1, -1, 8, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.618873119354248})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5263758897781372})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4947283864021301})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4835197329521179})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5261244773864746})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5532529950141907})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5187467932701111})
store['active_learning_steps'][135]['training']['best_epoch']=4
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.46468330078125}
store['active_learning_steps'][135]['acquisition']={'indices': [49579, 47350, 51419, 44484, 52672], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6341853141784668})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5318788886070251})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45937779545783997})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4942225217819214})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5167607665061951})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5108097195625305})
store['active_learning_steps'][136]['training']['best_epoch']=3
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.409607666015625}
store['active_learning_steps'][136]['acquisition']={'indices': [34613, 45696, 36555, 6950, 43760], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6417535543441772})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4645302891731262})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4966217279434204})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4891592860221863})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5116094350814819})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.444313037109375}
store['active_learning_steps'][137]['acquisition']={'indices': [13551, 49673, 17382, 24450, 41050], 'labels': [5, 3, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.614993691444397})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46334218978881836})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48025572299957275})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4497445821762085})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5001474618911743})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4781368374824524})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4821298122406006})
store['active_learning_steps'][138]['training']['best_epoch']=4
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9396, 'crossentropy': 0.3911419677734375}
store['active_learning_steps'][138]['acquisition']={'indices': [18812, 23427, 52642, 30609, 28107], 'labels': [3, 7, 4, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6961253881454468})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5794457793235779})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46912986040115356})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4918224811553955})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4834715723991394})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4635678231716156})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5350179672241211})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5906208157539368})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5443312525749207})
store['active_learning_steps'][139]['training']['best_epoch']=6
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.44493408203125}
store['active_learning_steps'][139]['acquisition']={'indices': [40282, 57237, 42101, 16629, 32129], 'labels': [6, 8, 5, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6246615648269653})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5170992612838745})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4869554042816162})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4835922122001648})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47894060611724854})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45490017533302307})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4936125576496124})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43756163120269775})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46250247955322266})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49728772044181824})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.541298508644104})
store['active_learning_steps'][140]['training']['best_epoch']=8
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9381, 'crossentropy': 0.460352587890625}
store['active_learning_steps'][140]['acquisition']={'indices': [10055, 11198, 49548, 27399, 19052], 'labels': [9, 5, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6789222955703735})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5169481039047241})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5297141075134277})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5107521414756775})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48712921142578125})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5341811180114746})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5031857490539551})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4874269366264343})
store['active_learning_steps'][141]['training']['best_epoch']=5
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.43782548828125}
store['active_learning_steps'][141]['acquisition']={'indices': [49020, 22311, 21133, 24641, 8757], 'labels': [3, 4, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6629053354263306})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5051836371421814})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4762954115867615})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5309337377548218})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5139350295066833})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4361240267753601})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49379125237464905})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4940965175628662})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49051547050476074})
store['active_learning_steps'][142]['training']['best_epoch']=6
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9405, 'crossentropy': 0.41914228515625}
store['active_learning_steps'][142]['acquisition']={'indices': [32863, 18294, 20520, 7695, 38327], 'labels': [-1, 4, 2, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7341197729110718})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5289808511734009})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.49296197295188904})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4921903908252716})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44879859685897827})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4436996579170227})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.534270703792572})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5158169269561768})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5079801082611084})
store['active_learning_steps'][143]['training']['best_epoch']=6
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.4078796875}
store['active_learning_steps'][143]['acquisition']={'indices': [30051, 1834, 3446, 7654, 22576], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6956887245178223})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5291863679885864})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5069332122802734})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4840518832206726})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5068227648735046})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48766398429870605})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48146378993988037})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49420875310897827})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.529789924621582})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4870002269744873})
store['active_learning_steps'][144]['training']['best_epoch']=7
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.43969619140625}
store['active_learning_steps'][144]['acquisition']={'indices': [54111, 34652, 56616, 28485, 16624], 'labels': [5, -1, 3, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6449728012084961})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4986844062805176})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5056231021881104})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4697229862213135})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5102295875549316})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4427979588508606})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45837995409965515})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48055198788642883})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5535181760787964})
store['active_learning_steps'][145]['training']['best_epoch']=6
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9344, 'crossentropy': 0.50497294921875}
store['active_learning_steps'][145]['acquisition']={'indices': [16692, 11112, 17882, 1730, 44578], 'labels': [5, 1, 7, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6486091613769531})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49753886461257935})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4833945035934448})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4433213472366333})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4376220703125})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43948638439178467})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5068917274475098})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5119574069976807})
store['active_learning_steps'][146]['training']['best_epoch']=5
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9429, 'crossentropy': 0.40154375}
store['active_learning_steps'][146]['acquisition']={'indices': [3857, 25598, 38117, 4668, 34988], 'labels': [-1, 5, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6658896207809448})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4591867923736572})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4765068292617798})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3997684419155121})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4349387288093567})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45531386137008667})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4440348744392395})
store['active_learning_steps'][147]['training']['best_epoch']=4
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9458, 'crossentropy': 0.3618892578125}
store['active_learning_steps'][147]['acquisition']={'indices': [22734, 47130, 21570, 49137, 48494], 'labels': [5, 5, 3, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6806772947311401})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4971585273742676})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49030259251594543})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.435066282749176})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.442129522562027})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4995149075984955})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4692450761795044})
store['active_learning_steps'][148]['training']['best_epoch']=4
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.426181884765625}
store['active_learning_steps'][148]['acquisition']={'indices': [2555, 20603, 15984, 13903, 53819], 'labels': [8, 6, 5, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6746875047683716})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.48093557357788086})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4901078939437866})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48192235827445984})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46606987714767456})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47425514459609985})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4511345326900482})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5351257920265198})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48055267333984375})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5221453905105591})
store['active_learning_steps'][149]['training']['best_epoch']=7
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9463, 'crossentropy': 0.416281884765625}
store['active_learning_steps'][149]['acquisition']={'indices': [10758, 48169, 41802, 5495, 44432], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6627975106239319})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48877397179603577})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.46727412939071655})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43569672107696533})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.445989191532135})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4582110047340393})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.423123836517334})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.500150203704834})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.482888400554657})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49475768208503723})
store['active_learning_steps'][150]['training']['best_epoch']=7
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.438362841796875}
store['active_learning_steps'][150]['acquisition']={'indices': [9094, 38362, 17560, 25668, 28233], 'labels': [6, 5, 1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6572961211204529})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4869198799133301})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4004613161087036})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41933292150497437})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46066442131996155})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47754430770874023})
store['active_learning_steps'][151]['training']['best_epoch']=3
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.4047125732421875}
store['active_learning_steps'][151]['acquisition']={'indices': [15267, 8243, 21653, 21284, 47958], 'labels': [-1, 4, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6426653861999512})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47862231731414795})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.49139127135276794})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41868817806243896})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44203299283981323})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4373233914375305})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5241965055465698})
store['active_learning_steps'][152]['training']['best_epoch']=4
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.413622119140625}
store['active_learning_steps'][152]['acquisition']={'indices': [52582, 45241, 7195, 49657, 43294], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6686656475067139})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49449026584625244})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4346317648887634})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43058907985687256})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5088100433349609})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4908733069896698})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.451593816280365})
store['active_learning_steps'][153]['training']['best_epoch']=4
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.406624169921875}
store['active_learning_steps'][153]['acquisition']={'indices': [3285, 44137, 43953, 10959, 34956], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6379889845848083})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.48387718200683594})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.453050434589386})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4412015676498413})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4539620876312256})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46551513671875})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44700461626052856})
store['active_learning_steps'][154]['training']['best_epoch']=4
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.410242578125}
store['active_learning_steps'][154]['acquisition']={'indices': [16580, 33298, 33400, 58322, 41459], 'labels': [-1, -1, 3, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6745731234550476})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5243192911148071})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.46090537309646606})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.441518634557724})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48219579458236694})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4644186496734619})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5026276111602783})
store['active_learning_steps'][155]['training']['best_epoch']=4
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.4115896484375}
store['active_learning_steps'][155]['acquisition']={'indices': [11742, 18281, 29609, 43612, 11155], 'labels': [-1, 8, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6410137414932251})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4645949602127075})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4234141707420349})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4540303647518158})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4358992874622345})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4272599220275879})
store['active_learning_steps'][156]['training']['best_epoch']=3
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.395940478515625}
store['active_learning_steps'][156]['acquisition']={'indices': [830, 52096, 21312, 5502, 43422], 'labels': [2, -1, -1, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6592491865158081})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4903888702392578})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42686787247657776})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4967851936817169})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4524380564689636})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43371614813804626})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.406093115234375}
store['active_learning_steps'][157]['acquisition']={'indices': [51185, 52958, 50251, 43297, 1679], 'labels': [9, 4, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6884370446205139})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.49049824476242065})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4444083273410797})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.44150596857070923})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4433346688747406})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47521284222602844})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45329004526138306})
store['active_learning_steps'][158]['training']['best_epoch']=4
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9378, 'crossentropy': 0.4214955078125}
store['active_learning_steps'][158]['acquisition']={'indices': [33637, 53886, 1904, 31529, 27886], 'labels': [4, 7, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6041474342346191})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.49539387226104736})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4455806612968445})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4999937117099762})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49045976996421814})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48918232321739197})
store['active_learning_steps'][159]['training']['best_epoch']=3
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.430825341796875}
store['active_learning_steps'][159]['acquisition']={'indices': [11541, 59666, 33708, 44952, 45224], 'labels': [-1, 8, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6560811400413513})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4742659330368042})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4850636422634125})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46707409620285034})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.483585000038147})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4365381598472595})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4990634322166443})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5424490571022034})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5016927719116211})
store['active_learning_steps'][160]['training']['best_epoch']=6
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.429865625}
store['active_learning_steps'][160]['acquisition']={'indices': [8675, 43265, 49405, 13279, 53452], 'labels': [-1, 0, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6728274822235107})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5164324045181274})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4432673752307892})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.48810291290283203})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48790210485458374})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5182126760482788})
store['active_learning_steps'][161]['training']['best_epoch']=3
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.408370654296875}
store['active_learning_steps'][161]['acquisition']={'indices': [54943, 46137, 40385, 35908, 33032], 'labels': [-1, 9, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6264694929122925})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.47414469718933105})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45535415410995483})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4137476086616516})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.451257586479187})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45068103075027466})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46553289890289307})
store['active_learning_steps'][162]['training']['best_epoch']=4
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.4056862060546875}
store['active_learning_steps'][162]['acquisition']={'indices': [42906, 23462, 18924, 38848, 17775], 'labels': [3, -1, -1, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6427761316299438})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4619109034538269})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4595361351966858})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44834840297698975})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46847838163375854})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47583913803100586})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44588780403137207})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5252619981765747})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44974201917648315})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49784523248672485})
store['active_learning_steps'][163]['training']['best_epoch']=7
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.40907470703125}
store['active_learning_steps'][163]['acquisition']={'indices': [48115, 32536, 9001, 22569, 6265], 'labels': [8, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6694602370262146})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5085306167602539})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4811709523200989})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47415441274642944})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47995316982269287})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48495566844940186})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5092184543609619})
store['active_learning_steps'][164]['training']['best_epoch']=4
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.445813671875}
store['active_learning_steps'][164]['acquisition']={'indices': [6928, 55784, 29062, 10406, 19481], 'labels': [-1, 1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6874008178710938})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5787093639373779})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43441736698150635})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4576123356819153})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45791080594062805})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4843386113643646})
store['active_learning_steps'][165]['training']['best_epoch']=3
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.42337255859375}
store['active_learning_steps'][165]['acquisition']={'indices': [620, 21866, 5703, 35172, 2], 'labels': [-1, 3, -1, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6816909313201904})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5079857707023621})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.49680694937705994})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4908030033111572})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4885097146034241})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.451924204826355})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4944963753223419})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5576469898223877})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4896148443222046})
store['active_learning_steps'][166]['training']['best_epoch']=6
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.436943798828125}
store['active_learning_steps'][166]['acquisition']={'indices': [16025, 51534, 20700, 40611, 58776], 'labels': [2, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7604175806045532})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.47876113653182983})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42998242378234863})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4289078116416931})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4395020604133606})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45469406247138977})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4722030758857727})
store['active_learning_steps'][167]['training']['best_epoch']=4
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9394, 'crossentropy': 0.3990535400390625}
store['active_learning_steps'][167]['acquisition']={'indices': [10457, 11569, 15683, 37668, 15423], 'labels': [-1, -1, 4, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6919838190078735})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5150401592254639})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4715961813926697})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.417805016040802})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47613030672073364})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5323996543884277})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4393416941165924})
store['active_learning_steps'][168]['training']['best_epoch']=4
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.3737104736328125}
store['active_learning_steps'][168]['acquisition']={'indices': [28330, 11030, 42144, 6887, 29128], 'labels': [-1, -1, 9, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6581028699874878})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5327768921852112})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4472529888153076})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48752260208129883})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43422144651412964})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4584715962409973})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49157190322875977})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46514376997947693})
store['active_learning_steps'][169]['training']['best_epoch']=5
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9389, 'crossentropy': 0.4029003173828125}
store['active_learning_steps'][169]['acquisition']={'indices': [46591, 20970, 16097, 53631, 28160], 'labels': [2, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6136826276779175})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.49422216415405273})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.45016831159591675})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47120386362075806})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5069849491119385})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.477373868227005})
store['active_learning_steps'][170]['training']['best_epoch']=3
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9334, 'crossentropy': 0.425249609375}
store['active_learning_steps'][170]['acquisition']={'indices': [20307, 59113, 25105, 57475, 34390], 'labels': [9, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6506416201591492})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5067158937454224})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46430933475494385})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4706781208515167})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46246787905693054})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.455962598323822})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48660987615585327})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4798866808414459})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4993763267993927})
store['active_learning_steps'][171]['training']['best_epoch']=6
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.418749658203125}
store['active_learning_steps'][171]['acquisition']={'indices': [12596, 42625, 7906, 22806, 45860], 'labels': [-1, -1, 7, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.613956093788147})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4944952726364136})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.41463136672973633})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4068452715873718})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3812289834022522})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40837663412094116})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43245929479599})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45743876695632935})
store['active_learning_steps'][172]['training']['best_epoch']=5
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.3795234130859375}
