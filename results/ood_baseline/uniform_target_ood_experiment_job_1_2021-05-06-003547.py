store = {}
store['timestamp']=1620257747
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=1']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=1
store['worker_id']=1
store['num_workers']=40
store['config']={'seed': 1, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.2121522426605225})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.592459201812744})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5327870845794678})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0106239318847656})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6488, 'crossentropy': 2.0698455078125}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 19102], ['id', 37189], ['id', 19072], ['id', 32178], ['id', 26315], ['id', 47625], ['ood', 51511], ['id', 2881], ['id', 36502], ['id', 11794]], 'labels': [4, 0, 0, 4, 0, 3, 3, 7, 4, 0], 'scores': [0.7022647857666016, 1.0724793672561646, 1.0143189430236816, 0.5620789527893066, 0.9335161447525024, 0.7371844053268433, 0.5653772354125977, 0.6288672983646393, 0.9118465483188629, 1.1391395330429077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6879487037658691})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.8349061012268066})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.277324914932251})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.137211561203003})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7242, 'crossentropy': 1.54790625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 59314], ['id', 27915], ['id', 56623], ['id', 25239], ['id', 53220], ['id', 23430], ['id', 39518], ['id', 17794], ['id', 24650], ['id', 50346]], 'labels': [9, 2, 8, 9, 6, 7, 2, 5, 5, 8], 'scores': [0.5584138631820679, 0.9176743626594543, 0.7921438813209534, 0.5849470496177673, 0.6382606625556946, 0.7485500574111938, 0.8651913404464722, 0.6359855532646179, 0.7041392922401428, 0.637041449546814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.3256961107254028})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.6736547946929932})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.7686928510665894})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.840831995010376})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.741, 'crossentropy': 1.32127451171875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12493], ['id', 547], ['id', 47107], ['id', 14862], ['id', 4066], ['id', 30322], ['id', 32438], ['id', 8077], ['id', 59286], ['id', 39493]], 'labels': [8, 6, 5, 5, 1, 8, 2, 3, 8, 5], 'scores': [0.7145688533782959, 0.6511490345001221, 0.6569355726242065, 0.82137131690979, 0.6629924774169922, 0.7714172601699829, 0.6332712769508362, 0.6660712957382202, 0.7145154476165771, 0.6490482687950134]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2248705625534058})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.5012526512145996})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5319433212280273})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.7773082256317139})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7659, 'crossentropy': 1.179375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 12995], ['id', 44928], ['id', 57215], ['id', 40735], ['id', 24435], ['id', 45441], ['id', 9393], ['id', 7917], ['id', 54536], ['id', 38982]], 'labels': [3, 5, 7, 1, 3, 3, 1, 5, 7, 3], 'scores': [0.683193564414978, 0.7004068493843079, 0.5084609985351562, 0.5708989500999451, 0.6574231386184692, 0.5476505756378174, 0.533541202545166, 0.7751596570014954, 0.6454232335090637, 0.7612531185150146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.89028000831604})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9257138967514038})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0372170209884644})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9920675754547119})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8366, 'crossentropy': 0.880986328125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 16916], ['id', 14679], ['id', 42323], ['id', 53838], ['ood', 30830], ['id', 43518], ['id', 33115], ['id', 8060], ['id', 14288], ['id', 52094]], 'labels': [2, 8, 2, 3, 5, 6, 4, 9, 7, 9], 'scores': [0.661253035068512, 0.6468276977539062, 0.7604995965957642, 0.5776481032371521, 0.3940838575363159, 0.8241933584213257, 0.4800506830215454, 0.6994946599006653, 0.5998556017875671, 0.7753432393074036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8124715685844421})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9001399874687195})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9271211624145508})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9521738290786743})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8488, 'crossentropy': 0.78056767578125}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 54974], ['id', 17972], ['id', 44445], ['id', 55639], ['id', 15093], ['id', 43848], ['id', 17147], ['id', 5148], ['id', 6742], ['id', 14744]], 'labels': [5, 9, 0, 5, 2, 8, 9, 3, 6, 9], 'scores': [0.2846362590789795, 0.48529499769210815, 0.637293815612793, 0.5309948325157166, 0.7297055721282959, 0.4678767919540405, 0.6812723278999329, 0.4958062171936035, 0.4005838632583618, 0.6413763761520386]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7718912959098816})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7093759179115295})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7585669755935669})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7262932062149048})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8318884372711182})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8839, 'crossentropy': 0.6773669921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 18643], ['id', 36862], ['id', 20083], ['id', 13742], ['id', 33694], ['id', 5254], ['id', 46524], ['id', 49810], ['id', 46025], ['id', 59603]], 'labels': [2, 3, 1, 9, 3, 5, 6, 3, 8, 8], 'scores': [0.6991071701049805, 0.7731287479400635, 0.590553343296051, 0.8917577862739563, 0.6898624300956726, 0.5538143515586853, 0.7769360542297363, 0.6539602279663086, 0.3993213176727295, 0.7532021403312683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7744817733764648})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7509706020355225})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7906081080436707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7753946781158447})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8347588181495667})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8695, 'crossentropy': 0.720645556640625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 37271], ['id', 35751], ['id', 32256], ['id', 57632], ['id', 23490], ['id', 14655], ['id', 19906], ['id', 32080], ['id', 14367], ['id', 18720]], 'labels': [3, 8, 9, 2, 3, 3, 8, 5, 3, 7], 'scores': [0.6677087545394897, 0.6248105764389038, 0.4157884120941162, 0.7258982062339783, 0.6633925437927246, 0.6341907382011414, 0.649196982383728, 0.6412456035614014, 0.6468807458877563, 0.9358721375465393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7809233665466309})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6293410062789917})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5803806781768799})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.614348292350769})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7158710360527039})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7909796237945557})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.64347666015625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 35097], ['id', 5265], ['id', 5085], ['id', 58312], ['id', 52866], ['id', 17091], ['id', 29757], ['id', 11675], ['id', 9180], ['id', 46237]], 'labels': [5, 4, 4, 5, 7, 4, 3, 0, 3, 8], 'scores': [0.7702785730361938, 0.8146692514419556, 0.6918872594833374, 1.056975781917572, 0.9439310431480408, 0.7332990765571594, 0.8049921989440918, 0.7990366816520691, 0.9322337508201599, 0.7106534838676453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8724840879440308})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6430149078369141})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6453006267547607})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6507664918899536})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6375299692153931})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.688912034034729})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7176902890205383})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7602492570877075})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9184, 'crossentropy': 0.566866357421875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 2184], ['id', 38698], ['id', 45998], ['id', 15924], ['id', 33542], ['id', 52092], ['id', 14697], ['id', 57507], ['id', 27972], ['id', 22579]], 'labels': [2, 5, 2, 6, 6, 7, 8, 0, 8, 2], 'scores': [1.0784181356430054, 0.9933544993400574, 0.8047317564487457, 0.8025817275047302, 0.5279971957206726, 0.9992586970329285, 0.9828989505767822, 0.8273212313652039, 0.9410064220428467, 0.9309116005897522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7832530736923218})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6591016054153442})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.585118293762207})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6355356574058533})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6078548431396484})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6328848600387573})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.564458349609375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 30144], ['id', 35062], ['id', 3168], ['id', 31090], ['id', 33161], ['id', 20360], ['id', 19124], ['id', 16558], ['id', 10521], ['id', 24193]], 'labels': [9, 5, 8, 4, 3, 9, 8, 5, 4, 9], 'scores': [0.8644843101501465, 0.5523277521133423, 0.6561140716075897, 0.629808783531189, 0.5746878683567047, 0.7398131489753723, 0.9314042925834656, 0.6879100799560547, 0.5159005522727966, 0.791204571723938]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8615087270736694})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6460037231445312})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5085079669952393})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6649007201194763})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6228673458099365})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6650979518890381})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.501023046875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 39545], ['id', 13639], ['id', 39734], ['id', 16754], ['id', 38257], ['id', 55537], ['id', 12972], ['id', 11708], ['id', 48586], ['id', 1059]], 'labels': [2, 8, 2, 2, 7, 8, 4, 3, 5, 8], 'scores': [0.8950092196464539, 0.7369645237922668, 0.8886033296585083, 0.8897120356559753, 0.4062419831752777, 0.35578393936157227, 0.8841460943222046, 0.7892414331436157, 0.7250692248344421, 0.6757350564002991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.843500018119812})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5634033679962158})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5840593576431274})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5560753345489502})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5717679858207703})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6119208335876465})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5585697293281555})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.513896875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 53170], ['id', 56874], ['id', 12211], ['id', 48248], ['id', 23582], ['id', 28710], ['id', 14201], ['id', 17739], ['id', 17553], ['id', 30493]], 'labels': [8, 8, 3, 2, 8, 8, 7, 5, 3, 1], 'scores': [1.0875845551490784, 0.7381427884101868, 0.7088093757629395, 0.7160575091838837, 0.7147728204727173, 0.8483904600143433, 0.6921902298927307, 0.9681923389434814, 0.7774011492729187, 0.8104286193847656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.87066650390625})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5454443693161011})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5918052196502686})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5202385783195496})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5937420129776001})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5930572748184204})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6351006031036377})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.47802421875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 20169], ['id', 44862], ['id', 59574], ['ood', 5034], ['id', 56279], ['id', 24779], ['id', 28762], ['id', 21674], ['id', 17059], ['id', 49589]], 'labels': [4, 0, 5, 5, 9, 6, 5, 2, 6, 3], 'scores': [0.7550922632217407, 0.728925883769989, 0.7059081196784973, 0.5142472982406616, 0.7394130229949951, 0.5350174903869629, 0.7650602161884308, 0.442198246717453, 0.729117751121521, 0.8165063261985779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9163415431976318})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5551855564117432})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.592930793762207})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5443140864372253})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5355015993118286})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5555591583251953})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5596518516540527})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5727294683456421})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.47121669921875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 6618], ['id', 16637], ['id', 14286], ['id', 11240], ['id', 58249], ['id', 58413], ['id', 8719], ['id', 53006], ['id', 40224], ['id', 14813]], 'labels': [8, 8, 3, 0, 3, 9, 8, 8, 4, 6], 'scores': [0.7491828799247742, 0.8558334112167358, 0.9048745632171631, 1.059004008769989, 0.7237294316291809, 0.7576780319213867, 0.7748532295227051, 0.802595853805542, 0.6901228427886963, 0.6454696655273438]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.888922929763794})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5237975716590881})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4735081195831299})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4695499539375305})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5034621357917786})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46259817481040955})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46219906210899353})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.523989200592041})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5231502056121826})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5625976920127869})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.423836279296875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 29725], ['id', 13021], ['id', 637], ['id', 54532], ['id', 32835], ['id', 16913], ['id', 45274], ['id', 54146], ['id', 31200], ['ood', 15119]], 'labels': [6, 5, 1, 7, 7, 4, 6, 9, 9, 0], 'scores': [0.7888920307159424, 0.8291317224502563, 0.4059361517429352, 0.766266942024231, 0.7049262523651123, 0.6477327346801758, 0.8885241150856018, 0.7878679633140564, 0.8221873641014099, 0.8757234215736389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9031565189361572})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5223116278648376})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4638403654098511})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47341567277908325})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4572030305862427})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4533730149269104})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43135613203048706})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4768124222755432})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.505018949508667})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4749533236026764})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9468, 'crossentropy': 0.3883044921875}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 38135], ['id', 24263], ['id', 19324], ['id', 1554], ['id', 51154], ['id', 21660], ['id', 16022], ['id', 17182], ['id', 30658], ['id', 8879]], 'labels': [5, 9, 2, 4, 3, 3, 8, 4, 4, 3], 'scores': [0.6704424619674683, 0.7914678454399109, 0.7537115812301636, 0.7601673007011414, 0.7227541208267212, 1.138359248638153, 0.9606202244758606, 0.7136675119400024, 0.8626107573509216, 0.8583329319953918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0130200386047363})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4941786527633667})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.503920316696167})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4618085026741028})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4368109703063965})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4423303008079529})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48491260409355164})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4308241605758667})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4575725495815277})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45731157064437866})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49522703886032104})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.953, 'crossentropy': 0.3650270263671875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 31919], ['id', 35464], ['id', 30932], ['id', 2369], ['id', 26424], ['id', 3220], ['id', 20820], ['id', 23104], ['id', 33224], ['id', 47870]], 'labels': [9, 9, 0, 8, 9, 3, 9, 0, 1, 9], 'scores': [0.890547513961792, 0.712737500667572, 0.9316928386688232, 0.6608206629753113, 0.6471838355064392, 0.639328122138977, 0.8985515236854553, 0.9754853248596191, 0.7649492919445038, 0.7782321572303772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9501845836639404})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5694987773895264})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4745158851146698})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47199904918670654})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41259241104125977})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4530237317085266})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4199267029762268})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4365438222885132})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9554, 'crossentropy': 0.3440145263671875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 25945], ['id', 25148], ['id', 49282], ['id', 52744], ['id', 12264], ['id', 44128], ['id', 52109], ['id', 28856], ['id', 49517], ['id', 37118]], 'labels': [1, 2, 2, 7, 0, 6, 2, 8, 6, 3], 'scores': [0.5501879751682281, 0.6408217549324036, 0.7065086960792542, 0.7428974509239197, 0.6667516231536865, 0.6026166677474976, 0.6894848942756653, 0.7674299478530884, 0.8252339363098145, 0.8832657933235168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9242680668830872})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5198657512664795})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.449341356754303})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4483293294906616})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4217112064361572})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43639808893203735})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4466957151889801})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4772953391075134})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.3679484619140625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 14894], ['id', 53358], ['id', 32656], ['id', 26358], ['id', 18824], ['id', 53076], ['id', 21880], ['ood', 21362], ['id', 10156], ['id', 10293]], 'labels': [5, 3, 3, 3, 7, 2, 2, 5, 1, 1], 'scores': [0.8012715578079224, 0.6996182203292847, 0.4797351658344269, 0.9042249321937561, 0.7692182660102844, 0.5794278979301453, 0.877414345741272, 0.3873027563095093, 0.6219965219497681, 0.7734830379486084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.920814037322998})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5044929385185242})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40397268533706665})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41889119148254395})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39435988664627075})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38749054074287415})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4060560464859009})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4302612245082855})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3952665627002716})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.31444052734375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 42108], ['id', 10994], ['id', 25966], ['id', 57898], ['id', 34542], ['id', 5129], ['id', 30351], ['id', 28267], ['id', 7984], ['ood', 48988]], 'labels': [5, 3, 5, 8, 1, 2, 5, 5, 4, 1], 'scores': [0.8855677247047424, 0.8744511008262634, 0.8198332190513611, 0.7457178831100464, 0.953410267829895, 0.8813448548316956, 0.4263206422328949, 0.6198337376117706, 0.8594462871551514, 0.43611741065979004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9664158225059509})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5284144878387451})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4567580819129944})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3976458013057709})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41603460907936096})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4321887493133545})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4410141706466675})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9503, 'crossentropy': 0.363789404296875}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 13772], ['id', 35732], ['id', 17849], ['id', 32404], ['id', 44206], ['id', 19892], ['id', 6324], ['id', 40466], ['id', 55001], ['ood', 16217]], 'labels': [5, 9, 7, 8, 8, 5, 5, 8, 2, 7], 'scores': [0.3140542507171631, 0.541359007358551, 0.5903413891792297, 0.6131864786148071, 0.5426139235496521, 0.7007344961166382, 0.5275119841098785, 0.9062361717224121, 0.8236415386199951, 0.4028196334838867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.057227373123169})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5272684693336487})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44407474994659424})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3954247832298279})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4044986665248871})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4055596590042114})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3869062662124634})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4219030737876892})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43056535720825195})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.436450332403183})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.96, 'crossentropy': 0.30689736328125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 16302], ['id', 28014], ['id', 26850], ['id', 34860], ['id', 48973], ['ood', 52667], ['id', 38613], ['id', 31677], ['id', 40334], ['id', 52624]], 'labels': [4, 7, 2, 4, 8, 5, 8, 0, 4, 1], 'scores': [0.6633661985397339, 0.7238072156906128, 0.7251107096672058, 0.8640307784080505, 0.6465598940849304, 0.4501417875289917, 0.5973391532897949, 0.704677164554596, 0.7751283645629883, 0.9019286036491394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9590672254562378})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5462371110916138})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4565771222114563})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38580361008644104})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3937446177005768})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3906779885292053})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4088190197944641})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9564, 'crossentropy': 0.33972548828125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 866], ['id', 602], ['id', 21692], ['id', 52140], ['id', 9633], ['id', 42334], ['id', 8731], ['id', 28319], ['id', 8140], ['id', 54074]], 'labels': [2, 8, 2, 4, 9, 5, 5, 9, 6, 3], 'scores': [0.7692141234874725, 0.7265903353691101, 0.7508766651153564, 0.6169456243515015, 0.7477848529815674, 0.6416836380958557, 0.7190805673599243, 0.5268246531486511, 0.5229603052139282, 0.6042329668998718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0133073329925537})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4794214963912964})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3956632614135742})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3541736900806427})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3651382327079773})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34618082642555237})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36107826232910156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36381858587265015})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37994277477264404})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.959, 'crossentropy': 0.2986112060546875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 43212], ['id', 34552], ['id', 262], ['id', 31512], ['id', 39316], ['id', 55743], ['id', 50308], ['id', 49582], ['id', 14580], ['id', 45770]], 'labels': [5, 3, 2, 2, 7, 3, 3, 2, 9, 5], 'scores': [0.6952266097068787, 0.615613579750061, 0.7032046914100647, 0.9040145874023438, 0.8093248009681702, 0.8199213743209839, 0.5506657660007477, 0.5196419954299927, 0.8688693046569824, 0.46209830045700073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.044479250907898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5139434933662415})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3920682966709137})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35762834548950195})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3728839159011841})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35160744190216064})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3506515622138977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3502834439277649})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3484036922454834})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36438819766044617})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3436990976333618})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3739689588546753})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3587096929550171})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3382127285003662})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.352746844291687})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39069604873657227})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4453079104423523})
store['active_learning_steps'][25]['training']['best_epoch']=14
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.3283890869140625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 24040], ['id', 2000], ['id', 21426], ['id', 6582], ['id', 48115], ['id', 52173], ['id', 39942], ['id', 3095], ['id', 1328], ['id', 48356]], 'labels': [7, 5, 6, 8, 8, 7, 9, 9, 5, 2], 'scores': [0.6874412298202515, 0.6942063271999359, 0.9734975695610046, 1.0188276767730713, 0.7896915078163147, 0.7380045652389526, 0.9467628598213196, 0.37362077832221985, 1.0387741923332214, 0.8218380808830261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9662565588951111})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47667354345321655})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38274118304252625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34454578161239624})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3354097604751587})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33667606115341187})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33857661485671997})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37158626317977905})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.2995622314453125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 48647], ['id', 55194], ['id', 509], ['id', 109], ['id', 20002], ['id', 34829], ['id', 36818], ['id', 25050], ['id', 4784], ['id', 31637]], 'labels': [9, 3, 3, 2, 7, 5, 7, 4, 7, 5], 'scores': [0.6096931099891663, 0.3991071581840515, 0.7279645800590515, 0.7584553956985474, 0.7214156985282898, 0.9186699986457825, 0.5441166162490845, 0.6340706050395966, 0.7251167893409729, 0.7383153438568115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.133040428161621})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5950847864151001})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4261123239994049})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39669060707092285})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3858915865421295})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.353397011756897})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3487507104873657})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3720352351665497})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3289126753807068})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38482969999313354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3799756169319153})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4148795008659363})
store['active_learning_steps'][27]['training']['best_epoch']=9
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.28262919921875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 37233], ['id', 14749], ['id', 2381], ['id', 20146], ['id', 22543], ['id', 54986], ['id', 25789], ['id', 47225], ['id', 9559], ['id', 52646]], 'labels': [9, 0, 7, 1, 8, 8, 3, 3, 8, 9], 'scores': [0.4116887152194977, 1.0990004539489746, 0.5806509256362915, 0.8617933988571167, 1.0037113428115845, 0.7998976111412048, 0.6903344094753265, 0.8231778740882874, 0.9185201525688171, 0.7544805407524109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0183746814727783})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5254842638969421})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34638699889183044})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3399825692176819})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3282032608985901})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33702969551086426})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3480146527290344})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3299885094165802})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.2991513916015625}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 51282], ['id', 28306], ['id', 3644], ['id', 46040], ['id', 52959], ['id', 36892], ['id', 57378], ['id', 46379], ['id', 15745], ['id', 41950]], 'labels': [7, 8, 1, 1, 2, 1, 1, 3, 9, 4], 'scores': [0.42767441272735596, 0.3814912438392639, 0.6699613332748413, 0.5848727226257324, 0.6617349982261658, 0.5765425562858582, 0.42556989192962646, 0.8243456482887268, 0.5332454442977905, 0.6180441975593567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0698106288909912})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5260383486747742})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37162190675735474})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3646806478500366})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32813310623168945})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29129523038864136})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3411520719528198})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.344149112701416})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.365414023399353})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.253631982421875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 2160], ['id', 56586], ['id', 20660], ['id', 45749], ['id', 53497], ['id', 24424], ['ood', 18068], ['id', 27780], ['id', 3691], ['id', 7924]], 'labels': [0, 5, 8, 4, 5, 1, 5, 9, 0, 8], 'scores': [0.5197232365608215, 0.6909058094024658, 0.7030781507492065, 0.4486839771270752, 0.7334391474723816, 0.7842642664909363, 0.31358128786087036, 0.3997683525085449, 0.5987341403961182, 0.8297321796417236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9599647521972656})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.505303144454956})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37843114137649536})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33716413378715515})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3059280514717102})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31746381521224976})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3783194422721863})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30792832374572754})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.273907666015625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 13456], ['id', 49305], ['id', 21174], ['id', 57972], ['id', 49890], ['id', 14754], ['id', 30844], ['id', 9608], ['id', 52089], ['id', 18976]], 'labels': [9, 6, 2, 4, 5, 8, 8, 8, 7, 9], 'scores': [0.49898451566696167, 0.42536041140556335, 0.8719046115875244, 0.7524529099464417, 0.9304586052894592, 0.6252416968345642, 0.7147703766822815, 0.6177900433540344, 0.6632863283157349, 0.5709589123725891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1117398738861084})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5281611680984497})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3375861644744873})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3664047420024872})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32446014881134033})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33978503942489624})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34225451946258545})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33212602138519287})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9613, 'crossentropy': 0.2912822509765625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 6291], ['id', 30962], ['ood', 13995], ['id', 29880], ['id', 38142], ['id', 12066], ['id', 12940], ['id', 274], ['id', 49844], ['id', 32507]], 'labels': [3, 3, 2, 5, 8, 8, 5, 6, 9, 5], 'scores': [0.8356361985206604, 0.7873013615608215, 0.5148963928222656, 0.6634681820869446, 0.8460304737091064, 0.7702066898345947, 0.7959164381027222, 0.7577153444290161, 0.5933559536933899, 0.782139003276825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1935005187988281})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5214928388595581})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36735638976097107})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33038005232810974})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3023666441440582})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.286437451839447})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.294816792011261})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3128504157066345})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32356148958206177})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.252842431640625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 9940], ['id', 24347], ['id', 24632], ['id', 21390], ['id', 41379], ['id', 13018], ['id', 40653], ['id', 49519], ['id', 11600], ['id', 44040]], 'labels': [4, 2, 2, 3, 7, 8, 2, 1, 2, 0], 'scores': [0.7655036449432373, 0.7117488086223602, 0.5459679961204529, 0.8317277431488037, 0.42895156145095825, 0.6367514133453369, 0.6278688907623291, 0.7232542634010315, 0.6197584271430969, 0.7689405679702759]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0619661808013916})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5027216672897339})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3265256881713867})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31047725677490234})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28435149788856506})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32400184869766235})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.301347553730011})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3004608452320099})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.26300361328125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 18473], ['id', 55019], ['id', 32168], ['id', 14311], ['id', 26733], ['id', 27121], ['ood', 5974], ['id', 26577], ['id', 8974], ['id', 32032]], 'labels': [4, 6, 5, 0, 2, 8, 8, 2, 6, 4], 'scores': [0.782941460609436, 0.6535853743553162, 0.598239004611969, 0.4265207052230835, 0.5478687286376953, 0.6942421197891235, 0.43962693214416504, 0.5656450986862183, 0.5116991996765137, 0.598435640335083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1288397312164307})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5210839509963989})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32578474283218384})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31192857027053833})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29143819212913513})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26661235094070435})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2819353938102722})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28481385111808777})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2735433578491211})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.24781865234375}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 44754], ['id', 27783], ['id', 56066], ['id', 45602], ['id', 57822], ['id', 15769], ['id', 38035], ['id', 55244], ['id', 45944], ['ood', 43787]], 'labels': [5, 3, 7, 5, 0, 3, 0, 7, 9, 8], 'scores': [0.2986750602722168, 0.6204195022583008, 0.8173623085021973, 0.8595153093338013, 0.5165683031082153, 0.4912940263748169, 0.4766849875450134, 0.6692290306091309, 0.8588871955871582, 0.3410125970840454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.220792531967163})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5036419630050659})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3640580177307129})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3427949845790863})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3311532139778137})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32012665271759033})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28327351808547974})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3229213356971741})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3284156918525696})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2768905758857727})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3271920084953308})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2968088984489441})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3152529001235962})
store['active_learning_steps'][35]['training']['best_epoch']=10
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.2477043212890625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 18739], ['id', 34968], ['id', 1033], ['id', 58832], ['id', 588], ['id', 54880], ['id', 26405], ['id', 48649], ['id', 20641], ['id', 33150]], 'labels': [3, 8, 2, 3, 2, 5, 9, 6, 9, 8], 'scores': [0.825888603925705, 0.8697787523269653, 0.7681782245635986, 0.8583337664604187, 0.508148729801178, 0.9538761079311371, 0.7484471797943115, 0.6601970791816711, 0.7819821834564209, 0.8234644532203674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1435601711273193})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6050890684127808})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38010939955711365})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31728485226631165})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3070777952671051})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29604822397232056})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2548367381095886})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27483099699020386})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24574822187423706})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2675883173942566})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26274678111076355})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3373402953147888})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2443141357421875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 38389], ['id', 22505], ['id', 28844], ['id', 22270], ['id', 18084], ['id', 24052], ['id', 52169], ['id', 49541], ['id', 1674], ['id', 47240]], 'labels': [7, 9, 2, 0, 2, 4, 2, 9, 9, 4], 'scores': [0.7043614387512207, 0.7238895893096924, 0.8498561978340149, 0.5128476023674011, 0.6699474453926086, 0.5943443477153778, 0.7536394596099854, 0.6910151839256287, 0.8976758718490601, 0.9917799830436707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0939139127731323})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5181021690368652})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41358083486557007})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.326322078704834})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.262493371963501})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2701268792152405})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.265154093503952})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28596627712249756})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2356884521484375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 41789], ['id', 1239], ['id', 42078], ['id', 33519], ['id', 29440], ['id', 13942], ['id', 15386], ['id', 50789], ['id', 36527], ['id', 28444]], 'labels': [0, 8, 4, 8, 7, 4, 6, 1, 6, 3], 'scores': [0.6681347489356995, 0.6410272717475891, 0.6667256355285645, 0.6224748492240906, 0.7202191352844238, 0.5226861834526062, 0.49095189571380615, 0.5944787859916687, 0.5358355343341827, 0.5274862051010132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 1.0695557594299316})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.48290789127349854})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33317816257476807})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2897987365722656})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2846798896789551})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2690308690071106})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25821128487586975})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22767725586891174})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2518575191497803})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24422255158424377})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2548115849494934})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9738, 'crossentropy': 0.221833056640625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 15855], ['id', 52462], ['id', 49672], ['id', 10301], ['id', 33720], ['id', 38397], ['id', 57732], ['id', 28030], ['id', 31077], ['id', 49545]], 'labels': [5, 9, 5, 1, 4, 8, 9, 0, 9, 8], 'scores': [0.5497545599937439, 0.8423973917961121, 0.8649171590805054, 0.4988452196121216, 0.4203662872314453, 0.7138078212738037, 0.732977032661438, 0.6402634382247925, 0.6630977392196655, 0.7685260772705078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 1.0226391553878784})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5515156388282776})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3520053029060364})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3318885564804077})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28818100690841675})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2817411422729492})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2689629793167114})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2851101756095886})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2946637272834778})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.281745046377182})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.24744970703125}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 995], ['id', 4786], ['id', 30523], ['id', 55496], ['id', 15402], ['id', 48681], ['id', 43560], ['id', 43174], ['id', 5000], ['id', 18487]], 'labels': [7, 5, 8, 9, 5, 2, 5, 9, 7, 4], 'scores': [0.626473069190979, 0.41036152839660645, 0.48865246772766113, 0.6148605942726135, 0.6918126344680786, 0.8395278453826904, 0.5314750075340271, 0.5785911679267883, 0.6293456554412842, 0.8322685360908508]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1710293292999268})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5402113795280457})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3809344172477722})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3193463087081909})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2957134246826172})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30818885564804077})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2779988646507263})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.289916455745697})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2789172828197479})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26811113953590393})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2758740484714508})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31729423999786377})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2751362919807434})
store['active_learning_steps'][40]['training']['best_epoch']=10
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.247702392578125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 44822], ['id', 47888], ['id', 50639], ['id', 49487], ['id', 44350], ['id', 54994], ['id', 55368], ['id', 46368], ['id', 6952], ['id', 15486]], 'labels': [9, 8, 8, 8, 3, 6, 8, 8, 8, 3], 'scores': [0.6557702422142029, 0.6892167925834656, 0.7824962139129639, 0.8191673755645752, 0.907966673374176, 0.8371133208274841, 0.8434962034225464, 0.7834329605102539, 0.9323858022689819, 0.5985927581787109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1162643432617188})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.547285258769989})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3642357587814331})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36939895153045654})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28378772735595703})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2984410524368286})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.256997287273407})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26380470395088196})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2732546329498291})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25551754236221313})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28375890851020813})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2633087635040283})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2883226275444031})
store['active_learning_steps'][41]['training']['best_epoch']=10
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.250024755859375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 35710], ['id', 57211], ['id', 37758], ['id', 52800], ['id', 16286], ['id', 6174], ['id', 47741], ['id', 20037], ['id', 23732], ['id', 30359]], 'labels': [1, 5, 0, 9, 0, 9, 5, 8, 9, 7], 'scores': [0.5434178113937378, 0.6239271759986877, 0.8795787692070007, 0.7618096470832825, 0.7650132775306702, 0.9445526003837585, 0.676678478717804, 0.8689240217208862, 0.7901409268379211, 0.8358056545257568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1920220851898193})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6340254545211792})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37682104110717773})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3515945076942444})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.292840838432312})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26486390829086304})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2915359139442444})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2890017032623291})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2753034830093384})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2498900390625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 16690], ['id', 34739], ['id', 2550], ['id', 12986], ['id', 31861], ['id', 49656], ['id', 41295], ['id', 43310], ['id', 38315], ['id', 42437]], 'labels': [2, 9, 2, 5, 7, 9, 9, 9, 0, 9], 'scores': [0.335732102394104, 0.6463994383811951, 0.5301793217658997, 0.6472108960151672, 0.5175716280937195, 0.6443687677383423, 0.6207003593444824, 0.7196523547172546, 0.5272677540779114, 0.5548820495605469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3679343461990356})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5659618377685547})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4068605303764343})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3215456008911133})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28629547357559204})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27387896180152893})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2976904809474945})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26653021574020386})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2590488791465759})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24551859498023987})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2731199264526367})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25571492314338684})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2891290485858917})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9766, 'crossentropy': 0.2101173583984375}
