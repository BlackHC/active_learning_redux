store = {}
store['timestamp']=1620257768
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=4']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=4
store['worker_id']=4
store['num_workers']=40
store['config']={'seed': 5, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.044506788253784})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.55367112159729})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5569536685943604})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7237491607666016})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6873, 'crossentropy': 2.010672265625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 41457], ['id', 53933], ['id', 17620], ['id', 12730], ['id', 18408]], 'labels': [5, 8, 0, 7, 7], 'scores': [0.6795614957809448, 0.7780990600585938, 0.7506852149963379, 0.7282359600067139, 0.8074465394020081]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.861968994140625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.4012107849121094})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3798720836639404})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.6889657974243164})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7308, 'crossentropy': 1.7968359375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 46794], ['ood', 7886], ['ood', 1195], ['id', 48375], ['id', 51414]], 'labels': [8, 8, 7, 8, 8], 'scores': [0.7410089373588562, 0.6156641244888306, 0.5899688005447388, 0.8393470048904419, 0.9172461032867432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.7625317573547363})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.0659728050231934})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.173866033554077})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.347947597503662})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6762, 'crossentropy': 1.64804375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 43931], ['id', 58005], ['id', 7481], ['id', 48177], ['id', 7726]], 'labels': [6, 5, 5, 1, 4], 'scores': [0.2630489766597748, 0.49644017219543457, 0.38297146558761597, 0.6342236399650574, 0.7119536995887756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5512762069702148})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9057362079620361})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9894863367080688})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2356340885162354})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7262, 'crossentropy': 1.4138341796875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 49850], ['id', 54278], ['id', 43534], ['id', 24095], ['id', 32668]], 'labels': [4, 7, 8, 3, 9], 'scores': [0.575833797454834, 0.6539750695228577, 0.4184451103210449, 0.6198076009750366, 0.7151262164115906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4512094259262085})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7799766063690186})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.9657641649246216})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.1417109966278076})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7446, 'crossentropy': 1.34485244140625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 36839], ['id', 49778], ['id', 21415], ['id', 32248], ['id', 34963]], 'labels': [5, 2, 3, 5, 6], 'scores': [0.7924979329109192, 0.6706993579864502, 0.7229715585708618, 0.665664792060852, 0.4980837106704712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.2531275749206543})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2951914072036743})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.43808913230896})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.5977962017059326})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7901, 'crossentropy': 1.127955078125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 23793], ['id', 9000], ['id', 33709], ['id', 47643], ['id', 20820]], 'labels': [0, 6, 3, 3, 9], 'scores': [0.5411694645881653, 0.6682018041610718, 0.6985701322555542, 0.8352283239364624, 0.6020740866661072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1784945726394653})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2115898132324219})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.449946403503418})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5086472034454346})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8015, 'crossentropy': 1.07322001953125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 47178], ['id', 44706], ['id', 13234], ['id', 11590], ['id', 53292]], 'labels': [9, 5, 5, 5, 5], 'scores': [0.5753040313720703, 0.6918123364448547, 0.6073486804962158, 0.8094902038574219, 0.5584352612495422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1942903995513916})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3207788467407227})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.4574817419052124})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.6386663913726807})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7918, 'crossentropy': 1.08931279296875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 36820], ['id', 42417], ['id', 19524], ['id', 18929], ['id', 55672]], 'labels': [8, 8, 2, 5, 5], 'scores': [0.5039278864860535, 0.7527467012405396, 0.6951377391815186, 0.7050014734268188, 0.7840089797973633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0819685459136963})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2646031379699707})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3331451416015625})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4756908416748047})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7967, 'crossentropy': 1.0015599609375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 43513], ['id', 29681], ['id', 30477], ['id', 8116], ['id', 11429]], 'labels': [2, 2, 2, 0, 0], 'scores': [0.7959268093109131, 0.6528844237327576, 0.6438453197479248, 0.719323456287384, 0.416301965713501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0084528923034668})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0452044010162354})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1834096908569336})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2562174797058105})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8315, 'crossentropy': 0.91147763671875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 41911], ['id', 46878], ['id', 13030], ['id', 8097], ['id', 33642]], 'labels': [2, 5, 0, 2, 9], 'scores': [0.7679648995399475, 0.5901919603347778, 0.7641003131866455, 0.6412080526351929, 0.7889006733894348]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.945090651512146})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.047187089920044})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9911607503890991})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1373863220214844})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8466, 'crossentropy': 0.82386552734375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 16746], ['id', 43381], ['id', 50093], ['id', 51106], ['id', 3890]], 'labels': [6, 7, 6, 3, 2], 'scores': [0.4814649224281311, 0.474947988986969, 0.29192519187927246, 0.4486337900161743, 0.6089208126068115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8886916041374207})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9423078894615173})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0105774402618408})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0281398296356201})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8271, 'crossentropy': 0.8325931640625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 48490], ['id', 23008], ['id', 32169], ['id', 5580], ['id', 23329]], 'labels': [7, 8, 2, 4, 9], 'scores': [0.593566358089447, 0.5335948467254639, 0.5818706750869751, 0.5787349939346313, 0.5204775333404541]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9671515226364136})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9324007630348206})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.971032440662384})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1003979444503784})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1574082374572754})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8442, 'crossentropy': 0.85155517578125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 59952], ['id', 22605], ['id', 4094], ['id', 4409], ['id', 55274]], 'labels': [0, 0, 3, 4, 6], 'scores': [0.6457120180130005, 0.7098641395568848, 0.7939995527267456, 0.7967382669448853, 0.6932492256164551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8391299247741699})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8015459775924683})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8430367112159729})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.917169451713562})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8519160747528076})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8647, 'crossentropy': 0.715076953125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 34872], ['id', 57547], ['id', 30649], ['id', 17710], ['id', 28412]], 'labels': [8, 7, 1, 3, 0], 'scores': [0.6093162894248962, 0.8486490845680237, 0.45039504766464233, 0.6177154779434204, 0.7690866589546204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.794575572013855})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7012686729431152})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7286961078643799})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8517566919326782})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7693933248519897})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.624313916015625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 29132], ['ood', 21613], ['id', 33576], ['id', 1925], ['id', 49202]], 'labels': [8, 1, 9, 9, 5], 'scores': [0.7640577554702759, 0.4728538990020752, 0.5237144231796265, 0.6092942953109741, 0.8549036383628845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9175348281860352})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7070060968399048})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7402245402336121})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8129907846450806})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7802971601486206})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8767, 'crossentropy': 0.665563916015625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 50091], ['id', 39768], ['id', 44350], ['id', 43176], ['id', 3408]], 'labels': [5, 3, 3, 2, 7], 'scores': [0.5272608995437622, 0.7121132016181946, 0.5818562507629395, 0.8850226402282715, 0.605585515499115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8516424298286438})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6486740112304688})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6345073580741882})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6926255226135254})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7616912126541138})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7915831804275513})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.901, 'crossentropy': 0.57239072265625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 19494], ['id', 22609], ['id', 31114], ['id', 42607], ['id', 51408]], 'labels': [9, 6, 4, 4, 6], 'scores': [0.5488174557685852, 0.7368072271347046, 0.6714150905609131, 0.79194176197052, 0.46654629707336426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8529398441314697})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7027778625488281})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.726420521736145})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7267104387283325})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7995144724845886})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.675256396484375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 54556], ['id', 39690], ['ood', 23951], ['id', 8924], ['ood', 42166]], 'labels': [2, 4, 5, 2, 9], 'scores': [0.8820688724517822, 0.5722500085830688, 0.733973503112793, 1.0096612572669983, 0.41454625129699707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7815849781036377})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6474146842956543})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6352983117103577})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6484626531600952})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6820472478866577})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.646233856678009})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.551009521484375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 39573], ['id', 12117], ['id', 28305], ['id', 31335], ['id', 51812]], 'labels': [5, 3, 0, 5, 9], 'scores': [0.8388521075248718, 0.8750786185264587, 0.5943683385848999, 0.8603187799453735, 0.7453826069831848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.815383791923523})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5922900438308716})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5551841855049133})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6215634942054749})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6314824223518372})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6421233415603638})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.499675537109375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 44554], ['id', 52172], ['id', 1812], ['id', 49893], ['id', 23428]], 'labels': [5, 5, 4, 3, 8], 'scores': [0.7381827235221863, 0.9141818284988403, 0.7305653095245361, 0.6554637551307678, 0.6771361827850342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9292545318603516})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.579559862613678})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5972569584846497})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.575329065322876})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6110219955444336})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6818391680717468})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6180105209350586})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.525269140625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 38920], ['id', 49786], ['id', 11719], ['id', 17079], ['id', 7182]], 'labels': [7, 1, 3, 6, 8], 'scores': [0.785428524017334, 0.6778317093849182, 0.6848593354225159, 0.8186454772949219, 0.9961327314376831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8552911281585693})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5574401617050171})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5111088752746582})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5132941007614136})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5562192797660828})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5923324823379517})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9219, 'crossentropy': 0.4862111328125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 51432], ['id', 8104], ['id', 5482], ['id', 3682], ['id', 29764]], 'labels': [1, 5, 4, 5, 4], 'scores': [0.8821598887443542, 0.7007349729537964, 0.5374944806098938, 0.6951473951339722, 0.5571728646755219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7284100651741028})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5622135400772095})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4872775077819824})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5564764738082886})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5313472151756287})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5542998313903809})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.432352587890625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 51324], ['id', 49824], ['id', 29320], ['id', 18714], ['id', 32757]], 'labels': [8, 8, 1, 8, 5], 'scores': [0.5780088901519775, 0.6666648983955383, 0.5777251124382019, 0.44902122020721436, 0.691111147403717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.831375002861023})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5649964213371277})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5253705978393555})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5125381350517273})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5459469556808472})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5835837721824646})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5884871482849121})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.473074169921875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 43110], ['id', 18772], ['id', 53653], ['id', 56412], ['id', 3447]], 'labels': [8, 6, 8, 8, 9], 'scores': [0.6896148324012756, 0.6201334595680237, 0.6127939224243164, 0.5458916425704956, 0.6645208597183228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9775768518447876})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.561400294303894})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5245846509933472})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48739224672317505})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47273504734039307})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5559465885162354})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5353118181228638})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5175772905349731})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.46475283203125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 48319], ['id', 11569], ['id', 1077], ['id', 50902], ['id', 27296]], 'labels': [6, 5, 3, 8, 5], 'scores': [0.39497876167297363, 0.91404789686203, 0.6038287878036499, 0.8999415636062622, 0.776330292224884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7774307727813721})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5588989853858948})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5003107786178589})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5113186836242676})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4951171875})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5258561968803406})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5763119459152222})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5769431591033936})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9285, 'crossentropy': 0.470241845703125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 39355], ['id', 31612], ['id', 31431], ['id', 12933], ['id', 35917]], 'labels': [8, 6, 3, 3, 6], 'scores': [0.6801056861877441, 0.8691897392272949, 0.6830272674560547, 0.6699929237365723, 0.41733962297439575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8188475370407104})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5089765787124634})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49108070135116577})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47295141220092773})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4842567443847656})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48121505975723267})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49617886543273926})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.428280126953125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 18720], ['id', 36760], ['id', 14355], ['id', 26658], ['id', 1758]], 'labels': [7, 7, 2, 2, 8], 'scores': [0.6070075631141663, 0.7770459055900574, 0.6003047227859497, 0.5321149826049805, 0.5589152574539185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9079080820083618})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5305157899856567})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5201936960220337})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4772908687591553})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48517173528671265})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5779702663421631})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5275534391403198})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.45319794921875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 12276], ['id', 36822], ['id', 9557], ['id', 8450], ['id', 54794]], 'labels': [0, 1, 8, 3, 2], 'scores': [0.49659138917922974, 0.7411612272262573, 0.8128898739814758, 0.4258803129196167, 0.6417431533336639]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8505367040634155})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5550665855407715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4769950807094574})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4786590039730072})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49223071336746216})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.494060218334198})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.431527587890625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 54880], ['id', 47383], ['id', 23924], ['ood', 20069], ['id', 19238]], 'labels': [5, 6, 6, 5, 3], 'scores': [0.569473147392273, 0.5934879779815674, 0.5971090495586395, 0.4913078546524048, 0.6149077415466309]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8820481896400452})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5357104539871216})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5009361505508423})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4460563063621521})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5337661504745483})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4865849018096924})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4458695650100708})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48224353790283203})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5494996309280396})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5256785750389099})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.442254443359375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 966], ['id', 51614], ['id', 1444], ['id', 3814], ['id', 42993]], 'labels': [3, 2, 2, 6, 9], 'scores': [0.925187885761261, 0.7476609349250793, 0.8184103965759277, 0.7479830384254456, 0.6115689873695374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0274873971939087})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5333389043807983})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43522143363952637})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4233503043651581})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40733200311660767})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42380261421203613})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4401508569717407})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.405154824256897})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4636288285255432})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45508211851119995})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4669550955295563})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.3942830078125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 40684], ['id', 7986], ['id', 14602], ['id', 42713], ['id', 56082]], 'labels': [7, 2, 4, 1, 8], 'scores': [0.6859820783138275, 0.6981717944145203, 0.7135953307151794, 0.5766435265541077, 0.6650223135948181]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8805696368217468})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.470697283744812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46295982599258423})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4766741394996643})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4604138433933258})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4567025303840637})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46324437856674194})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4792594909667969})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4554772973060608})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.500443160533905})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5210148096084595})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5244107246398926})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.460730517578125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 18473], ['id', 16692], ['id', 36363], ['id', 21529], ['id', 36324]], 'labels': [4, 5, 6, 8, 3], 'scores': [1.0475423336029053, 0.9620442688465118, 1.1049684286117554, 1.0683491230010986, 0.7328338027000427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8728340268135071})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47976404428482056})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42523834109306335})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4218154549598694})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42912474274635315})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49538829922676086})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45164865255355835})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.942, 'crossentropy': 0.3948263671875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 55153], ['id', 212], ['id', 17190], ['id', 38597], ['id', 22481]], 'labels': [8, 7, 9, 9, 7], 'scores': [0.8832764625549316, 0.4234301447868347, 0.6547850370407104, 0.7070114612579346, 0.6182547807693481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7593209743499756})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47110041975975037})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4091781973838806})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3920939862728119})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3923380970954895})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44879311323165894})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4328887462615967})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9475, 'crossentropy': 0.371564990234375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 13538], ['id', 40966], ['id', 27065], ['id', 57311], ['id', 9415]], 'labels': [5, 5, 5, 5, 1], 'scores': [0.8244381546974182, 0.7413158416748047, 0.6879326701164246, 0.6979359984397888, 0.3090564012527466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8300586342811584})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4766347408294678})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.435430109500885})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4302111864089966})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4205302596092224})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43623873591423035})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42404550313949585})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42374685406684875})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9486, 'crossentropy': 0.37225439453125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 31608], ['id', 47662], ['ood', 13262], ['id', 36889], ['ood', 8485]], 'labels': [2, 9, 1, 7, 0], 'scores': [0.7850984036922455, 1.003951072692871, 0.537816047668457, 0.47319984436035156, 0.33064305782318115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8949155211448669})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4849764108657837})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4168640971183777})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43815141916275024})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.388253390789032})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4404045343399048})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41672515869140625})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4227592349052429})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.361589111328125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 16951], ['id', 57882], ['id', 12748], ['id', 53330], ['id', 45954]], 'labels': [8, 0, 0, 1, 8], 'scores': [0.7493699789047241, 0.8588438630104065, 0.6202573180198669, 0.6948786377906799, 0.6329801082611084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8522550463676453})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47893768548965454})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40655070543289185})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3785030245780945})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4015094041824341})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3720727264881134})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3756450414657593})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39712440967559814})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4122162461280823})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9493, 'crossentropy': 0.338829736328125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 34407], ['id', 515], ['id', 49958], ['id', 17262], ['id', 2934]], 'labels': [3, 2, 7, 1, 9], 'scores': [0.7995581924915314, 0.319374680519104, 0.7431471347808838, 0.694857656955719, 0.7742948532104492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7970865964889526})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49302566051483154})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4146372079849243})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4100220799446106})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3985954523086548})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4111725389957428})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4053821563720703})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4359636902809143})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.3826400390625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 37887], ['id', 13572], ['id', 23814], ['id', 30688], ['id', 50233]], 'labels': [9, 9, 2, 8, 7], 'scores': [0.6177369952201843, 0.614332914352417, 0.7609847187995911, 0.9100099802017212, 0.4763239324092865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9915655255317688})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5279502868652344})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40083640813827515})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4073910415172577})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36161375045776367})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3828360140323639})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37687820196151733})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34901857376098633})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3824749290943146})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37531134486198425})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40204811096191406})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3407605224609375}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 22094], ['id', 56468], ['ood', 47647], ['ood', 37971], ['id', 14650]], 'labels': [7, 5, 2, 8, 4], 'scores': [0.6557134985923767, 0.7061700224876404, 0.8368003368377686, 0.4342970848083496, 0.7720032334327698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0270626544952393})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.501981258392334})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4205666780471802})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39953669905662537})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40346837043762207})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39337635040283203})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41621944308280945})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41661548614501953})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4171043932437897})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9433, 'crossentropy': 0.3802093505859375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 12938], ['id', 8417], ['id', 52971], ['id', 51261], ['id', 44948]], 'labels': [2, 6, 2, 4, 9], 'scores': [0.7892719209194183, 0.491798996925354, 0.5602864623069763, 0.6270797252655029, 0.5639639496803284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9205783605575562})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48876282572746277})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4221653938293457})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3787546753883362})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39508774876594543})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38205957412719727})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4114602208137512})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.3348265869140625}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 26947], ['id', 2172], ['id', 23490], ['id', 20989], ['id', 38932]], 'labels': [8, 5, 3, 3, 5], 'scores': [0.7245523929595947, 0.5476067066192627, 0.6646603345870972, 0.7854571342468262, 0.6482896208763123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9685181379318237})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.535570502281189})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41401827335357666})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37029391527175903})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37122416496276855})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4085356593132019})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3835155963897705})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9513, 'crossentropy': 0.34733330078125}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 45048], ['id', 48388], ['id', 52922], ['id', 8045], ['id', 15630]], 'labels': [4, 9, 3, 8, 3], 'scores': [0.5968790054321289, 0.5048713684082031, 0.7168655395507812, 0.5479706525802612, 0.6641885638237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1131342649459839})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5291217565536499})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42180562019348145})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38185393810272217})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4042680263519287})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4156950116157532})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.412744402885437})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9516, 'crossentropy': 0.3383178955078125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 27793], ['id', 1512], ['id', 25301], ['id', 54181], ['id', 40708]], 'labels': [1, 0, 8, 9, 8], 'scores': [0.8431662917137146, 0.6360659599304199, 0.6077042818069458, 0.5929260849952698, 0.7362974882125854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9162291288375854})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4872158169746399})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42982062697410583})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3942893147468567})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40104395151138306})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38265761733055115})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42098551988601685})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4019326865673065})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4039551615715027})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.954, 'crossentropy': 0.3436062255859375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 7074], ['id', 17934], ['id', 17178], ['id', 19124], ['id', 8865]], 'labels': [1, 4, 8, 8, 3], 'scores': [0.6515412330627441, 0.5519464612007141, 0.6210300922393799, 0.7516800761222839, 0.7064722180366516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9164606332778931})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.470768004655838})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.410983145236969})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3303665220737457})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3959228992462158})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35541433095932007})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.350680947303772})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.3320837158203125}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 12373], ['id', 6670], ['id', 8443], ['id', 17472], ['id', 27646]], 'labels': [7, 6, 2, 1, 8], 'scores': [0.697925329208374, 0.4914218783378601, 0.6588525176048279, 0.6103348135948181, 0.5977539420127869]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 1.0239075422286987})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5256134867668152})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43553146719932556})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38634437322616577})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34137198328971863})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34777605533599854})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.336517333984375})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3425843417644501})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3891304135322571})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3877222537994385})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9596, 'crossentropy': 0.3074951416015625}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 31140], ['id', 42793], ['id', 57718], ['id', 59297], ['id', 28136]], 'labels': [3, 4, 7, 1, 8], 'scores': [0.497084379196167, 0.866558849811554, 0.8628992438316345, 0.7477487921714783, 0.7624281644821167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0729221105575562})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5294251441955566})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4653111696243286})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38883867859840393})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4206741750240326})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4145559072494507})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3932185769081116})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9519, 'crossentropy': 0.35921484375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 52083], ['id', 25144], ['id', 17300], ['id', 9472], ['id', 40308]], 'labels': [2, 5, 4, 2, 7], 'scores': [0.7465515732765198, 0.6530969142913818, 0.48910999298095703, 0.8753318190574646, 0.710939884185791]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8890935778617859})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4782503843307495})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38245218992233276})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33940720558166504})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35089874267578125})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.330519437789917})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3249794542789459})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3954601287841797})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36276739835739136})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3768351674079895})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.2882636962890625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 23968], ['id', 33150], ['id', 37427], ['id', 21659], ['id', 20771]], 'labels': [7, 8, 2, 8, 8], 'scores': [0.4972468614578247, 0.691949725151062, 0.6894411444664001, 0.5531432032585144, 0.5882779955863953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.935575008392334})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5097775459289551})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37774574756622314})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34872567653656006})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34083276987075806})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32025274634361267})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3489484190940857})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3104953467845917})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3486015200614929})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3246324360370636})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3322622776031494})
store['active_learning_steps'][48]['training']['best_epoch']=8
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.29729326171875}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 18501], ['id', 54814], ['id', 24601], ['id', 44123], ['id', 9608]], 'labels': [4, 4, 4, 8, 8], 'scores': [0.8735954165458679, 0.8393433094024658, 0.660943865776062, 0.663667619228363, 0.9852499961853027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1516098976135254})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5723317265510559})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43368834257125854})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39111876487731934})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35955995321273804})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3640304505825043})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3645714521408081})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3464720547199249})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3625953197479248})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35688334703445435})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37037694454193115})
store['active_learning_steps'][49]['training']['best_epoch']=8
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.2993566162109375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 45925], ['id', 13259], ['id', 52086], ['id', 59335], ['id', 59309]], 'labels': [9, 1, 5, 4, 8], 'scores': [0.6438791453838348, 1.0316683650016785, 1.0762090682983398, 0.5875198245048523, 0.956624448299408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0574417114257812})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4767201542854309})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40729567408561707})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3343249559402466})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3221997618675232})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31743597984313965})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3121213912963867})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33213353157043457})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3259311020374298})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35001036524772644})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.259938720703125}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 37643], ['id', 29410], ['ood', 22029], ['id', 13376], ['id', 32766]], 'labels': [3, 5, 2, 3, 8], 'scores': [0.733680009841919, 0.6132631301879883, 0.5989136695861816, 0.678632378578186, 0.6107888221740723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.94284588098526})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5248428583145142})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3560866415500641})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36530327796936035})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3199123740196228})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34286272525787354})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3403809666633606})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3029167652130127})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3144325911998749})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3415556848049164})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3523552417755127})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2583320068359375}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 39673], ['id', 21589], ['id', 17958], ['id', 54937], ['id', 52800]], 'labels': [2, 8, 9, 7, 9], 'scores': [0.7548583447933197, 0.6304425001144409, 0.8229755759239197, 0.7938646078109741, 0.8587951064109802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 1.022693157196045})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4795829653739929})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3504980206489563})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32178086042404175})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3161594867706299})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28228238224983215})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3052217960357666})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32706236839294434})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30347779393196106})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.2501559326171875}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 57124], ['id', 4955], ['id', 7924], ['id', 31919], ['id', 19086]], 'labels': [5, 2, 8, 9, 7], 'scores': [0.7294300198554993, 0.87897789478302, 0.727792501449585, 0.7322775721549988, 0.4741535782814026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0833125114440918})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.554767370223999})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4415006637573242})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39166122674942017})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3771515488624573})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3285195529460907})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33544886112213135})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3590124249458313})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3372299075126648})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.281153564453125}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 12018], ['id', 6846], ['ood', 13840], ['id', 2076], ['id', 9147]], 'labels': [7, 2, 5, 3, 4], 'scores': [0.6492090225219727, 0.7607451677322388, 0.5690304040908813, 0.8485897779464722, 0.7922706604003906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0951321125030518})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5781487226486206})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4389764070510864})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35242778062820435})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31554722785949707})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34598690271377563})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3529857397079468})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3802306354045868})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.279376220703125}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 45250], ['id', 51818], ['id', 52548], ['id', 24943], ['id', 52708]], 'labels': [5, 0, 2, 3, 4], 'scores': [0.6642211079597473, 0.26608267426490784, 0.6416552066802979, 0.6075717210769653, 0.5474671721458435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0249131917953491})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.559607744216919})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37817418575286865})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36510366201400757})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.335534930229187})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35048651695251465})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33964234590530396})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36702418327331543})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2806505126953125}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 14078], ['id', 18166], ['id', 36792], ['id', 31312], ['id', 29638]], 'labels': [5, 9, 6, 9, 4], 'scores': [0.3546002507209778, 0.6532504558563232, 0.668490469455719, 0.6074943542480469, 0.5097206234931946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.064863681793213})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.510613739490509})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3619963526725769})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3617469072341919})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3568207025527954})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3582782745361328})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.335345983505249})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3263312578201294})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3525036573410034})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3265189230442047})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3250153958797455})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3154008388519287})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3788730800151825})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3819305896759033})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3756518065929413})
store['active_learning_steps'][56]['training']['best_epoch']=12
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.2703925048828125}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 9774], ['id', 32276], ['id', 49910], ['id', 8221], ['id', 7793]], 'labels': [7, 3, 6, 8, 8], 'scores': [0.6812283396720886, 0.8723783493041992, 0.8920193314552307, 0.7963671684265137, 1.043962836265564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9149391651153564})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5072176456451416})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37623363733291626})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3191054165363312})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3126581907272339})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3254425525665283})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3146190643310547})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29741281270980835})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3031335175037384})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3115044832229614})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30677083134651184})
store['active_learning_steps'][57]['training']['best_epoch']=8
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.2435122314453125}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 6920], ['id', 5216], ['id', 43230], ['id', 57742], ['id', 55396]], 'labels': [3, 2, 3, 6, 5], 'scores': [0.7473966479301453, 0.7093770503997803, 0.48175859451293945, 0.7291780114173889, 0.7527872323989868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0976760387420654})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.49818575382232666})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.350327730178833})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3616079092025757})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3332178294658661})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3062554597854614})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32870548963546753})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31582629680633545})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33556002378463745})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.273057666015625}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 29530], ['id', 13969], ['id', 30900], ['id', 12940], ['id', 16590]], 'labels': [4, 3, 5, 5, 6], 'scores': [0.5593568086624146, 0.9355804920196533, 0.8421263098716736, 0.6137940585613251, 0.6193469166755676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.143113613128662})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5263198018074036})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40505868196487427})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3457723557949066})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28861337900161743})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3094128966331482})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31030064821243286})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35114213824272156})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.2777725830078125}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 47628], ['id', 26581], ['id', 27085], ['id', 48382], ['id', 31011]], 'labels': [3, 1, 8, 8, 3], 'scores': [0.474453866481781, 0.3399001359939575, 0.7983032464981079, 0.5747063159942627, 0.6203010678291321]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.9134700298309326})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4406226873397827})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36729153990745544})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31673991680145264})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29940447211265564})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31742215156555176})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.320237398147583})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32031556963920593})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.2620188720703125}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 6347], ['id', 55438], ['id', 48912], ['id', 10762], ['id', 56130]], 'labels': [3, 8, 2, 3, 6], 'scores': [0.6797298789024353, 0.5284207463264465, 0.6916173100471497, 0.4093390703201294, 0.6817194223403931]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.058387041091919})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5059218406677246})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3726732134819031})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3594513237476349})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3206908106803894})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32826241850852966})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35608208179473877})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3263635039329529})
store['active_learning_steps'][61]['training']['best_epoch']=5
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.28857734375}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 17365], ['id', 41713], ['id', 21279], ['id', 1058], ['id', 22364]], 'labels': [0, 0, 0, 2, 0], 'scores': [0.48709630966186523, 0.6570686101913452, 0.6620098352432251, 0.5302855372428894, 0.625129222869873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.052263617515564})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.56169193983078})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4128504991531372})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33294278383255005})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34391355514526367})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33163386583328247})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3251120448112488})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3288135528564453})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3249051570892334})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31810063123703003})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3363184332847595})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34849151968955994})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.31206029653549194})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3137866258621216})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3302558660507202})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3260175883769989})
store['active_learning_steps'][62]['training']['best_epoch']=13
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2789811279296875}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 39942], ['id', 5332], ['id', 14067], ['id', 42086], ['id', 9116]], 'labels': [9, 3, 4, 9, 4], 'scores': [1.1756131649017334, 0.6430587768554688, 0.3997765779495239, 0.6954749822616577, 0.5306636989116669]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0532870292663574})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.59615159034729})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40373045206069946})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3349587321281433})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3089117109775543})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34083041548728943})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2985670566558838})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29467809200286865})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2956555485725403})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3027312755584717})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31665098667144775})
store['active_learning_steps'][63]['training']['best_epoch']=8
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.279011328125}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 57659], ['id', 57575], ['id', 13878], ['id', 52129], ['id', 59747]], 'labels': [0, 0, 4, 3, 5], 'scores': [0.5405853390693665, 0.8264669179916382, 0.7831482887268066, 0.49323877692222595, 0.7731524109840393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.156760811805725})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5333566069602966})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4000394940376282})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33416324853897095})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.298842191696167})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29701223969459534})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27895253896713257})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28891611099243164})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33319413661956787})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2840089499950409})
store['active_learning_steps'][64]['training']['best_epoch']=7
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.25613720703125}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 4066], ['id', 46246], ['id', 42774], ['id', 22597], ['id', 52210]], 'labels': [1, 3, 4, 9, 5], 'scores': [0.8884762525558472, 0.582556426525116, 0.6121620535850525, 0.8035873770713806, 0.8837226629257202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.190910816192627})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5647464990615845})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40917909145355225})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3352777361869812})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3907724618911743})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2885381579399109})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30946511030197144})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31150227785110474})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29751306772232056})
store['active_learning_steps'][65]['training']['best_epoch']=6
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2701390625}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 50826], ['id', 34906], ['id', 16446], ['ood', 51590], ['id', 11951]], 'labels': [2, 3, 5, 5, 3], 'scores': [0.6595149636268616, 0.6986823976039886, 0.5402575731277466, 0.3081681728363037, 0.5683572888374329]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1837141513824463})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5935022830963135})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4116446375846863})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34754496812820435})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3549520969390869})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.318619966506958})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33516255021095276})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2997344136238098})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32269519567489624})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3325885534286499})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3170250952243805})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2621130859375}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 19576], ['id', 55314], ['id', 42838], ['id', 41464], ['id', 15880]], 'labels': [9, 6, 9, 8, 5], 'scores': [0.8296867609024048, 0.7541400790214539, 0.6696063876152039, 0.9422255158424377, 0.5663687288761139]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.254760980606079})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5815629959106445})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39584434032440186})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34845972061157227})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3261871933937073})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3211197555065155})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31873762607574463})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28129035234451294})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30491146445274353})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28229817748069763})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3045221269130707})
store['active_learning_steps'][67]['training']['best_epoch']=8
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.25233134765625}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 33066], ['id', 19866], ['id', 5065], ['id', 18598], ['id', 5370]], 'labels': [0, 3, 2, 9, 3], 'scores': [0.6898125410079956, 0.7253112196922302, 0.6084396243095398, 0.8307517766952515, 0.8672453761100769]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1608903408050537})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5347709059715271})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.429959774017334})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3380613327026367})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3396863341331482})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29243436455726624})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2763019800186157})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30619537830352783})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27660608291625977})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29035231471061707})
store['active_learning_steps'][68]['training']['best_epoch']=7
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2638955322265625}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 49616], ['id', 43474], ['ood', 43860], ['id', 26733], ['id', 31395]], 'labels': [7, 3, 9, 2, 3], 'scores': [0.8723727464675903, 0.6831232905387878, 0.349098801612854, 0.8148117661476135, 0.627689003944397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1908683776855469})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5966593623161316})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3909016251564026})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3146619498729706})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31185048818588257})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3201397657394409})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2956526279449463})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2915906012058258})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2956576645374298})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2778061032295227})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28042006492614746})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2668406367301941})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2918332517147064})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2944612503051758})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2827149033546448})
store['active_learning_steps'][69]['training']['best_epoch']=12
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.25004853515625}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 29922], ['id', 59354], ['id', 32856], ['id', 26983], ['id', 38974]], 'labels': [4, 1, 2, 6, 1], 'scores': [0.7267428040504456, 0.5710516571998596, 0.5406155586242676, 0.7039406001567841, 0.7083775401115417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1630102396011353})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.519932746887207})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4070824980735779})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3648887872695923})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29262232780456543})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3237107992172241})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3103259801864624})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2985026240348816})
store['active_learning_steps'][70]['training']['best_epoch']=5
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2956132080078125}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 1361], ['id', 25823], ['id', 21242], ['id', 25482], ['id', 26079]], 'labels': [2, 0, 0, 8, 8], 'scores': [0.4687679409980774, 0.7657455205917358, 0.6442049145698547, 0.43627023696899414, 0.7116619944572449]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.1837372779846191})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5905734300613403})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4229363203048706})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32868456840515137})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3397117555141449})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2847896218299866})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2617310881614685})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26999589800834656})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25825977325439453})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2462063431739807})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25368309020996094})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2637253403663635})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3026573657989502})
store['active_learning_steps'][71]['training']['best_epoch']=10
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9738, 'crossentropy': 0.2390635009765625}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 32016], ['id', 46899], ['id', 53999], ['id', 48726], ['id', 24004]], 'labels': [9, 3, 8, 8, 5], 'scores': [0.903449535369873, 0.6724127531051636, 0.6754123568534851, 1.0391297936439514, 0.7138529717922211]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.192460298538208})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5765968561172485})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39421531558036804})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34925052523612976})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32665085792541504})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2930937707424164})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2896795868873596})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28785407543182373})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26606082916259766})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2838420867919922})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2767508029937744})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30374234914779663})
store['active_learning_steps'][72]['training']['best_epoch']=9
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.242993798828125}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 32776], ['id', 38698], ['id', 57139], ['id', 1075], ['id', 35276]], 'labels': [4, 5, 2, 7, 5], 'scores': [0.9312205910682678, 0.8544832468032837, 0.6983785629272461, 0.9689309000968933, 0.7234362363815308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.211210012435913})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5413281917572021})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3643922507762909})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.319663941860199})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3009355664253235})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27981066703796387})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2824857831001282})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2730497717857361})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2958497703075409})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2859042286872864})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2783997654914856})
store['active_learning_steps'][73]['training']['best_epoch']=8
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.2582347412109375}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 52914], ['id', 24059], ['id', 4058], ['id', 24512], ['id', 8449]], 'labels': [5, 3, 8, 3, 0], 'scores': [0.6223830580711365, 0.7216157913208008, 0.6060439348220825, 0.5674721598625183, 0.7933381795883179]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.2007637023925781})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5688204765319824})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4117271900177002})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34600532054901123})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2953782081604004})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30335694551467896})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2800566256046295})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28466349840164185})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27410537004470825})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2903466820716858})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3239162564277649})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30526137351989746})
store['active_learning_steps'][74]['training']['best_epoch']=9
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.2485931640625}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 51863], ['id', 22139], ['id', 33694], ['id', 48681], ['id', 55268]], 'labels': [9, 2, 3, 2, 8], 'scores': [0.9235124588012695, 0.9126280546188354, 0.6713728904724121, 0.872027575969696, 0.5248990654945374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0982842445373535})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5297091007232666})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44838839769363403})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33694106340408325})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3180004060268402})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31593483686447144})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28639739751815796})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27620458602905273})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27746036648750305})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2820108234882355})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3008822500705719})
store['active_learning_steps'][75]['training']['best_epoch']=8
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2536733154296875}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 15745], ['id', 37680], ['id', 13159], ['id', 10255], ['id', 17121]], 'labels': [9, 5, 2, 5, 8], 'scores': [0.5989627242088318, 0.6199924647808075, 0.42458027601242065, 0.550430417060852, 0.692724347114563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1359975337982178})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.6047606468200684})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4636685252189636})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32779937982559204})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3439529240131378})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31401491165161133})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27944451570510864})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28906118869781494})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3047049045562744})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2951395511627197})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2698984375}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 40449], ['ood', 8352], ['id', 11377], ['id', 19606], ['id', 46906]], 'labels': [4, 3, 3, 2, 7], 'scores': [0.4165570139884949, 0.40306246280670166, 0.8513311743736267, 0.5372091829776764, 0.6177870631217957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.186319351196289})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5821100473403931})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4256250858306885})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3576653003692627})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3081151843070984})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3152020573616028})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2934214770793915})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3023242950439453})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3344178795814514})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2944454550743103})
store['active_learning_steps'][77]['training']['best_epoch']=7
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2521613037109375}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 23406], ['id', 15803], ['id', 4165], ['id', 36268], ['id', 3251]], 'labels': [4, 1, 2, 5, 8], 'scores': [0.779052734375, 0.8017997741699219, 0.9706918597221375, 0.7975011467933655, 0.5852044224739075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1120431423187256})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.6011945009231567})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4040523171424866})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30851203203201294})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2990351915359497})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3053973615169525})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28365617990493774})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2639508843421936})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28302836418151855})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28128162026405334})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2866290807723999})
store['active_learning_steps'][78]['training']['best_epoch']=8
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2403286376953125}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 23448], ['id', 59294], ['id', 55015], ['id', 3432], ['id', 17494]], 'labels': [7, 8, 8, 8, 5], 'scores': [0.4448698163032532, 0.8650021553039551, 0.6397632360458374, 0.49916255474090576, 0.7376596927642822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.166070580482483})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6593374609947205})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4266020655632019})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38276833295822144})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30081871151924133})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2726820707321167})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28852373361587524})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.287024587392807})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27259570360183716})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25781121850013733})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2988930940628052})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27191436290740967})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28883981704711914})
store['active_learning_steps'][79]['training']['best_epoch']=10
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.249206494140625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 20714], ['id', 27758], ['id', 27448], ['id', 7267], ['id', 46284]], 'labels': [4, 7, 9, 0, 9], 'scores': [0.5013264417648315, 0.6467058956623077, 0.6781762838363647, 0.513327419757843, 0.6413179636001587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1002612113952637})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5767050981521606})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.414553701877594})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3480353355407715})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3057863116264343})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29796862602233887})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27581578493118286})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26721251010894775})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2936270236968994})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2543530762195587})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30335354804992676})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2676449120044708})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2603271007537842})
store['active_learning_steps'][80]['training']['best_epoch']=10
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9741, 'crossentropy': 0.230993798828125}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 36606], ['id', 12651], ['id', 35205], ['id', 40530], ['id', 47680]], 'labels': [9, 9, 6, 2, 4], 'scores': [0.6776853203773499, 0.8871691823005676, 0.9062792062759399, 0.7894176840782166, 0.6532312035560608]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2322055101394653})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.591543436050415})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38573122024536133})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3361167907714844})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32614269852638245})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30701005458831787})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29330891370773315})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29910340905189514})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2811588943004608})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3200773298740387})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28309714794158936})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2861591577529907})
store['active_learning_steps'][81]['training']['best_epoch']=9
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2476486083984375}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 2574], ['id', 37336], ['id', 12102], ['id', 24928], ['id', 51759]], 'labels': [7, 6, 4, 7, 3], 'scores': [0.6824116110801697, 0.6915071606636047, 0.6677184104919434, 0.631767749786377, 0.8044851422309875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.258756399154663})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.6164754629135132})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4212917983531952})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3896729350090027})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3498886823654175})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32801157236099243})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2815582752227783})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2690690755844116})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2905083894729614})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28911644220352173})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2658872604370117})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2979167103767395})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2926030158996582})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31366634368896484})
store['active_learning_steps'][82]['training']['best_epoch']=11
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2572678955078125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 53872], ['id', 23594], ['id', 30037], ['id', 15252], ['id', 44570]], 'labels': [8, 6, 0, 1, 7], 'scores': [0.7931469678878784, 0.4955703616142273, 0.603293389081955, 0.6487857699394226, 0.797167181968689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1212735176086426})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5832761526107788})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4173324704170227})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33230745792388916})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2930948734283447})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27876001596450806})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2725495994091034})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2561311721801758})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2826647162437439})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2715685963630676})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2494415044784546})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2854834198951721})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2903648018836975})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29396677017211914})
store['active_learning_steps'][83]['training']['best_epoch']=11
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9747, 'crossentropy': 0.2321301025390625}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 32426], ['id', 39451], ['id', 50090], ['id', 23812], ['id', 53996]], 'labels': [8, 1, 4, 3, 8], 'scores': [0.860834538936615, 0.703441858291626, 0.7671961784362793, 0.826632022857666, 0.5999670624732971]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2306487560272217})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.645200252532959})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4095819592475891})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3516913056373596})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3447403907775879})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3104110062122345})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29710307717323303})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28899967670440674})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2830964922904968})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.280504047870636})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29439032077789307})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3083555996417999})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2868248224258423})
store['active_learning_steps'][84]['training']['best_epoch']=10
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.2245711181640625}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 59934], ['id', 13099], ['id', 3798], ['id', 43001], ['id', 53558]], 'labels': [0, 3, 7, 9, 3], 'scores': [0.8106278777122498, 0.5460537672042847, 0.7916539311408997, 0.5513485670089722, 0.7071364521980286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2201683521270752})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5797561407089233})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42360594868659973})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31841403245925903})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.303639680147171})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3087139427661896})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27674558758735657})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26931697130203247})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25872987508773804})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2849343419075012})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2581711709499359})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2899571657180786})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32074087858200073})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2952701151371002})
store['active_learning_steps'][85]['training']['best_epoch']=11
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.23472939453125}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 50371], ['id', 53873], ['id', 8940], ['id', 56066], ['id', 11950]], 'labels': [7, 4, 6, 7, 8], 'scores': [0.9445632696151733, 0.988933801651001, 0.7776010632514954, 0.9835443496704102, 0.570183277130127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.364691972732544})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6173872947692871})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.42402535676956177})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2991715669631958})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3018590807914734})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28500431776046753})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25290971994400024})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2659282088279724})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25054579973220825})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2853311002254486})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29793307185173035})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29135239124298096})
store['active_learning_steps'][86]['training']['best_epoch']=9
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9752, 'crossentropy': 0.2220495849609375}
