store = {}
store['timestamp']=1620298814
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=23']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=23
store['worker_id']=23
store['num_workers']=40
store['config']={'seed': 26, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.161097764968872})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.5259101390838623})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.5367178916931152})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.6449456214904785})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6884, 'crossentropy': 1.976848046875}
store['active_learning_steps'][0]['acquisition']={'indices': [31328, 13348, 23557, 35699, 46493], 'labels': [-1, -1, -1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3986353874206543})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.636603832244873})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.66648530960083})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.8049721717834473})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6752, 'crossentropy': 2.1666091796875}
store['active_learning_steps'][1]['acquisition']={'indices': [14882, 24659, 3412, 39741, 83], 'labels': [4, 9, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.8444459438323975})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.1952333450317383})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.305748224258423})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.610229015350342})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7169, 'crossentropy': 1.7874048828125}
store['active_learning_steps'][2]['acquisition']={'indices': [39893, 19566, 16688, 27241, 21416], 'labels': [6, 8, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8078241348266602})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.4571945667266846})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.69061279296875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.5744709968566895})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6748, 'crossentropy': 1.855187109375}
store['active_learning_steps'][3]['acquisition']={'indices': [24652, 21975, 9640, 57194, 29938], 'labels': [7, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.129763126373291})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.670109272003174})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.8824567794799805})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.931490898132324})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6753, 'crossentropy': 2.12414296875}
store['active_learning_steps'][4]['acquisition']={'indices': [49417, 48350, 22220, 46322, 5651], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9580838680267334})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.5805232524871826})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0546064376831055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7818121910095215})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6869, 'crossentropy': 1.878985546875}
store['active_learning_steps'][5]['acquisition']={'indices': [26490, 59459, 45139, 41869, 30889], 'labels': [-1, 5, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.013103485107422})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.473562240600586})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.802542209625244})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.6448283195495605})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6605, 'crossentropy': 2.114884765625}
store['active_learning_steps'][6]['acquisition']={'indices': [50698, 26694, 33511, 32908, 40054], 'labels': [9, -1, 5, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6834678649902344})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.9268357753753662})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.4133694171905518})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.7252721786499023})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7094, 'crossentropy': 1.57919638671875}
store['active_learning_steps'][7]['acquisition']={'indices': [34624, 6400, 22817, 47396, 35070], 'labels': [6, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8542017936706543})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.104933023452759})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.3347368240356445})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5594775676727295})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6974, 'crossentropy': 1.6687681640625}
store['active_learning_steps'][8]['acquisition']={'indices': [11913, 23770, 20974, 20442, 28330], 'labels': [-1, -1, -1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.7127108573913574})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3786392211914062})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.9243483543395996})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.773421287536621})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6917, 'crossentropy': 1.74593671875}
store['active_learning_steps'][9]['acquisition']={'indices': [1444, 1214, 43438, 6634, 43787], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6378463506698608})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.1280388832092285})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.225154399871826})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.222561836242676})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.695, 'crossentropy': 1.618924609375}
store['active_learning_steps'][10]['acquisition']={'indices': [5703, 52571, 40601, 53161, 1510], 'labels': [-1, -1, 4, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8019999265670776})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.9974697828292847})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.3106980323791504})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.3800477981567383})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6867, 'crossentropy': 1.845579296875}
store['active_learning_steps'][11]['acquisition']={'indices': [51397, 22095, 50976, 50077, 48598], 'labels': [1, 1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.655918836593628})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.214998483657837})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.2535629272460938})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.2823846340179443})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7303, 'crossentropy': 1.5759140625}
store['active_learning_steps'][12]['acquisition']={'indices': [34316, 23390, 10907, 57308, 22854], 'labels': [-1, 1, 1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.452863097190857})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9492383003234863})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.109818458557129})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.1882381439208984})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.745, 'crossentropy': 1.4714931640625}
store['active_learning_steps'][13]['acquisition']={'indices': [31393, 32033, 22429, 57317, 10702], 'labels': [-1, -1, 0, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.632448673248291})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.7405887842178345})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.852054238319397})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.2526798248291016})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7366, 'crossentropy': 1.58856240234375}
store['active_learning_steps'][14]['acquisition']={'indices': [16460, 841, 55157, 10291, 45530], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5478113889694214})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.8237740993499756})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9914494752883911})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.281428337097168})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7351, 'crossentropy': 1.460403125}
store['active_learning_steps'][15]['acquisition']={'indices': [21922, 5492, 13570, 9928, 58999], 'labels': [-1, 9, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6671371459960938})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.8771165609359741})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.905011773109436})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.2392730712890625})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7249, 'crossentropy': 1.56683056640625}
store['active_learning_steps'][16]['acquisition']={'indices': [16196, 2616, 23902, 27946, 52847], 'labels': [2, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6275255680084229})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.891023874282837})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.2679967880249023})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.317481517791748})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7111, 'crossentropy': 1.57357421875}
store['active_learning_steps'][17]['acquisition']={'indices': [36053, 29998, 4526, 26011, 24578], 'labels': [4, -1, 6, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.4146488904953003})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.6196774244308472})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.9115772247314453})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.1445536613464355})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7522, 'crossentropy': 1.37462451171875}
store['active_learning_steps'][18]['acquisition']={'indices': [13693, 30945, 30601, 11179, 21369], 'labels': [-1, 6, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4582338333129883})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.705413818359375})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8364297151565552})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.186556816101074})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7413, 'crossentropy': 1.3991009765625}
store['active_learning_steps'][19]['acquisition']={'indices': [23360, 45355, 55176, 42934, 40045], 'labels': [7, -1, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.502441644668579})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7372477054595947})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.8911080360412598})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.8579826354980469})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7451, 'crossentropy': 1.35803916015625}
store['active_learning_steps'][20]['acquisition']={'indices': [935, 20456, 13292, 24792, 45603], 'labels': [8, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3436224460601807})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.8206861019134521})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.805492877960205})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.040259599685669})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7429, 'crossentropy': 1.461646875}
store['active_learning_steps'][21]['acquisition']={'indices': [18390, 31218, 24063, 48279, 3258], 'labels': [-1, -1, 3, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.2859044075012207})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4559510946273804})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6568512916564941})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8199487924575806})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7871, 'crossentropy': 1.2487517578125}
store['active_learning_steps'][22]['acquisition']={'indices': [52756, 53841, 38705, 45751, 52302], 'labels': [4, -1, 7, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2801529169082642})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.512986660003662})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.6543723344802856})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.790423035621643})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7644, 'crossentropy': 1.32193857421875}
store['active_learning_steps'][23]['acquisition']={'indices': [49492, 57366, 8368, 6033, 2501], 'labels': [9, 2, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2403407096862793})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.564206600189209})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.601152777671814})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6166510581970215})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7688, 'crossentropy': 1.2694958984375}
store['active_learning_steps'][24]['acquisition']={'indices': [11577, 38456, 52952, 7971, 14599], 'labels': [-1, 9, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2720422744750977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3348169326782227})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5562913417816162})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.7631402015686035})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7769, 'crossentropy': 1.23478125}
store['active_learning_steps'][25]['acquisition']={'indices': [29984, 50428, 49464, 47305, 30674], 'labels': [-1, 6, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2633609771728516})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.5714054107666016})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.7904168367385864})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8719781637191772})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7516, 'crossentropy': 1.2941759765625}
store['active_learning_steps'][26]['acquisition']={'indices': [35654, 14492, 7170, 21584, 59620], 'labels': [1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.2760632038116455})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.4586217403411865})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.6455647945404053})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.7056339979171753})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7803, 'crossentropy': 1.20963466796875}
store['active_learning_steps'][27]['acquisition']={'indices': [11259, 56212, 39495, 32549, 16565], 'labels': [-1, -1, -1, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.2848631143569946})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.5852422714233398})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.505716323852539})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.707708477973938})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7757, 'crossentropy': 1.30908818359375}
store['active_learning_steps'][28]['acquisition']={'indices': [35582, 36920, 49787, 35191, 49244], 'labels': [3, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2095205783843994})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5338611602783203})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5349366664886475})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4342494010925293})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7715, 'crossentropy': 1.16923505859375}
store['active_learning_steps'][29]['acquisition']={'indices': [3695, 35220, 28358, 37776, 43364], 'labels': [5, -1, 0, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.3171606063842773})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3974225521087646})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.66276216506958})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.6998494863510132})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7514, 'crossentropy': 1.2758568359375}
store['active_learning_steps'][30]['acquisition']={'indices': [8655, 49148, 21897, 1112, 24019], 'labels': [-1, 2, 9, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1000850200653076})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.459336280822754})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4398547410964966})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.5414716005325317})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7965, 'crossentropy': 1.0966912109375}
store['active_learning_steps'][31]['acquisition']={'indices': [26945, 1215, 2151, 19521, 36063], 'labels': [7, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1329982280731201})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1883695125579834})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.481504201889038})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.5361154079437256})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8098, 'crossentropy': 1.10206708984375}
store['active_learning_steps'][32]['acquisition']={'indices': [52422, 40139, 42155, 19188, 28140], 'labels': [2, 6, 8, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.248957872390747})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.479612112045288})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.5358946323394775})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.7632791996002197})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7911, 'crossentropy': 1.17548466796875}
store['active_learning_steps'][33]['acquisition']={'indices': [10568, 20316, 28934, 26516, 26715], 'labels': [1, -1, -1, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.134169101715088})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.4459714889526367})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.345823049545288})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.5355594158172607})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7882, 'crossentropy': 1.14750869140625}
store['active_learning_steps'][34]['acquisition']={'indices': [34509, 37561, 11017, 14595, 46155], 'labels': [5, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0894932746887207})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2905848026275635})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3020126819610596})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3265008926391602})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7958, 'crossentropy': 1.0624599609375}
store['active_learning_steps'][35]['acquisition']={'indices': [59808, 1198, 58236, 36293, 2426], 'labels': [3, 4, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0126218795776367})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0447195768356323})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.26787269115448})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2150766849517822})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.816, 'crossentropy': 1.036556640625}
store['active_learning_steps'][36]['acquisition']={'indices': [58777, 30747, 50338, 53980, 46972], 'labels': [-1, 3, 1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0263917446136475})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2502418756484985})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2274338006973267})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2977190017700195})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7962, 'crossentropy': 1.03534873046875}
store['active_learning_steps'][37]['acquisition']={'indices': [5946, 37556, 51699, 18093, 25447], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0281574726104736})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1437536478042603})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1864672899246216})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2555643320083618})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8262, 'crossentropy': 1.03486875}
store['active_learning_steps'][38]['acquisition']={'indices': [28084, 57974, 54626, 34498, 34801], 'labels': [6, 3, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9814584851264954})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0091928243637085})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0945708751678467})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.184450387954712})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8304, 'crossentropy': 0.9346630859375}
store['active_learning_steps'][39]['acquisition']={'indices': [48957, 14150, 58098, 58712, 23403], 'labels': [4, -1, 2, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.060921311378479})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.085556983947754})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.205653429031372})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2274324893951416})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8189, 'crossentropy': 0.99373251953125}
store['active_learning_steps'][40]['acquisition']={'indices': [49987, 18464, 38630, 45120, 25856], 'labels': [0, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0592843294143677})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0598387718200684})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0443373918533325})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0749218463897705})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.2338016033172607})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.1784112453460693})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8542, 'crossentropy': 1.10836044921875}
store['active_learning_steps'][41]['acquisition']={'indices': [15150, 28396, 42814, 3614, 30984], 'labels': [0, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8972615003585815})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.964505136013031})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0083568096160889})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.059590220451355})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8282, 'crossentropy': 0.90773681640625}
store['active_learning_steps'][42]['acquisition']={'indices': [27049, 27983, 35587, 31555, 54485], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9424141645431519})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9740443825721741})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9400159120559692})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.037086009979248})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1185898780822754})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.2180092334747314})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8551, 'crossentropy': 1.012337109375}
store['active_learning_steps'][43]['acquisition']={'indices': [2654, 360, 36123, 5961, 50704], 'labels': [-1, -1, 2, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9745775461196899})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.156235933303833})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.204919695854187})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1936628818511963})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8252, 'crossentropy': 0.96000966796875}
store['active_learning_steps'][44]['acquisition']={'indices': [50930, 45872, 30429, 6499, 38725], 'labels': [-1, -1, 2, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8775959014892578})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.07498037815094})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.174243450164795})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.208033800125122})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8229, 'crossentropy': 0.910954296875}
store['active_learning_steps'][45]['acquisition']={'indices': [15096, 31973, 43616, 53237, 47759], 'labels': [-1, -1, 1, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8687022924423218})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9808166027069092})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0084657669067383})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0849878787994385})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8292, 'crossentropy': 0.8721833984375}
store['active_learning_steps'][46]['acquisition']={'indices': [15588, 3577, 23800, 43585, 32273], 'labels': [2, 6, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9800851345062256})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.921508252620697})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.016688585281372})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1750065088272095})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.204671025276184})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8502, 'crossentropy': 0.95777724609375}
store['active_learning_steps'][47]['acquisition']={'indices': [39971, 39961, 16948, 2625, 5297], 'labels': [-1, -1, -1, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9346768856048584})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0343043804168701})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0333491563796997})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0681577920913696})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8215, 'crossentropy': 0.940226171875}
store['active_learning_steps'][48]['acquisition']={'indices': [16961, 7723, 15798, 14327, 2910], 'labels': [0, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9972227215766907})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0556706190109253})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1222760677337646})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1259117126464844})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8285, 'crossentropy': 0.93251181640625}
store['active_learning_steps'][49]['acquisition']={'indices': [59199, 53772, 49382, 34898, 27250], 'labels': [1, 2, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0245060920715332})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9866348505020142})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0800158977508545})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0873804092407227})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.15189790725708})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8506, 'crossentropy': 0.97878408203125}
store['active_learning_steps'][50]['acquisition']={'indices': [13233, 23452, 6156, 17108, 41803], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8792696595191956})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.94881671667099})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.94475257396698})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0761473178863525})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8368, 'crossentropy': 0.8887943359375}
store['active_learning_steps'][51]['acquisition']={'indices': [43412, 13824, 41502, 16991, 59313], 'labels': [-1, 3, 9, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9860615730285645})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1327345371246338})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0208579301834106})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1373250484466553})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8038, 'crossentropy': 0.962940625}
store['active_learning_steps'][52]['acquisition']={'indices': [1979, 18109, 14941, 16680, 26901], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8928009271621704})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0229188203811646})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.033232569694519})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1389739513397217})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8236, 'crossentropy': 0.901959765625}
store['active_learning_steps'][53]['acquisition']={'indices': [31237, 34281, 55831, 34309, 58264], 'labels': [-1, 4, 3, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9769737720489502})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9590328335762024})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9369642734527588})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.2043821811676025})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9883221983909607})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.2168035507202148})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8608, 'crossentropy': 0.962887109375}
store['active_learning_steps'][54]['acquisition']={'indices': [12834, 1063, 58839, 55970, 21306], 'labels': [-1, 8, 6, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8807997703552246})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8761977553367615})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0709867477416992})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9169667363166809})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.071522831916809})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8658, 'crossentropy': 0.8397890625}
store['active_learning_steps'][55]['acquisition']={'indices': [34926, 53945, 20410, 21977, 16407], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9303615093231201})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9152957201004028})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9083095192909241})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9750400185585022})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0603560209274292})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0653793811798096})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8672, 'crossentropy': 0.95675224609375}
store['active_learning_steps'][56]['acquisition']={'indices': [55867, 1397, 13836, 36531, 1329], 'labels': [-1, -1, 3, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0686979293823242})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9153202176094055})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0719914436340332})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1551735401153564})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.145484209060669})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8505, 'crossentropy': 0.94328818359375}
store['active_learning_steps'][57]['acquisition']={'indices': [29570, 43007, 33690, 49933, 31226], 'labels': [-1, -1, 5, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9422217607498169})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8755353689193726})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1171388626098633})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9426741600036621})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.1140912771224976})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8628, 'crossentropy': 0.9114826171875}
store['active_learning_steps'][58]['acquisition']={'indices': [4486, 34477, 13064, 14524, 40504], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8061339855194092})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7984448671340942})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.091148853302002})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9604861736297607})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.978233814239502})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8705, 'crossentropy': 0.811288623046875}
store['active_learning_steps'][59]['acquisition']={'indices': [31800, 48464, 3557, 9307, 498], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9490907788276672})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9583345651626587})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9363061189651489})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0028595924377441})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9950467348098755})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.1222478151321411})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8728, 'crossentropy': 0.9342029296875}
store['active_learning_steps'][60]['acquisition']={'indices': [56327, 50488, 57855, 14117, 21630], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0090891122817993})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9493590593338013})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9420700073242188})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.037699818611145})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0146080255508423})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.1996123790740967})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8662, 'crossentropy': 0.8939931640625}
store['active_learning_steps'][61]['acquisition']={'indices': [55838, 10578, 36117, 29632, 48079], 'labels': [5, 5, 1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8712230920791626})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7942299842834473})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.921232283115387})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9378142356872559})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0919240713119507})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8632, 'crossentropy': 0.84655166015625}
store['active_learning_steps'][62]['acquisition']={'indices': [1349, 41238, 6382, 11780, 22272], 'labels': [0, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9084535837173462})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8397036194801331})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9228911399841309})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8201947212219238})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0249545574188232})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.062535285949707})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 1.0538454055786133})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8838, 'crossentropy': 0.88470068359375}
store['active_learning_steps'][63]['acquisition']={'indices': [38234, 12954, 44757, 28761, 41836], 'labels': [-1, -1, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.885441780090332})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9282830953598022})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9189386367797852})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9998444318771362})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8262, 'crossentropy': 0.8890443359375}
store['active_learning_steps'][64]['acquisition']={'indices': [55670, 30083, 37536, 6553, 41644], 'labels': [6, 6, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8931233882904053})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9179575443267822})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9380018711090088})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9122471213340759})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8418, 'crossentropy': 0.8644333984375}
store['active_learning_steps'][65]['acquisition']={'indices': [13770, 33526, 28409, 50873, 31506], 'labels': [-1, 2, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8119888305664062})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7673342227935791})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8015561103820801})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8463171720504761})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9966632127761841})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8816, 'crossentropy': 0.77958759765625}
store['active_learning_steps'][66]['acquisition']={'indices': [35711, 54329, 26357, 47659, 28625], 'labels': [7, 1, 2, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8939336538314819})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8574978113174438})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8935047388076782})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9878817796707153})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 1.0067138671875})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8589, 'crossentropy': 0.85770244140625}
store['active_learning_steps'][67]['acquisition']={'indices': [16745, 20363, 1401, 51323, 42461], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7890662550926208})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8636116981506348})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8207634687423706})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.852057933807373})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.847, 'crossentropy': 0.790332861328125}
store['active_learning_steps'][68]['acquisition']={'indices': [12035, 19804, 58472, 46235, 47820], 'labels': [3, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8756569623947144})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8500091433525085})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8045091032981873})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8841404318809509})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8893272876739502})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9927096366882324})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8786, 'crossentropy': 0.8475611328125}
store['active_learning_steps'][69]['acquisition']={'indices': [49045, 54750, 51216, 57515, 30496], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9024361371994019})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8229596614837646})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8428606986999512})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0382864475250244})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.003623127937317})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8561, 'crossentropy': 0.85264453125}
store['active_learning_steps'][70]['acquisition']={'indices': [49249, 24648, 40031, 39847, 31747], 'labels': [3, 4, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7847719192504883})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7441538572311401})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8038127422332764})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8103375434875488})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.895114541053772})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8783, 'crossentropy': 0.757672119140625}
store['active_learning_steps'][71]['acquisition']={'indices': [40924, 43980, 1846, 23813, 10340], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8605538606643677})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9008588790893555})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.828411340713501})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8701833486557007})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9688542485237122})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9313244819641113})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8837, 'crossentropy': 0.8355029296875}
store['active_learning_steps'][72]['acquisition']={'indices': [37428, 59467, 43300, 44731, 4084], 'labels': [8, -1, 1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8302304148674011})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7486763000488281})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8080642819404602})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9518455862998962})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9199835062026978})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8829, 'crossentropy': 0.763567626953125}
store['active_learning_steps'][73]['acquisition']={'indices': [20297, 8780, 4466, 37786, 52632], 'labels': [-1, 8, 9, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7909365892410278})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7706054449081421})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7409955263137817})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7701703906059265})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8103092908859253})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8786970376968384})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8919, 'crossentropy': 0.69421796875}
store['active_learning_steps'][74]['acquisition']={'indices': [12670, 52452, 11339, 56808, 35630], 'labels': [-1, 5, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8489968180656433})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8975411057472229})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7592296600341797})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8192588090896606})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8970751762390137})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7772505283355713})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8856, 'crossentropy': 0.817924365234375}
store['active_learning_steps'][75]['acquisition']={'indices': [22274, 35480, 2066, 49563, 37039], 'labels': [-1, 9, 0, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7859078645706177})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6829001903533936})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6465003490447998})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7733951807022095})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.839728832244873})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8485916256904602})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.66369970703125}
store['active_learning_steps'][76]['acquisition']={'indices': [47585, 56277, 13675, 56580, 24084], 'labels': [-1, 5, 3, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.849219560623169})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7830823659896851})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7592695951461792})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8292772769927979})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8279315233230591})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.917951226234436})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.74921416015625}
store['active_learning_steps'][77]['acquisition']={'indices': [26397, 44293, 307, 5863, 56875], 'labels': [8, -1, -1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7236367464065552})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7157114744186401})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7404124736785889})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.886358380317688})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8274681568145752})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8876, 'crossentropy': 0.706963671875}
store['active_learning_steps'][78]['acquisition']={'indices': [18682, 44096, 40369, 25513, 38302], 'labels': [7, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7685908675193787})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6747512817382812})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8512935042381287})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8104636073112488})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8082945942878723})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.678879345703125}
store['active_learning_steps'][79]['acquisition']={'indices': [27002, 34085, 4480, 41645, 14365], 'labels': [5, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8472930192947388})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.744094729423523})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.817792534828186})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8490725755691528})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9699332118034363})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 0.7034484375}
store['active_learning_steps'][80]['acquisition']={'indices': [38038, 44786, 44595, 1490, 31253], 'labels': [5, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7561633586883545})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7300372123718262})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8232539892196655})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7756842374801636})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8224124908447266})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8888, 'crossentropy': 0.736267578125}
store['active_learning_steps'][81]['acquisition']={'indices': [1748, 34532, 675, 19428, 47332], 'labels': [9, 2, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7424280643463135})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7281651496887207})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7905717492103577})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8106637001037598})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8239715099334717})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.75557421875}
store['active_learning_steps'][82]['acquisition']={'indices': [41355, 57303, 19121, 50669, 22901], 'labels': [-1, 1, 4, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8304316997528076})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7478749752044678})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7271637916564941})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7650703191757202})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8182401061058044})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8770291805267334})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9007, 'crossentropy': 0.7374025390625}
store['active_learning_steps'][83]['acquisition']={'indices': [23095, 34716, 18167, 33265, 14363], 'labels': [0, 3, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7627984285354614})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6910466551780701})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7011884450912476})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.707382082939148})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7475177049636841})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.8955, 'crossentropy': 0.671516943359375}
store['active_learning_steps'][84]['acquisition']={'indices': [56011, 47875, 4489, 22006, 47675], 'labels': [-1, 1, 2, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8071787357330322})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7626838684082031})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8511476516723633})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8075624704360962})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.945041298866272})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8758, 'crossentropy': 0.772343896484375}
store['active_learning_steps'][85]['acquisition']={'indices': [30552, 39434, 33288, 13050, 40917], 'labels': [4, 2, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7527430057525635})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6919166445732117})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7056566476821899})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7911105155944824})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8136241436004639})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8881, 'crossentropy': 0.695763427734375}
store['active_learning_steps'][86]['acquisition']={'indices': [54630, 50853, 33768, 47529, 3529], 'labels': [6, 5, -1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8736323714256287})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8042476177215576})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7336721420288086})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7494306564331055})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7914342880249023})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7988426089286804})
store['active_learning_steps'][87]['training']['best_epoch']=3
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.717691064453125}
store['active_learning_steps'][87]['acquisition']={'indices': [55075, 22114, 31866, 22216, 22476], 'labels': [5, -1, 9, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8216869831085205})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7106201648712158})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7763491868972778})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8026339411735535})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7979685664176941})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.7229568359375}
store['active_learning_steps'][88]['acquisition']={'indices': [8415, 5865, 46212, 52890, 19713], 'labels': [4, 9, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7726715803146362})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7282782793045044})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7671171426773071})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7420065402984619})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9378097057342529})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.8827, 'crossentropy': 0.716574560546875}
store['active_learning_steps'][89]['acquisition']={'indices': [1422, 24054, 33826, 24728, 56678], 'labels': [-1, 9, 1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8353942632675171})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7871685028076172})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7398306727409363})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.768601655960083})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8153706789016724})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8976308107376099})
store['active_learning_steps'][90]['training']['best_epoch']=3
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.8894, 'crossentropy': 0.7703544921875}
store['active_learning_steps'][90]['acquisition']={'indices': [47745, 12826, 47179, 31884, 37548], 'labels': [-1, 3, 6, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7908996343612671})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7026845216751099})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8126365542411804})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.742233157157898})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7731503844261169})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.71357236328125}
store['active_learning_steps'][91]['acquisition']={'indices': [43725, 23280, 42478, 9327, 33446], 'labels': [7, 1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7972280383110046})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8014247417449951})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7424828410148621})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8535407781600952})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.833777904510498})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8440594673156738})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.8964, 'crossentropy': 0.70534140625}
store['active_learning_steps'][92]['acquisition']={'indices': [5497, 21941, 58221, 29665, 44520], 'labels': [-1, 6, -1, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.849158525466919})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7184985876083374})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7642108201980591})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8360903263092041})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8988613486289978})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8849, 'crossentropy': 0.682622412109375}
store['active_learning_steps'][93]['acquisition']={'indices': [40713, 33158, 52615, 45770, 27506], 'labels': [5, 2, 1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7982608079910278})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7256688475608826})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7321872711181641})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7825619578361511})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.807007372379303})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.8944, 'crossentropy': 0.679601416015625}
store['active_learning_steps'][94]['acquisition']={'indices': [52546, 54081, 33908, 40305, 15480], 'labels': [9, 9, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8555031418800354})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8212395906448364})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7947816252708435})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7317328453063965})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7101619243621826})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7581179738044739})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.784433126449585})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8337609767913818})
store['active_learning_steps'][95]['training']['best_epoch']=5
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.700937255859375}
store['active_learning_steps'][95]['acquisition']={'indices': [4287, 23537, 12762, 52601, 2627], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7284813523292542})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7023096084594727})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7373155355453491})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7516409158706665})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6744945645332336})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7476741075515747})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.788349986076355})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8078732490539551})
store['active_learning_steps'][96]['training']['best_epoch']=5
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.68815556640625}
store['active_learning_steps'][96]['acquisition']={'indices': [1931, 30029, 22990, 43713, 59647], 'labels': [6, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7687841653823853})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.732283353805542})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6512043476104736})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6695573925971985})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7424472570419312})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7339321374893188})
store['active_learning_steps'][97]['training']['best_epoch']=3
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.60930556640625}
store['active_learning_steps'][97]['acquisition']={'indices': [26137, 26533, 7266, 41056, 8963], 'labels': [4, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7126910090446472})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6837753057479858})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6027438640594482})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7638294100761414})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6657782196998596})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7418802976608276})
store['active_learning_steps'][98]['training']['best_epoch']=3
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.592798046875}
store['active_learning_steps'][98]['acquisition']={'indices': [30400, 1659, 30239, 39022, 42102], 'labels': [3, -1, 8, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7313375473022461})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6722381711006165})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.692093551158905})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.680404782295227})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7303657531738281})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.634314013671875}
store['active_learning_steps'][99]['acquisition']={'indices': [33535, 44095, 20920, 15824, 55960], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6819491386413574})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6687164306640625})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7021768689155579})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6514549255371094})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8206461071968079})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7683769464492798})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7359341382980347})
store['active_learning_steps'][100]['training']['best_epoch']=4
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9093, 'crossentropy': 0.63958251953125}
store['active_learning_steps'][100]['acquisition']={'indices': [25166, 4455, 40253, 55207, 52893], 'labels': [0, -1, 5, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6813831329345703})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6800888776779175})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6551827192306519})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7415826320648193})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7746536731719971})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.730211079120636})
store['active_learning_steps'][101]['training']['best_epoch']=3
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9072, 'crossentropy': 0.641246044921875}
store['active_learning_steps'][101]['acquisition']={'indices': [30195, 23460, 13419, 52098, 25549], 'labels': [4, 2, 4, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7064713835716248})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6717374324798584})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6748613119125366})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6892744302749634})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7773978114128113})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.64001005859375}
store['active_learning_steps'][102]['acquisition']={'indices': [8447, 41862, 5127, 53190, 7608], 'labels': [3, 1, 3, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6878750324249268})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.650342583656311})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6641830205917358})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7238043546676636})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.646489143371582})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7282973527908325})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6846787929534912})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8039301633834839})
store['active_learning_steps'][103]['training']['best_epoch']=5
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.678342626953125}
store['active_learning_steps'][103]['acquisition']={'indices': [20923, 28166, 4672, 42571, 29129], 'labels': [8, -1, -1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7706023454666138})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6255596876144409})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6448196172714233})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6582345962524414})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6688864231109619})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.8988, 'crossentropy': 0.609694189453125}
store['active_learning_steps'][104]['acquisition']={'indices': [56836, 25603, 47979, 34715, 37255], 'labels': [-1, 5, 3, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7219662070274353})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6618316173553467})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6534201502799988})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7578099370002747})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.686055600643158})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.766942024230957})
store['active_learning_steps'][105]['training']['best_epoch']=3
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.68623056640625}
store['active_learning_steps'][105]['acquisition']={'indices': [6983, 3441, 53701, 9366, 45103], 'labels': [-1, -1, 8, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7136397957801819})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7037246227264404})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.63310706615448})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7128872275352478})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7229716777801514})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.69097900390625})
store['active_learning_steps'][106]['training']['best_epoch']=3
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9096, 'crossentropy': 0.63609287109375}
store['active_learning_steps'][106]['acquisition']={'indices': [47009, 8431, 25177, 51141, 4692], 'labels': [9, 8, 5, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6777279376983643})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5855628848075867})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6558739542961121})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6948709487915039})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6425458192825317})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9043, 'crossentropy': 0.593152880859375}
store['active_learning_steps'][107]['acquisition']={'indices': [45516, 51015, 14932, 15425, 9058], 'labels': [1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7311115264892578})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6892292499542236})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6934605836868286})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6944297552108765})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6624186038970947})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6724058389663696})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6512017250061035})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7304724454879761})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.698778510093689})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6541259288787842})
store['active_learning_steps'][108]['training']['best_epoch']=7
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.6869494140625}
store['active_learning_steps'][108]['acquisition']={'indices': [791, 30492, 58749, 35386, 21619], 'labels': [-1, -1, -1, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.717383861541748})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6810660362243652})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6289849281311035})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6381327509880066})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6778424978256226})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7093167304992676})
store['active_learning_steps'][109]['training']['best_epoch']=3
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.6083150390625}
store['active_learning_steps'][109]['acquisition']={'indices': [58872, 6577, 14894, 20497, 55974], 'labels': [-1, 9, -1, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7479193210601807})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.63685142993927})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6642558574676514})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5938076972961426})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6337745189666748})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6743849515914917})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6618025898933411})
store['active_learning_steps'][110]['training']['best_epoch']=4
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.63073037109375}
store['active_learning_steps'][110]['acquisition']={'indices': [31455, 31835, 7874, 6938, 8706], 'labels': [5, -1, 0, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7363671064376831})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5663026571273804})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.573444128036499})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6719359159469604})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7433134317398071})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.59204658203125}
store['active_learning_steps'][111]['acquisition']={'indices': [34553, 48217, 51952, 43302, 31296], 'labels': [0, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7017695903778076})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6374803781509399})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6263788938522339})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.607654869556427})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7075897455215454})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6055428981781006})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7182766199111938})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6814538240432739})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.699982762336731})
store['active_learning_steps'][112]['training']['best_epoch']=6
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.636787841796875}
store['active_learning_steps'][112]['acquisition']={'indices': [7053, 7242, 29971, 6554, 43627], 'labels': [9, -1, 6, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7114353775978088})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5957491993904114})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6600868105888367})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6559797525405884})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6506959199905396})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.606309912109375}
store['active_learning_steps'][113]['acquisition']={'indices': [47315, 210, 8008, 13294, 14596], 'labels': [-1, 0, 8, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7138739228248596})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6055808663368225})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6147350668907166})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6403628587722778})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5998919010162354})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6292852759361267})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6724507808685303})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6424109935760498})
store['active_learning_steps'][114]['training']['best_epoch']=5
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.594501123046875}
store['active_learning_steps'][114]['acquisition']={'indices': [18916, 32615, 53285, 23979, 8863], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6666384935379028})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5765083432197571})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5919122695922852})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6473327875137329})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6423420906066895})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.57939326171875}
store['active_learning_steps'][115]['acquisition']={'indices': [32477, 21739, 837, 2062, 39223], 'labels': [6, 5, -1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7629427909851074})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5799612402915955})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6213030815124512})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6264144778251648})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6971138715744019})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.8958, 'crossentropy': 0.597700439453125}
store['active_learning_steps'][116]['acquisition']={'indices': [34439, 9015, 2201, 258, 25522], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6932886838912964})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5850241780281067})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5698215365409851})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6509567499160767})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6843329071998596})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7661011815071106})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9071, 'crossentropy': 0.623950732421875}
store['active_learning_steps'][117]['acquisition']={'indices': [18068, 24975, 52276, 32176, 23936], 'labels': [6, 7, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7149652242660522})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5908616185188293})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.62918621301651})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5860717296600342})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.629510760307312})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6591330766677856})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6097139120101929})
store['active_learning_steps'][118]['training']['best_epoch']=4
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.5859494140625}
store['active_learning_steps'][118]['acquisition']={'indices': [58183, 18318, 1852, 24588, 43239], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7415581345558167})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6258890628814697})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6201995611190796})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5919808745384216})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6574795246124268})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5530542731285095})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6297193765640259})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6147308945655823})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6234443187713623})
store['active_learning_steps'][119]['training']['best_epoch']=6
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.569619873046875}
store['active_learning_steps'][119]['acquisition']={'indices': [41603, 42291, 49762, 37759, 24530], 'labels': [9, 8, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.836033821105957})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6228535175323486})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6900360584259033})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6798187494277954})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.678170919418335})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.8928, 'crossentropy': 0.63014443359375}
store['active_learning_steps'][120]['acquisition']={'indices': [37619, 19295, 20605, 4105, 18521], 'labels': [-1, 9, 7, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7270833253860474})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6170778274536133})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5909817218780518})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6154454946517944})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5614861249923706})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6581103801727295})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6223762631416321})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.624139666557312})
store['active_learning_steps'][121]['training']['best_epoch']=5
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.622753564453125}
store['active_learning_steps'][121]['acquisition']={'indices': [48897, 37412, 33727, 4664, 11649], 'labels': [-1, 2, 2, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6706811785697937})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5362372994422913})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5457327365875244})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6208756566047668})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5867105722427368})
store['active_learning_steps'][122]['training']['best_epoch']=2
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.526477685546875}
store['active_learning_steps'][122]['acquisition']={'indices': [52495, 9370, 35832, 18847, 48297], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7901581525802612})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6367537975311279})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6714964509010315})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.66265869140625})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6784287691116333})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.58136142578125}
store['active_learning_steps'][123]['acquisition']={'indices': [39804, 47016, 13611, 20121, 10952], 'labels': [3, 5, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7179502844810486})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5660288333892822})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6137598156929016})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6252990961074829})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6157407164573669})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.577518994140625}
store['active_learning_steps'][124]['acquisition']={'indices': [1169, 3691, 5780, 51001, 49077], 'labels': [-1, 0, 6, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7408159971237183})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5924102067947388})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5856493711471558})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6222392916679382})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5860706567764282})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6360552310943604})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.602431201171875}
store['active_learning_steps'][125]['acquisition']={'indices': [28485, 50571, 47731, 36636, 2791], 'labels': [3, 8, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6556273102760315})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5926872491836548})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5740759968757629})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6572902202606201})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6408286690711975})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6098081469535828})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.5723400390625}
store['active_learning_steps'][126]['acquisition']={'indices': [6408, 25794, 16519, 37904, 55365], 'labels': [1, -1, 0, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8056663274765015})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6161783337593079})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5955451130867004})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6493314504623413})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5604494214057922})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6124498844146729})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7319251894950867})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6830710172653198})
store['active_learning_steps'][127]['training']['best_epoch']=5
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.598344970703125}
store['active_learning_steps'][127]['acquisition']={'indices': [39898, 43554, 53482, 14280, 23537], 'labels': [-1, -1, -1, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6967178583145142})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5664489269256592})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6690443754196167})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6608365178108215})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6451456546783447})
store['active_learning_steps'][128]['training']['best_epoch']=2
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.562149267578125}
store['active_learning_steps'][128]['acquisition']={'indices': [37817, 5424, 51753, 55453, 578], 'labels': [5, 5, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7310381531715393})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5878232717514038})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5680941343307495})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6126773357391357})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6435084342956543})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6604130268096924})
store['active_learning_steps'][129]['training']['best_epoch']=3
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.568262548828125}
store['active_learning_steps'][129]['acquisition']={'indices': [45598, 7880, 52134, 47193, 18227], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6875320672988892})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5928308963775635})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5937507748603821})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5605664253234863})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5815646052360535})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6170668601989746})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6428463459014893})
store['active_learning_steps'][130]['training']['best_epoch']=4
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.568507080078125}
store['active_learning_steps'][130]['acquisition']={'indices': [52049, 17501, 48122, 4322, 7979], 'labels': [-1, -1, -1, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7118637561798096})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5812884569168091})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5811257362365723})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6505074501037598})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5841583013534546})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6051642298698425})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.579465234375}
store['active_learning_steps'][131]['acquisition']={'indices': [1800, 52585, 3806, 16444, 54335], 'labels': [-1, 3, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6484426259994507})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5402127504348755})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5438066124916077})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6191074252128601})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6009145379066467})
store['active_learning_steps'][132]['training']['best_epoch']=2
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.545335595703125}
store['active_learning_steps'][132]['acquisition']={'indices': [46699, 28947, 29576, 17103, 25345], 'labels': [-1, -1, 8, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7213211059570312})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5747637748718262})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5812628865242004})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6329904198646545})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6357147097587585})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.560868310546875}
store['active_learning_steps'][133]['acquisition']={'indices': [28355, 15811, 54379, 33121, 25550], 'labels': [1, 7, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7294576168060303})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5677920579910278})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5654233694076538})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5697445869445801})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5608563423156738})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6006436347961426})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6759039759635925})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6182151436805725})
store['active_learning_steps'][134]['training']['best_epoch']=5
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.600579248046875}
store['active_learning_steps'][134]['acquisition']={'indices': [9570, 1031, 140, 38660, 36127], 'labels': [1, 1, 7, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.744645357131958})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5352665185928345})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5439717769622803})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5595576763153076})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6359318494796753})
store['active_learning_steps'][135]['training']['best_epoch']=2
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.546031982421875}
store['active_learning_steps'][135]['acquisition']={'indices': [55571, 37656, 51695, 19559, 5519], 'labels': [9, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6724874377250671})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5321660041809082})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5774616003036499})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5757350921630859})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5070717334747314})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5419759750366211})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5903613567352295})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6148918271064758})
store['active_learning_steps'][136]['training']['best_epoch']=5
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.57878681640625}
store['active_learning_steps'][136]['acquisition']={'indices': [6534, 22818, 10065, 41369, 4062], 'labels': [-1, 4, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7014992237091064})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5677101612091064})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6111435294151306})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5861373543739319})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5990971326828003})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.55804609375}
store['active_learning_steps'][137]['acquisition']={'indices': [51311, 16391, 42020, 30061, 31151], 'labels': [6, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7289897203445435})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5307217836380005})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5641707181930542})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5309449434280396})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.514934241771698})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.554423451423645})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6164299249649048})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5648106336593628})
store['active_learning_steps'][138]['training']['best_epoch']=5
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.516670361328125}
store['active_learning_steps'][138]['acquisition']={'indices': [4595, 19028, 57240, 55249, 34364], 'labels': [3, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.717041015625})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5692702531814575})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5242109894752502})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5402642488479614})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5299158096313477})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.545079231262207})
store['active_learning_steps'][139]['training']['best_epoch']=3
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.5249228515625}
store['active_learning_steps'][139]['acquisition']={'indices': [814, 22435, 2867, 4946, 5407], 'labels': [-1, -1, -1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6598267555236816})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6117678880691528})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4916556775569916})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5557608604431152})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5517044067382812})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5510846376419067})
store['active_learning_steps'][140]['training']['best_epoch']=3
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.5063509765625}
store['active_learning_steps'][140]['acquisition']={'indices': [6617, 20413, 54868, 32634, 43472], 'labels': [1, 3, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6707067489624023})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.550675630569458})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5389318466186523})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5097166895866394})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.553461492061615})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.520929217338562})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5373985171318054})
store['active_learning_steps'][141]['training']['best_epoch']=4
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.534127294921875}
store['active_learning_steps'][141]['acquisition']={'indices': [48912, 24231, 13532, 8984, 6046], 'labels': [-1, -1, 5, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7097148299217224})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5474052429199219})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5458725094795227})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5627695322036743})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5358781814575195})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5475589036941528})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6088215112686157})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5867261290550232})
store['active_learning_steps'][142]['training']['best_epoch']=5
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.521050390625}
store['active_learning_steps'][142]['acquisition']={'indices': [19060, 31166, 18633, 11313, 10459], 'labels': [0, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6600570678710938})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.525424063205719})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5666072964668274})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5210028290748596})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5273658037185669})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5704320669174194})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6216611862182617})
store['active_learning_steps'][143]['training']['best_epoch']=4
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.511460302734375}
store['active_learning_steps'][143]['acquisition']={'indices': [38381, 33518, 25143, 19111, 21307], 'labels': [2, 6, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6811516284942627})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5371674299240112})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5001859068870544})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49546489119529724})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5640782713890076})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5599287748336792})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.534971296787262})
store['active_learning_steps'][144]['training']['best_epoch']=4
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.498846875}
store['active_learning_steps'][144]['acquisition']={'indices': [58186, 4932, 58928, 31967, 46319], 'labels': [8, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7482516765594482})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5172787308692932})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5402706861495972})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5794253349304199})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48824524879455566})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5285680294036865})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49261438846588135})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5570974946022034})
store['active_learning_steps'][145]['training']['best_epoch']=5
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.517106640625}
store['active_learning_steps'][145]['acquisition']={'indices': [12840, 42591, 48529, 43921, 50491], 'labels': [-1, 6, 0, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7031213641166687})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.510572075843811})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5534024834632874})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5214481353759766})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5175309777259827})
store['active_learning_steps'][146]['training']['best_epoch']=2
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.511527978515625}
store['active_learning_steps'][146]['acquisition']={'indices': [4115, 17994, 29921, 30548, 47596], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6520727872848511})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5273409485816956})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5333355665206909})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5716720819473267})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5513589382171631})
store['active_learning_steps'][147]['training']['best_epoch']=2
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.51137099609375}
store['active_learning_steps'][147]['acquisition']={'indices': [35452, 1354, 44047, 41744, 44427], 'labels': [6, -1, 1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6909807920455933})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5550294518470764})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4875062108039856})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5027672052383423})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5388054847717285})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5103855133056641})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.488128955078125}
store['active_learning_steps'][148]['acquisition']={'indices': [47420, 14356, 40975, 20464, 26396], 'labels': [8, -1, -1, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6460317373275757})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48469841480255127})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4808591306209564})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47921764850616455})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.521628201007843})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48633551597595215})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4974261522293091})
store['active_learning_steps'][149]['training']['best_epoch']=4
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.479789453125}
store['active_learning_steps'][149]['acquisition']={'indices': [16838, 21404, 3139, 42533, 1230], 'labels': [-1, 6, -1, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6751179695129395})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5676324367523193})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5744010806083679})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5455887913703918})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5860494375228882})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5339959859848022})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5506746768951416})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6212804317474365})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6484095454216003})
store['active_learning_steps'][150]['training']['best_epoch']=6
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.532990869140625}
store['active_learning_steps'][150]['acquisition']={'indices': [44127, 45472, 52037, 39013, 58538], 'labels': [0, -1, 8, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.722129762172699})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5339061617851257})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5166620016098022})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5164662599563599})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5095929503440857})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5275737047195435})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5657503604888916})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.552138090133667})
store['active_learning_steps'][151]['training']['best_epoch']=5
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.51248076171875}
store['active_learning_steps'][151]['acquisition']={'indices': [23531, 8021, 52791, 31122, 48620], 'labels': [-1, 0, -1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6446230411529541})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49626243114471436})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5033690333366394})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4881649911403656})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5285787582397461})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5990813970565796})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5107104778289795})
store['active_learning_steps'][152]['training']['best_epoch']=4
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.482892822265625}
store['active_learning_steps'][152]['acquisition']={'indices': [57735, 15507, 27743, 18035, 22687], 'labels': [3, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6394269466400146})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5267078876495361})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4883462190628052})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5469512939453125})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.567965030670166})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5276703834533691})
store['active_learning_steps'][153]['training']['best_epoch']=3
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.495717626953125}
store['active_learning_steps'][153]['acquisition']={'indices': [40313, 36803, 59538, 38961, 4545], 'labels': [0, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6262792348861694})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5316623449325562})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5118206739425659})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5176734328269958})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5427013635635376})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5264477133750916})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.507633251953125}
store['active_learning_steps'][154]['acquisition']={'indices': [38718, 45245, 22906, 51024, 28575], 'labels': [1, 8, 3, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7362614870071411})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5264553427696228})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5449860095977783})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5007035732269287})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4798389673233032})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5376375913619995})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5715384483337402})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5204375386238098})
store['active_learning_steps'][155]['training']['best_epoch']=5
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.498885595703125}
store['active_learning_steps'][155]['acquisition']={'indices': [17270, 48224, 6751, 50196, 6288], 'labels': [8, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6495479345321655})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5297720432281494})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4618154466152191})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46594831347465515})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5003056526184082})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5269715785980225})
store['active_learning_steps'][156]['training']['best_epoch']=3
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.47943203125}
store['active_learning_steps'][156]['acquisition']={'indices': [17445, 8849, 10963, 32620, 40492], 'labels': [-1, 7, 8, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6748089790344238})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5263189077377319})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4755309224128723})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4916451573371887})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5034488439559937})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5108639001846313})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.473187060546875}
store['active_learning_steps'][157]['acquisition']={'indices': [54775, 38080, 959, 20972, 51204], 'labels': [-1, -1, 1, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6180703043937683})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46634989976882935})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4814876317977905})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48296844959259033})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5000795125961304})
store['active_learning_steps'][158]['training']['best_epoch']=2
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.465245263671875}
store['active_learning_steps'][158]['acquisition']={'indices': [58150, 47629, 10679, 16653, 6211], 'labels': [-1, 5, -1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6250805258750916})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5156487226486206})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5142959356307983})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4773997664451599})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5243391394615173})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5097165107727051})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5205433964729309})
store['active_learning_steps'][159]['training']['best_epoch']=4
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9309, 'crossentropy': 0.458457373046875}
store['active_learning_steps'][159]['acquisition']={'indices': [44074, 6904, 23044, 18242, 89], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6214631199836731})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4732634425163269})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46564745903015137})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4218747615814209})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44582730531692505})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45326194167137146})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45042505860328674})
store['active_learning_steps'][160]['training']['best_epoch']=4
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.4446205078125}
store['active_learning_steps'][160]['acquisition']={'indices': [14304, 58064, 25615, 29534, 43887], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6618760824203491})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.471863716840744})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43416792154312134})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47024744749069214})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4911457896232605})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4158567190170288})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4487215280532837})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48779818415641785})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5042697191238403})
store['active_learning_steps'][161]['training']['best_epoch']=6
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9394, 'crossentropy': 0.4337515625}
store['active_learning_steps'][161]['acquisition']={'indices': [3869, 57253, 7564, 20274, 10091], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7264775633811951})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5488965511322021})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5076065063476562})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5221132040023804})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5034207105636597})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5133578181266785})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45451343059539795})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4930245280265808})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5675536394119263})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5144275426864624})
store['active_learning_steps'][162]['training']['best_epoch']=7
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.4633921875}
store['active_learning_steps'][162]['acquisition']={'indices': [44924, 2206, 19515, 39618, 8694], 'labels': [5, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6538115739822388})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.47416287660598755})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4931880831718445})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45571011304855347})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4996069669723511})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49625712633132935})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4720783829689026})
store['active_learning_steps'][163]['training']['best_epoch']=4
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.450181396484375}
store['active_learning_steps'][163]['acquisition']={'indices': [23406, 1655, 48164, 13028, 2530], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6719579696655273})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5034509897232056})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4727497100830078})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4864169657230377})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45952045917510986})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4476454257965088})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5127766132354736})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5343859791755676})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5158871412277222})
store['active_learning_steps'][164]['training']['best_epoch']=6
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.434799072265625}
store['active_learning_steps'][164]['acquisition']={'indices': [54804, 48107, 6381, 44429, 19840], 'labels': [-1, 2, -1, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6759294271469116})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4919363558292389})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47481977939605713})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5187796950340271})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4615754187107086})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49388113617897034})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4629802107810974})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.498996376991272})
store['active_learning_steps'][165]['training']['best_epoch']=5
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.4520625}
store['active_learning_steps'][165]['acquisition']={'indices': [22871, 26323, 10765, 50240, 16364], 'labels': [-1, 0, 3, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6779947280883789})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5138481855392456})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4875667989253998})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5205066204071045})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5136458873748779})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49609726667404175})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9334, 'crossentropy': 0.44847587890625}
store['active_learning_steps'][166]['acquisition']={'indices': [25619, 33423, 52880, 47324, 41230], 'labels': [3, 7, 6, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6706599593162537})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.48522841930389404})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4754582941532135})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47193002700805664})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47073376178741455})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5011578798294067})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5025075674057007})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5253170132637024})
store['active_learning_steps'][167]['training']['best_epoch']=5
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9372, 'crossentropy': 0.451127099609375}
store['active_learning_steps'][167]['acquisition']={'indices': [4377, 42643, 46464, 56393, 4782], 'labels': [9, -1, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6318361163139343})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5155894756317139})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4790584444999695})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4637087881565094})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46720337867736816})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4592454433441162})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41559040546417236})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5165917277336121})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5324541330337524})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5502564907073975})
store['active_learning_steps'][168]['training']['best_epoch']=7
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.421266015625}
store['active_learning_steps'][168]['acquisition']={'indices': [33578, 8066, 50078, 49418, 16943], 'labels': [-1, 9, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.647966742515564})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4967312216758728})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5216619372367859})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4722760319709778})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.497913658618927})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5345561504364014})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5452917814254761})
store['active_learning_steps'][169]['training']['best_epoch']=4
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9351, 'crossentropy': 0.44426005859375}
store['active_learning_steps'][169]['acquisition']={'indices': [6295, 37833, 31760, 44932, 8042], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6671374440193176})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4731273055076599})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4561614990234375})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4695394039154053})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5022742748260498})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4587591886520386})
store['active_learning_steps'][170]['training']['best_epoch']=3
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.413434716796875}
store['active_learning_steps'][170]['acquisition']={'indices': [11994, 14822, 43058, 49989, 55060], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7019858360290527})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4991645812988281})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47424131631851196})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4870818853378296})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47442781925201416})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4693412780761719})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.501491904258728})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46382755041122437})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5228996276855469})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47177445888519287})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.49101293087005615})
store['active_learning_steps'][171]['training']['best_epoch']=8
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9422, 'crossentropy': 0.439923681640625}
store['active_learning_steps'][171]['acquisition']={'indices': [20017, 1605, 55079, 28434, 24540], 'labels': [5, -1, -1, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6426142454147339})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5229537487030029})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46797382831573486})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44041043519973755})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4624447822570801})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.531844437122345})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5008677840232849})
store['active_learning_steps'][172]['training']['best_epoch']=4
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.41898466796875}
