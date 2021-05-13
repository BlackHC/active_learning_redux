store = {}
store['timestamp']=1620260544
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=39']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=39
store['worker_id']=39
store['num_workers']=40
store['config']={'seed': 58, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.872453212738037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3684964179992676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.768110752105713})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 4.009184837341309})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6362, 'crossentropy': 2.4240072265625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 2366], ['id', 18769], ['id', 51287], ['ood', 52384], ['ood', 20613]], 'labels': [1, 5, 1, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.6332099437713623})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.8755406141281128})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8134371042251587})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.1970834732055664})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7316, 'crossentropy': 1.39411669921875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 44467], ['id', 41671], ['ood', 855], ['id', 41267], ['id', 48792]], 'labels': [8, 4, 2, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5738345384597778})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.9808757305145264})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1381478309631348})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.9946155548095703})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.725, 'crossentropy': 1.49960458984375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 829], ['ood', 36431], ['id', 17553], ['ood', 8591], ['ood', 20313]], 'labels': [6, 9, 3, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3326528072357178})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.688889980316162})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.8308762311935425})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.9868913888931274})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7383, 'crossentropy': 1.24051123046875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 42660], ['id', 13921], ['id', 25390], ['id', 41545], ['id', 7511]], 'labels': [6, 0, 0, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.2127262353897095})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5106520652770996})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.5805132389068604})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.6596695184707642})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7732, 'crossentropy': 1.08800322265625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 41144], ['id', 8319], ['ood', 12818], ['id', 52004], ['id', 13148]], 'labels': [5, 1, 4, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.171955943107605})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4159746170043945})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4414963722229004})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.7659556865692139})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7776, 'crossentropy': 1.025148046875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 48178], ['ood', 42806], ['ood', 1592], ['ood', 45782], ['id', 56041]], 'labels': [0, 4, 4, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3108683824539185})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.5177627801895142})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7650277614593506})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.820610523223877})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7425, 'crossentropy': 1.15180068359375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 12033], ['id', 6749], ['id', 28791], ['id', 58712], ['id', 56802]], 'labels': [4, 5, 7, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1972153186798096})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1457877159118652})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2733747959136963})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.4275684356689453})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.5028400421142578})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8006, 'crossentropy': 1.063640625}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 15473], ['id', 32705], ['ood', 51636], ['ood', 31856], ['id', 44809]], 'labels': [8, 1, 6, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.1767971515655518})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3206883668899536})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.50950026512146})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3037998676300049})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7651, 'crossentropy': 1.1084220703125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 12423], ['id', 2116], ['id', 14660], ['id', 11952], ['ood', 57462]], 'labels': [6, 9, 6, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.1082937717437744})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2591056823730469})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.4068143367767334})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3872352838516235})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7703, 'crossentropy': 1.0413544921875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 10090], ['ood', 25180], ['id', 14742], ['ood', 11362], ['id', 56460]], 'labels': [2, 8, 5, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1493713855743408})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.185434103012085})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.4044179916381836})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.3827786445617676})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7524, 'crossentropy': 1.0952873046875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 12431], ['id', 19995], ['id', 28496], ['id', 40204], ['id', 49976]], 'labels': [9, 9, 6, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1201353073120117})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2677350044250488})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2535594701766968})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3275038003921509})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7855, 'crossentropy': 0.999383984375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 9018], ['ood', 11944], ['ood', 25147], ['id', 32927], ['id', 37746]], 'labels': [0, 5, 6, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9847807884216309})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0031359195709229})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0913383960723877})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2641973495483398})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7961, 'crossentropy': 0.9244193359375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 12825], ['ood', 28110], ['id', 50410], ['id', 42259], ['id', 39932]], 'labels': [9, 5, 8, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8844451904296875})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.944198489189148})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9787586331367493})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1009423732757568})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8309, 'crossentropy': 0.815346923828125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 53778], ['ood', 29257], ['id', 25402], ['ood', 50456], ['id', 24382]], 'labels': [2, 1, 5, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8799343705177307})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9605084657669067})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9385993480682373})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1332485675811768})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8347, 'crossentropy': 0.7916755859375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 53958], ['ood', 10096], ['ood', 6712], ['id', 21419], ['id', 1240]], 'labels': [3, 3, 8, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8589496612548828})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9047185182571411})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.028388261795044})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0786024332046509})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8333, 'crossentropy': 0.809117236328125}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 8527], ['ood', 53090], ['id', 10971], ['ood', 25225], ['ood', 15837]], 'labels': [1, 7, 1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8811362385749817})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.926577091217041})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.028113603591919})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0093092918395996})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8354, 'crossentropy': 0.794145556640625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 57546], ['id', 15455], ['ood', 6010], ['id', 51030], ['id', 9985]], 'labels': [7, 8, 1, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9140182733535767})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8605949878692627})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0053892135620117})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0658109188079834})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0524630546569824})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8543, 'crossentropy': 0.751409130859375}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 226], ['id', 27196], ['ood', 12779], ['id', 47588], ['id', 32361]], 'labels': [6, 4, 4, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8354928493499756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9469987154006958})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0400910377502441})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0475647449493408})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8421, 'crossentropy': 0.782506298828125}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 36580], ['id', 35299], ['id', 18407], ['ood', 44122], ['id', 47798]], 'labels': [8, 1, 1, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8692442774772644})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9049032926559448})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.912676215171814})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0575652122497559})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8439, 'crossentropy': 0.775683984375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 14661], ['ood', 10143], ['id', 55865], ['id', 13823], ['ood', 4428]], 'labels': [4, 0, 5, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9022048711776733})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8369476795196533})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9470660090446472})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9246646165847778})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0760831832885742})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.74663125}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 4002], ['id', 15990], ['id', 47451], ['id', 35223], ['ood', 12731]], 'labels': [3, 3, 6, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.914427638053894})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7974376082420349})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9512585401535034})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9733802676200867})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9748270511627197})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8671, 'crossentropy': 0.71125341796875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 56465], ['id', 20409], ['id', 26561], ['ood', 35459], ['id', 14022]], 'labels': [2, 1, 3, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8205761909484863})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7274770736694336})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8334829807281494})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8802471160888672})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9153870344161987})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8652, 'crossentropy': 0.671236083984375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5732], ['ood', 2611], ['id', 45871], ['id', 39133], ['ood', 24827]], 'labels': [1, 6, 7, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9505025744438171})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8863605260848999})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8158323764801025})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0202245712280273})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.003422498703003})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0498847961425781})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8588, 'crossentropy': 0.804090185546875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 30717], ['id', 5226], ['id', 56801], ['id', 49492], ['ood', 3326]], 'labels': [3, 6, 0, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9135951995849609})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8014518022537231})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9617354869842529})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9371795654296875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9447304010391235})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8657, 'crossentropy': 0.711884326171875}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 8590], ['id', 15892], ['id', 17548], ['ood', 11952], ['id', 16080]], 'labels': [0, 5, 2, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9611494541168213})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.856270432472229})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8567965030670166})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9359197020530701})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9772632718086243})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8597, 'crossentropy': 0.742967822265625}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 19689], ['ood', 11356], ['id', 10884], ['ood', 18524], ['id', 34563]], 'labels': [4, 2, 5, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9095180034637451})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8694862127304077})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8557438850402832})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8763777017593384})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8689779043197632})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9262436628341675})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8691, 'crossentropy': 0.730143994140625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 50473], ['id', 50699], ['ood', 44048], ['id', 39695], ['ood', 39382]], 'labels': [9, 4, 5, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8178604245185852})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7843131422996521})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8521330952644348})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8967725038528442})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8471485376358032})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.867, 'crossentropy': 0.685834375}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 47085], ['id', 51166], ['id', 45596], ['id', 12831], ['ood', 23828]], 'labels': [4, 7, 0, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.823836088180542})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7511354684829712})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8482776284217834})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8668785095214844})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8938663005828857})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.886, 'crossentropy': 0.606613232421875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 14866], ['id', 2913], ['ood', 8612], ['id', 8882], ['ood', 13632]], 'labels': [3, 6, 6, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8354998826980591})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7880219221115112})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8059003949165344})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.84089195728302})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.889733612537384})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8756, 'crossentropy': 0.639033203125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 30718], ['id', 42541], ['ood', 31291], ['id', 34138], ['ood', 53115]], 'labels': [3, 6, 7, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8652904033660889})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7278277277946472})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8467204570770264})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9118373394012451})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8734785914421082})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8731, 'crossentropy': 0.66382646484375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 57520], ['id', 21376], ['ood', 21103], ['ood', 15519], ['id', 27613]], 'labels': [2, 1, 6, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8848879337310791})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7702308893203735})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7748994827270508})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8289461731910706})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8426432013511658})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 0.6734654296875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 29722], ['ood', 1467], ['ood', 7026], ['id', 14344], ['id', 8815]], 'labels': [8, 9, 2, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7775269746780396})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6609806418418884})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6992899775505066})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6916019320487976})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7055796384811401})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8889, 'crossentropy': 0.58932646484375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 23839], ['id', 15590], ['id', 42097], ['id', 50714], ['ood', 45204]], 'labels': [6, 0, 3, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8400179147720337})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6804705858230591})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7169550061225891})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7621272802352905})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7706018686294556})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8803, 'crossentropy': 0.61873486328125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 3285], ['ood', 48259], ['ood', 21656], ['id', 56982], ['id', 2221]], 'labels': [5, 6, 4, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7865517735481262})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7060377597808838})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7896637916564941})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.849799633026123})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8290424346923828})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8806, 'crossentropy': 0.624261181640625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 25737], ['id', 7904], ['ood', 49883], ['id', 6711], ['id', 40073]], 'labels': [4, 9, 8, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8353997468948364})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6464385390281677})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6308484077453613})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6709902882575989})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7095965147018433})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7828354239463806})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8962, 'crossentropy': 0.5588728515625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 23466], ['ood', 40408], ['id', 19474], ['ood', 32587], ['id', 27036]], 'labels': [8, 8, 3, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7812082767486572})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.666253924369812})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.793877363204956})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.719200849533081})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8025322556495667})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.891, 'crossentropy': 0.58228076171875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 58243], ['id', 1066], ['ood', 54870], ['ood', 833], ['ood', 39485]], 'labels': [9, 9, 3, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7674403786659241})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6569816470146179})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6313705444335938})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7012761831283569})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7005342245101929})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7348448038101196})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.892, 'crossentropy': 0.570240625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 8780], ['id', 15727], ['id', 16909], ['id', 22325], ['ood', 24570]], 'labels': [8, 6, 2, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7750823497772217})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6453813314437866})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6669403314590454})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6766301393508911})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7201586961746216})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8979, 'crossentropy': 0.58232255859375}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 32885], ['ood', 47170], ['ood', 43726], ['id', 53342], ['ood', 17452]], 'labels': [3, 7, 8, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8125964403152466})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6618608236312866})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6425963044166565})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6760252714157104})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7337808012962341})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7322964668273926})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.56593056640625}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 18189], ['ood', 36956], ['id', 38954], ['ood', 41013], ['id', 42919]], 'labels': [5, 0, 7, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7623341083526611})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6224267482757568})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.576420247554779})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6195793747901917})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7364178895950317})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6827230453491211})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.54936279296875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 28455], ['ood', 56954], ['ood', 2321], ['ood', 52460], ['id', 1735]], 'labels': [5, 4, 7, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8201907873153687})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6540461182594299})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7351332902908325})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7068176865577698})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7130162715911865})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8881, 'crossentropy': 0.589691162109375}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 11393], ['id', 39417], ['ood', 35103], ['id', 24984], ['ood', 50479]], 'labels': [8, 1, 4, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8616151809692383})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7068876028060913})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6863795518875122})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6522629261016846})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6868263483047485})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6800503730773926})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7192478179931641})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.548032666015625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 23836], ['ood', 6324], ['ood', 9466], ['id', 58601], ['id', 6992]], 'labels': [5, 5, 8, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8336337208747864})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6451472043991089})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.668298602104187})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6273527145385742})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6549516916275024})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7547181248664856})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6911429166793823})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9016, 'crossentropy': 0.556139013671875}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 15921], ['id', 7778], ['ood', 3356], ['ood', 45424], ['id', 43869]], 'labels': [1, 3, 6, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7816094756126404})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6853405237197876})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.636198878288269})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6547365188598633})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7906814813613892})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8174853920936584})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.572086083984375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 20311], ['ood', 52516], ['id', 9239], ['ood', 14366], ['ood', 6618]], 'labels': [2, 1, 6, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.8721976280212402})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6754546165466309})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.696471095085144})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.757859468460083})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7720630168914795})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8854, 'crossentropy': 0.6095828125}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 41761], ['ood', 9589], ['ood', 37514], ['ood', 39684], ['id', 15744]], 'labels': [9, 7, 4, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7220546007156372})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6456153392791748})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6944414377212524})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6689269542694092})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7301896810531616})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.892, 'crossentropy': 0.571306884765625}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 28948], ['id', 34553], ['id', 11768], ['id', 47842], ['ood', 26171]], 'labels': [4, 0, 7, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8520630598068237})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6142439842224121})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6370505094528198})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6613236665725708})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.632667064666748})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.54000869140625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 17718], ['id', 10795], ['ood', 23450], ['ood', 45257], ['ood', 48251]], 'labels': [7, 7, 3, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7529540061950684})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6543054580688477})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5848965048789978})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6568726301193237})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.685906171798706})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6661754846572876})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.53445205078125}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 39216], ['id', 53315], ['ood', 985], ['ood', 12723], ['id', 20363]], 'labels': [2, 8, 2, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8074034452438354})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.651386022567749})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6091193556785583})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6132063865661621})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6797505021095276})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.677254855632782})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.54147666015625}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 1120], ['ood', 27310], ['id', 51954], ['id', 21763], ['ood', 45683]], 'labels': [8, 9, 8, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7976011037826538})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6487987041473389})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.642265796661377})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7087085843086243})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.762768030166626})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7185297012329102})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.56726416015625}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 18507], ['id', 10868], ['ood', 15664], ['ood', 26321], ['id', 49456]], 'labels': [0, 1, 2, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8201558589935303})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6682771444320679})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6489847302436829})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6751692295074463})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6592395305633545})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7553619146347046})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.572006982421875}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 36667], ['ood', 5900], ['ood', 11519], ['id', 6192], ['ood', 49964]], 'labels': [0, 8, 4, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7794626951217651})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6330732107162476})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6526945233345032})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6591389775276184})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7343830466270447})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.565812744140625}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 28362], ['ood', 7347], ['id', 34439], ['id', 25985], ['ood', 14428]], 'labels': [9, 2, 9, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8146085739135742})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6700855493545532})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6660240292549133})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6608244776725769})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6681647896766663})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7651277184486389})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7662971615791321})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9006, 'crossentropy': 0.572218212890625}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 1309], ['id', 18600], ['id', 36973], ['ood', 9528], ['ood', 10863]], 'labels': [6, 5, 9, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7851027250289917})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6269677877426147})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6735696792602539})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6986782550811768})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.673319935798645})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8933, 'crossentropy': 0.576496630859375}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 57730], ['ood', 2245], ['ood', 43541], ['ood', 29902], ['id', 19633]], 'labels': [0, 1, 8, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7712736129760742})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5858644247055054})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5184468030929565})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5794431567192078})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6549361944198608})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7260907292366028})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.488192822265625}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 8555], ['ood', 19762], ['ood', 54743], ['id', 52084], ['ood', 29107]], 'labels': [9, 8, 2, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8149980306625366})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6681931018829346})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6948489546775818})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6563440561294556})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6677881479263306})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7161785364151001})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7368748188018799})
store['active_learning_steps'][56]['training']['best_epoch']=4
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8995, 'crossentropy': 0.550073388671875}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 50198], ['ood', 26577], ['id', 41265], ['id', 46515], ['id', 20241]], 'labels': [8, 4, 0, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8422632217407227})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6648780703544617})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6345828771591187})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6191821694374084})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6878575086593628})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7240384817123413})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6614534854888916})
store['active_learning_steps'][57]['training']['best_epoch']=4
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.535387109375}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 5239], ['ood', 46899], ['ood', 55850], ['id', 35540], ['ood', 32992]], 'labels': [1, 6, 2, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7641950845718384})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5999450087547302})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6331764459609985})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5912936925888062})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6432424783706665})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6731223464012146})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.66949063539505})
store['active_learning_steps'][58]['training']['best_epoch']=4
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.5347314453125}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 19122], ['id', 51529], ['ood', 17366], ['id', 25334], ['ood', 44430]], 'labels': [1, 1, 0, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8073610067367554})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6252221465110779})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5983629822731018})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.59861820936203})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6876433491706848})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6646260619163513})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.523585693359375}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 49141], ['id', 18439], ['ood', 24757], ['id', 50505], ['ood', 55743]], 'labels': [5, 8, 0, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7833412885665894})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7293806076049805})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6806821823120117})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7832074761390686})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8329043984413147})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.791401743888855})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.58107060546875}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 35562], ['ood', 54738], ['id', 56110], ['ood', 25795], ['id', 40554]], 'labels': [4, 4, 1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7596606612205505})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6277464628219604})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5873807072639465})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6440148949623108})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6592954397201538})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6754374504089355})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9006, 'crossentropy': 0.527303515625}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 11567], ['id', 39411], ['ood', 51992], ['ood', 52494], ['ood', 25543]], 'labels': [4, 2, 7, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8106229305267334})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5877541899681091})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6016737818717957})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5756018161773682})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6986422538757324})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6121759414672852})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5980229377746582})
store['active_learning_steps'][62]['training']['best_epoch']=4
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.502146826171875}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 8308], ['ood', 52430], ['ood', 9613], ['ood', 18145], ['id', 56912]], 'labels': [3, 7, 7, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7948465943336487})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6229608058929443})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6045011878013611})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5902198553085327})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5613725185394287})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.607074499130249})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6707532405853271})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7084827423095703})
store['active_learning_steps'][63]['training']['best_epoch']=5
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9118, 'crossentropy': 0.52505166015625}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 18423], ['id', 55661], ['id', 1794], ['id', 3614], ['id', 44752]], 'labels': [9, 5, 9, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8674015402793884})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6031980514526367})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5702530741691589})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5630131959915161})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6032201647758484})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6286077499389648})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6139256954193115})
store['active_learning_steps'][64]['training']['best_epoch']=4
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.510851171875}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 33133], ['id', 13122], ['ood', 50304], ['ood', 43882], ['ood', 17394]], 'labels': [2, 8, 3, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7370551824569702})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5543913245201111})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5638483762741089})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5414395928382874})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5630433559417725})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5459135174751282})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5897337198257446})
store['active_learning_steps'][65]['training']['best_epoch']=4
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.476052490234375}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 56949], ['ood', 4648], ['id', 48909], ['id', 897], ['ood', 5494]], 'labels': [0, 0, 7, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7592455148696899})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5892576575279236})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5421422719955444})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5846942663192749})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6063755750656128})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5886440277099609})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.483125927734375}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 12816], ['ood', 38176], ['id', 49805], ['ood', 30614], ['id', 10184]], 'labels': [0, 6, 2, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8393501043319702})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5972986221313477})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6096384525299072})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5668516159057617})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5607187747955322})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5850468873977661})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6368300914764404})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5868954658508301})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9278, 'crossentropy': 0.436616259765625}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 21107], ['ood', 42856], ['id', 35133], ['ood', 13], ['ood', 47675]], 'labels': [4, 8, 5, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7233467102050781})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6050757765769958})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5840140581130981})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5826120376586914})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6168594360351562})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5858331918716431})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6057767271995544})
store['active_learning_steps'][68]['training']['best_epoch']=4
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9152, 'crossentropy': 0.487139599609375}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 28990], ['ood', 28322], ['ood', 30287], ['id', 57039], ['id', 41513]], 'labels': [7, 3, 0, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7738251686096191})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5578770041465759})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5653913617134094})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5839319825172424})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5925516486167908})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.539875146484375}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 42570], ['id', 50293], ['id', 7520], ['ood', 48335], ['id', 43209]], 'labels': [9, 1, 2, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7761592864990234})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6063001751899719})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5482234954833984})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5209263563156128})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5008553266525269})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5184366106987})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.552517831325531})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5456708669662476})
store['active_learning_steps'][70]['training']['best_epoch']=5
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.45951103515625}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 34380], ['ood', 41443], ['id', 26344], ['ood', 44176], ['ood', 7331]], 'labels': [1, 5, 6, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.780328631401062})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.596320629119873})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5702623724937439})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6100592613220215})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6046112775802612})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5914400219917297})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.5048966796875}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 56126], ['id', 42984], ['id', 52845], ['id', 18009], ['id', 18341]], 'labels': [7, 5, 9, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7760445475578308})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6102884411811829})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5622605085372925})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6153265237808228})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5530263185501099})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6314367055892944})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6647771596908569})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6411089897155762})
store['active_learning_steps'][72]['training']['best_epoch']=5
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.47195693359375}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 27918], ['ood', 37657], ['id', 17331], ['id', 26807], ['id', 48788]], 'labels': [8, 9, 1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8312545418739319})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5512512922286987})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5340595841407776})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.48665744066238403})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5334322452545166})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6092479825019836})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5890904664993286})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.45792294921875}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 52261], ['ood', 27685], ['ood', 16986], ['ood', 14355], ['id', 30107]], 'labels': [7, 8, 4, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7348819971084595})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5499513149261475})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5051665306091309})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5369020700454712})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5602054595947266})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5751508474349976})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.44461474609375}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 9446], ['ood', 27668], ['ood', 17711], ['ood', 26864], ['ood', 46817]], 'labels': [9, 0, 1, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8116971850395203})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.611966609954834})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5275588035583496})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5900306701660156})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5617467761039734})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5468334555625916})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.4699080078125}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 10764], ['ood', 17619], ['id', 58392], ['id', 25731], ['ood', 18136]], 'labels': [8, 8, 6, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7635158896446228})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5771549940109253})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5565539598464966})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.580837607383728})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6082711219787598})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5943444967269897})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.454184033203125}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 29359], ['ood', 14733], ['ood', 46512], ['id', 25638], ['ood', 52691]], 'labels': [5, 8, 5, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7459782361984253})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5595710277557373})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.513650119304657})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5611408948898315})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5466741919517517})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5833433866500854})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.92, 'crossentropy': 0.461030029296875}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 40181], ['ood', 34344], ['id', 24116], ['id', 905], ['ood', 36032]], 'labels': [1, 5, 2, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7480922341346741})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5656803846359253})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5686079263687134})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5682812929153442})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5893664360046387})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.516967236328125}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 26838], ['ood', 23313], ['ood', 59626], ['ood', 7361], ['ood', 53762]], 'labels': [1, 8, 2, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8193554282188416})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5926035642623901})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5660321712493896})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6107321977615356})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6099127531051636})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5802206993103027})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.489209912109375}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 36792], ['ood', 59529], ['id', 4304], ['ood', 33241], ['id', 15231]], 'labels': [6, 6, 5, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7672510147094727})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.625758707523346})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.516848087310791})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4708483815193176})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5118048191070557})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5536974668502808})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4903774559497833})
store['active_learning_steps'][80]['training']['best_epoch']=4
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9309, 'crossentropy': 0.439488232421875}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 6560], ['ood', 41815], ['ood', 35446], ['id', 40417], ['id', 27326]], 'labels': [4, 1, 1, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8060296773910522})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6068047285079956})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5940496921539307})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5736852288246155})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5697728395462036})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6016399264335632})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6003981828689575})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5900027751922607})
store['active_learning_steps'][81]['training']['best_epoch']=5
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.469201318359375}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 16144], ['ood', 39143], ['ood', 1451], ['id', 12000], ['ood', 54251]], 'labels': [0, 1, 7, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7793940305709839})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5199098587036133})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5360665321350098})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.552334189414978})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5752623677253723})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.492840576171875}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 2327], ['ood', 7566], ['ood', 20348], ['ood', 43694], ['ood', 30265]], 'labels': [0, 7, 0, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.784744381904602})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5838679671287537})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5881152749061584})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.554866373538971})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5671334862709045})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5743401050567627})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5561847686767578})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9278, 'crossentropy': 0.436037744140625}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 49647], ['ood', 23000], ['ood', 29788], ['ood', 50262], ['ood', 33601]], 'labels': [4, 4, 6, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7680426836013794})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5622732639312744})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5287095308303833})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5289366841316223})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5681896209716797})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5823171138763428})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.441889306640625}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 28999], ['id', 8727], ['id', 52889], ['ood', 53469], ['ood', 28479]], 'labels': [4, 2, 2, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7669281959533691})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5898143649101257})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.540654182434082})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5696007013320923})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5530408620834351})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5649584531784058})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.456805810546875}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 17264], ['id', 47832], ['ood', 29131], ['ood', 384], ['ood', 20826]], 'labels': [7, 5, 4, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8287388682365417})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6245852708816528})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5526354908943176})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5418500900268555})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5473682284355164})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5820499062538147})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6012030243873596})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.443101318359375}
